FROM python:3.4

COPY . /srv
RUN pip install -r /srv/requirements.txt

EXPOSE 5000
CMD ["python", "/srv/tatooine.py"]
