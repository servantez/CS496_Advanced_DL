FROM python:2.7-stretch

WORKDIR /usr/src/ensemble-adv-training-master

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/ensemble-adv-training-master
CMD ["python", "./main.py"]