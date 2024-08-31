import google.generativeai as genai
import os
import time
import json


from dotenv import load_dotenv

load_dotenv()

#api key set as an environment variable in an .env file
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

empty_data = []
with open('/home/madhav/Documents/DaSHLab/Assignment1/output.json', 'w') as json_file:
    json.dump(empty_data, json_file, indent=4)


inputpromptfile=open("/home/madhav/Documents/DaSHLab/Assignment1/input.txt",'r')
inputprompts=inputpromptfile.read().splitlines()

for i in inputprompts:

    TimeSent=time.time()
    inresponse = model.generate_content(i)
    TimeRecvd=time.time()

    response={
        "Prompt":i, 
        "Message": (inresponse.text), 
        "TimeSent": TimeSent, 
        "TimeRecvd": TimeRecvd, 
        "Source": "Gemini"}
    
    with open("/home/madhav/Documents/DaSHLab/Assignment1/output.json", "r") as json_file:
        data = json.load(json_file)
        data.append(response)

    with open("/home/madhav/Documents/DaSHLab/Assignment1/output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


with open("/home/madhav/Documents/DaSHLab/Assignment1/output.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
