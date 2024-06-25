## RABBITMQ SCHEDULER
import requests

def getDataFromRMQ():
    rmq = {"rmq": 'helloWorld1'}
    return rmq

def sendDataToCore(payload):
    url = 'http://localhost:5005/api'


    x = requests.post(url, json = payload)
    print(x.status_code)
    
result = getDataFromRMQ()
sendDataToCore(result)