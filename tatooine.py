from flask import Flask
import consul
import socket
import pprint
import redis


# Consul key
CONSUL_REDIS_KEY = "redis"

app = Flask(__name__)

def GetRedisFromConsul():
    MyConsul = consul.Consul(host='consul', port=8500)
    Index, ConsulRetObj = MyConsul.catalog.service(CONSUL_REDIS_KEY)

    pprint.pprint(ConsulRetObj)

    ServiceAddress = ConsulRetObj[0]['Address'].decode("utf-8") 
    ServicePort = ConsulRetObj[0]['ServicePort'].decode("utf-8") 
    
    return ServiceAddress, ServicePort


def GetCounterFromRedis(PServer, PPort):
    
    Myredis = redis.StrictRedis(host=PServer, port=PPort, db=0)
    Myredis.incr("value")

    return Myredis.get('value')


@app.route("/")
def hello():
    try:
    
        RedisServiceAddress, RedisServicePort = GetRedisFromConsul()

        Output = "Redis Server : %s:%s - counter value : %s" % (RedisServiceAddress,RedisServicePort, GetCounterFromRedis(RedisServiceAddress , RedisServicePort))
    
    except Exception as e:
        return("Error : %s" % str(e))
    return Output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
