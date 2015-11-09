FROM python:3.4

COPY . /srv
RUN pip install -r /srv/requirements.txt
<<<<<<< HEAD


EXPOSE 5000

CMD ["python", "/srv/tatooine.py"]
=======

EXPOSE 5000
CMD ["python", "/srv/tatooine.py"]
>>>>>>> 1e5e6ccdd2d06c910d11e9d2066745a00c8419e9
