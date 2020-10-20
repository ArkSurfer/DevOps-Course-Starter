FROM python:3.8.6-slim-buster as base

ENV POETRY_VERSION=1.1.0

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . ./app
WORKDIR /app

FROM base as development
EXPOSE 5000
ENTRYPOINT ["./run_dev.sh"]

FROM base as production
RUN pip install gunicorn
EXPOSE 5050
ENTRYPOINT ["./run_prod.sh"]