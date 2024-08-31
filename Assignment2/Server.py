from flask import Flask, request, jsonify
import requests
import google.generativeai as genai
import os
import time
import json

app = Flask(__name__)

from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')


@app.route('/generate', methods=['POST'])
def generate_content():
    # Get the prompt from the client's request
    client_data = request.json
    client_id=client_data.get('ClientID')
    if client_id=="ehdur3279fj&*jt49" or "swgdbd926%$@bshw" or "shwjdb2386^#**nd":
        prompt = client_data.get('prompt')

        TimeSent=time.time()
        inresponse = model.generate_content(prompt)
        TimeRecvd=time.time()

        response={
            "Prompt":prompt, 
            "Message": (inresponse.text), 
            "TimeSent": TimeSent, 
            "TimeRecvd": TimeRecvd,
            "ClientID":client_id,
            "Source": "Gemini"}

        return jsonify(response)
    
    else:
        response='Incorrect key'
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
