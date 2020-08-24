#use python 3.7 image
FROM python:3.7-slim

#set the working directory
WORKDIR /opt/app

#ENV PYTHONPATH "${PYTHONPATH}:app/services"
#ENV PYTHONPATH "${PYTHONPATH}:app/utils"

#install Project requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

#copy contents to container automatic-forensic-tool
ADD app .


#start app
CMD bash run.sh
