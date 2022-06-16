FROM python:3.10.0

COPY ./ /home/udi_barcode/

WORKDIR /home/udi_barcode/

RUN apt-get update
RUN apt-get install zbar-tools -y
RUN apt-get install libzbar-dev -y
RUN apt-get install libgl1-mesa-glx -y
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver --insecure 0.0.0.0:8000"]