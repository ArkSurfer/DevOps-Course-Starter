FROM python:3.8.6-slim-buster as base

ENV POETRY_VERSION=1.1.0

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . ./app
WORKDIR /app

# testing stage
FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]


# local development stage
FROM base as development
EXPOSE 5000
ENTRYPOINT ["./run_dev.sh"]

# production build stage
FROM base as production
RUN pip install gunicorn
EXPOSE 8000
ENTRYPOINT ["./run_prod.sh"]