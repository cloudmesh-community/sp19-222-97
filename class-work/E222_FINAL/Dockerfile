FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /server/requirements.txt
WORKDIR /server
RUN pip install -r requirements.txt

COPY ./requirements.txt ./data_tree.py ./linear_regressor.py./swagger.yaml ./server.py /server

ENTRYPOINT ["python"]

CMD ["server.py"]