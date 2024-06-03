from flask import Flask,jsonify
from flask_cors import CORS
from script import get_trending_topics
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
setup_done = False

def setup():
    chrome_driver_path = './chromedriver.exe'

    proxymesh_url = "http://anurag09:anurag@open.proxymesh.com:31280"
    
    service = Service(ChromeDriverManager().install())
    return service
    return webdriver.Chrome(service=service,options=chrome_options)

def initialize_driver():
    global setup_done
    if not setup_done:
        print("start")
        app.service = setup()
        print("drivers")
        setup_done = True

initialize_driver()

@app.route('/')
def index():
    return jsonify(message="Welcome to the Trending Topics App")

@app.route('/run_script', methods=['POST'])
def run_script():
    result = get_trending_topics(app.service)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
