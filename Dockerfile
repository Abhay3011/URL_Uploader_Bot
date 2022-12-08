FROM python:3.10.6-bullseye
RUN pip install --upgrade pip 
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3","bot.py"]
