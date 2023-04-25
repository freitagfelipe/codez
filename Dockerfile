FROM python:3.10-bullseye

COPY . .

RUN pip install pipenv
RUN pipenv install

CMD [ "pipenv", "run", "start" ]