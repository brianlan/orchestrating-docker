FROM nginx:1.10.2
RUN mkdir -p /etc/nginx/conf.d
COPY ./flask_project.conf /etc/nginx/conf.d/flask_project.conf
RUN rm  /etc/nginx/conf.d/default.conf
#RUN cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
