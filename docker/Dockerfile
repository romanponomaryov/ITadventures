FROM python:3.7.1-slim-stretch

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
	gcc \
	default-libmysqlclient-dev \
	vim \
	nano \ 
	mc 
ADD . /app/src/
WORKDIR /app/src
RUN pip install -r requirements.txt

WORKDIR /app/src/groupsite
CMD [ "python", "manage.py", "runserver"]
 
EXPOSE 8000

