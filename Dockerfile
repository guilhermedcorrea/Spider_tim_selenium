FROM python:3.11

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

ENV HOST 0.0.0.0
ENV PORT 5001
ENV DEBUG true

COPY . .
WORKDIR /app

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt




