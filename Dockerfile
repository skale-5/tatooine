FROM python:3.4

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "tatooine.py"]