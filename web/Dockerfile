FROM celery:3.1.24
ADD . /web
WORKDIR /web
USER root
RUN pip install -r requirements.txt
USER user