from alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

#WORKDIR /app
#COPY . /app

#RUN pip3 --no-cache-dir install -r requirements.txt

#RUN oc project gamification
#RUN ssh mysql-4-s6hbv 3306:3306

#EXPOSE 3306

ENTRYPOINT ["python3"]
CMD ["main.py"]
