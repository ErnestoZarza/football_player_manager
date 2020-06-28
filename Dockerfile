FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /football_player_manager
WORKDIR /football_player_manager
COPY requirements.txt /football_player_manager/
RUN pip install -r requirements.txt
COPY . /football_player_manager/
# EXPOSE 5000
CMD chmod +x start_code.sh
CMD bash -c ./start_code.sh
