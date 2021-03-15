FROM python:3.7.6

ENV PORT 8081

COPY ./app/app.py /app/app.py

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]