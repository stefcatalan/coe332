FROM python:3.9

RUN pip3 install pytest==7.0.0
RUN pip3 install --user xmltodict

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY test_app.py /app/test_app.py
COPY positionData.json /app/positionData.json
COPY sightingData.json /app/sightingData.json
COPY ISS.OEM_J2K_EPH.xml /app/ISS.OEM_J2K_EPH.xml
COPY XMLsightingData_citiesUSA01.xml /app/XMLsightingData_citiesUSA01.xml

RUN pip install -r /app/requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
