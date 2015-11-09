FROM debian:stretch

RUN apt-get update -y

RUN apt-get install nginx -y

CMD ["nginx", "-g", "daemon off;"]

