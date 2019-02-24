FROM selenium/standalone-chrome-debug

RUN set -x && \
sudo apt-get update && \
sudo apt-get install -y python3-pip && \
pip3 install selenium

COPY firstTest.py /home
RUN sudo chmod +x /home/firstTest.py