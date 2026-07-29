FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

EXPOSE 7860

CMD ["python","app.py"]