FROM python:3

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PYSETUP_PATH="/usr/src/app" \
  POETRY_VERSION=1.2.0 \
  POETRY_HOME="/usr/src/app/poetry" \
  POETRY_VENV="/usr/src/app/poetry-venv"

# prepend poetry and venv to path
ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN pip install "poetry==$POETRY_VERSION"

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml $PYSETUP_PATH

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-ansi

CMD ["poetry", "run", "python", "web-service.py"]