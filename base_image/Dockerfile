FROM python:3.8

COPY requirements.txt /opt
RUN pip3 install --no-cache-dir -r /opt/requirements.txt

CMD ["python3"]

# TODO: github job to build new image whenever a new package is added to poetry
