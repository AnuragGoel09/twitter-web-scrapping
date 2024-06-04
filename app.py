import time
import json
from bson import ObjectId
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from flask import Flask,jsonify,request
from flask_cors import CORS
from script import get_trending_topics
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

app=Flask(__name__)

def download_selenium():
    chromeoptions=webdriver.ChromeOptions()
    chromeoptions.add_argument("--headless")
    chromeoptions.add_argument("--no-sandbox")
    chromeoptions.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()),options=chromeoptions)
    return {"message":"download dn"}

@app.route('/',methods =['GET','POST'])
def home():
    if(request.method == 'GET'):
        return download_selenium()
    return {"message":"not get"}

if __name__=="__main__":
    app.run()