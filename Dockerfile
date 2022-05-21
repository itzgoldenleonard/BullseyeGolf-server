FROM python:latest

WORKDIR ./

COPY . .

RUN pip install build

RUN python -m build

RUN pip install dist/bgserver-*.whl

RUN pip install gunicorn

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "bgserver:create_app()" ]
