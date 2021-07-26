FROM dabarnyarddawg/kf-pipelines-base-images:latest

WORKDIR home
RUN mkdir src
COPY src src/
ENV PYTHONPATH=/home

CMD ["python3"]