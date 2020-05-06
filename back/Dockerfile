FROM ubuntu:18.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Set the working directory to /phonemizer
WORKDIR /phonemizer

# install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        festival \
        espeak-ng \
        git \
        python3 \
        python3-pip \
        python3-pytest && \
    apt-get clean

# install phonemizer and run the tests
RUN git clone https://github.com/bootphon/phonemizer.git && \
    cd phonemizer && \
    python3 setup.py install

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/hackathon-ima-2019-751c334d5318.json
WORKDIR /app
ENV FLASK_APP=app.py
COPY . .

RUN python3 -m pip install -r requirements.txt
RUN python3 -m spacy download fr_core_news_md &&\
    python3 -m spacy link fr_core_news_md fr

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" , "--debugger"]
# CMD [ "tail", "-f", "/dev/null" ]
