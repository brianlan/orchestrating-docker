FROM celery:3.1.24
ADD . /post_writer
WORKDIR /post_writer
USER root
RUN pip install -r requirements.txt
USER user