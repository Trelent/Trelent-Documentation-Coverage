FROM ubuntu:18.04

WORKDIR /action

RUN apt-get update && apt-get install python3 python3-pip python3-pygit2 -y


ENV SOURCE_PATH "./"

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD src/* ./

ENTRYPOINT [ "./start.sh" ]