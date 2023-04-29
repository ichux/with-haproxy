FROM nginx:1.23.4

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/sites-available/default.conf

RUN mkdir /etc/nginx/sites-enabled && ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/ && \
    sed -i 's/Server: nginx/Server: piccl/' `which nginx` && \
    sed -i 's/center>nginx/center>piccl/' `which nginx`

CMD ["nginx", "-g", "daemon off;"]
