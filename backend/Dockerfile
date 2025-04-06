ARG PYTHON_IMAGE=python:3.12.3

FROM ${PYTHON_IMAGE}

WORKDIR /app

COPY ./backend/app ./backend/app
COPY ./pyproject.toml ./
COPY ./poetry.lock ./
COPY ./start-dev.sh ./

ENV VENV_PATH="/opt/venv"
RUN python -m venv ${VENV_PATH}

SHELL ["/bin/bash", "-c"]

RUN source "$VENV_PATH/bin/activate" && pip install poetry
RUN source "$VENV_PATH/bin/activate" && poetry config virtualenvs.create false
RUN source "$VENV_PATH/bin/activate" && poetry install --no-root

RUN chmod a+x ./start-dev.sh
CMD ["bash", "./start-dev.sh"]