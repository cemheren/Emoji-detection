# docker build -t 
FROM ubuntu1604py27

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY local.py local.py
COPY . .

EXPOSE 5000

CMD ["python", "local.py"]