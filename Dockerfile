FROM python:3.8.6-slim-buster
ENV POETRY_VERSION=1.1.0
RUN pip install "poetry==$POETRY_VERSION"
COPY . ./app
WORKDIR /app
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

RUN pip install gunicorn
EXPOSE 5050
ENTRYPOINT ["./run.sh"]