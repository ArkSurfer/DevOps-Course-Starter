FROM python:3.8.6-buster as base

ENV POETRY_VERSION=1.1.0

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . ./app
WORKDIR /app

# testing stage
FROM base as test

RUN apt-get update &&\
  apt-get upgrade -y &&\
  curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
  apt-get install ./chrome.deb -y &&\
  rm ./chrome.deb
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
 echo "Installing chromium webdriver version ${LATEST}" &&\
 curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
 apt-get install unzip -y &&\
 unzip ./chromedriver_linux64.zip

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