FROM python:3.4

COPY . /srv
RUN pip install -r /srv/requirements.txt
RUN echo "consul 172.17.42.1" >> /etc/hosts

EXPOSE 5000
CMD ["python", "/srv/tatooine.py"]
