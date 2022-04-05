FROM python:3.9

RUN mkdir /data
WORKDIR /data

COPY requirements.txt /data/requirements.txt
COPY ML_Data_Sample.json /data/ML_Data_Sample.json
COPY data.json /data/data.json

RUN pip install -r /data/requirements.txt
COPY . /data

ENTRYPOINT ["python"]
CMD ["app.py"]
