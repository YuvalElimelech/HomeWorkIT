FROM python:3
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 9090
COPY . /
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
