FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/
COPY ./train.py /app/
COPY ./deploy.py /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# RUN python train.py
COPY ./model/model.joblib /app/model/

EXPOSE 8000

CMD ["uvicorn", "deploy:app", "--host", "0.0.0.0", "--port", "8000"]

#RUN mkdir -p data model
