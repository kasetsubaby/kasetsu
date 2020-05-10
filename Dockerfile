FROM perl:5.30.2
LABEL maintainer="ybrliiu <raian@reeshome.org>"

RUN cpanm --notest Carton App::cpm

CMD cd /usr/local/projects/kasetsu \
  && cpm install --no-test \
  && grep "script/log_file/" .gitignore | xargs touch \
  && carton exec -- plackup -s Gazelle app.psgi
