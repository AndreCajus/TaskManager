FROM ubuntu
RUN apt update -y && \
    apt-get upgrade -y && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.8 && \
    apt install -y python3-pip && \
    apt install -y libpq-dev && \
    apt install -y python3-dev
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip3 install -r requirements.txt
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable && \
    apt update -y && \
    apt upgrade -y && \
    apt-get install -y gdal-bin && \
    apt install libgdal-dev -y && \
    apt-get install -y python3-gdal && \
    apt-get install -y python3-numpy && \
    add-apt-repository ppa:thomas-schiex/blender
EXPOSE 80