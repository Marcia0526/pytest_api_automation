FROM python:3
MAINTAINER marciatsai0526@gmail.com
WORKDIR /work_dir
COPY . /work_dir
RUN pip install -r requirements.txt
RUN echo $PWD
CMD pytest -v --alluredir=./report --clean-alluredir

