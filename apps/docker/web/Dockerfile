FROM python:3.12.2-slim as requirements-stage

WORKDIR /tmp

RUN pip install poetry --no-cache-dir poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12.2-slim

WORKDIR /app/web/

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./apps/web/ .

COPY ./apps/web/start.sh .

RUN chmod +x /app/web/start.sh

CMD ["sh", "/app/web/start.sh"]