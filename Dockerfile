FROM dabarnyarddawg/kf-pipelines-base-images:latest

WORKDIR home
RUN mkdir src
COPY src src/

CMD ["python3"]