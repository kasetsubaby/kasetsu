FROM perl:5.30.2
LABEL maintainer="ybrliiu <raian@reeshome.org>"

COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY etc/nginx/conf.d/kasetsu.conf /etc/nginx/conf.d/kasetsu.conf

RUN wget -O /tmp/nginx_signing.key https://nginx.org/keys/nginx_signing.key \
  && APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1 apt-key add /tmp/nginx_signing.key \
  && echo 'deb http://nginx.org/packages/ubuntu/ bionic nginx' >> /etc/apt/sources.list \
  && echo 'deb-src http://nginx.org/packages/ubuntu/ bionic nginx' >> /etc/apt/sources.list \
  && apt-get update \
  && yes N | apt-get install nginx \
  && service nginx start \
  && cpanm --notest Carton App::cpm

CMD cd /usr/local/projects/kasetsu \
  && cpm install --no-test \
  && grep "script/log_file/" .gitignore | xargs touch \
  && carton exec -- plackup -s Gazelle app.psgi
