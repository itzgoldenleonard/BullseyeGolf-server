FROM python:latest

WORKDIR ./

COPY . .

RUN pip install build

RUN python -m build

RUN pip install --force-reinstall dist/gbserver-*.whl

RUN pip install gunicorn

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "gpserver:create_app()" ]

