FROM python:3.10-alpine3.18

COPY dist/ dist/

RUN pip install dist/dockerization-1.0.0-py3-none-any.whl

EXPOSE 8000

CMD uvicorn api.server:create_api --host 0.0.0.0 --port 8000