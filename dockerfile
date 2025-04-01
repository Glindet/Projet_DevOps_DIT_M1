FROM ubuntu:latest 
RUN apt update 
RUN apt install python3 python3-pip -y 
COPY manage.py ./ 
CMD ["python3", "./manage.py"]