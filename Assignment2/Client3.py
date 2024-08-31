import requests
from flask import Flask, request, jsonify
import requests
import google.generativeai as genai
import os
import time
import json


SERVER_URL = "http://localhost:5000/generate"

def send_prompt(prompt):
    # Send the prompt to the server
    response = requests.post(SERVER_URL, json={"prompt": prompt,"ClientID":"shwjdb2386^#**nd"})
    return response.json()


inputpromptfile=open("/home/madhav/Documents/DaSHLab/Assignment1/input.txt",'r')
inputprompts=inputpromptfile.read().splitlines()

empty_data = []
with open('/home/madhav/Documents/DaSHLab/Assignment2/output3.json', 'w') as json_file:
    json.dump(empty_data, json_file, indent=4)


inputpromptfile=open("/home/madhav/Documents/DaSHLab/Assignment1/input.txt",'r')
inputprompts=inputpromptfile.read().splitlines()
k=len(inputprompts)
i=9
while i<k :

    prompt = inputprompts[i]
    if __name__ == "__main__":
        response = send_prompt(prompt)
    if response == 'Incorrect key':
        print('incorrect key')
        quit()
    if response["Prompt"]!=prompt:
        response["Source"]="user"

    
    with open("/home/madhav/Documents/DaSHLab/Assignment2/output3.json", "r") as json_file:
        data = json.load(json_file)
        data.append(response)

    with open("/home/madhav/Documents/DaSHLab/Assignment2/output3.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    i=i+1


with open("/home/madhav/Documents/DaSHLab/Assignment2/output3.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
