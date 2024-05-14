# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev build-essential

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
WORKDIR ${waitlis}

#Install pip requirements

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh
COPY . /app/

#RUN chmod +x entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh" ]