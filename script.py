import time
import json
from bson import ObjectId
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient

client = MongoClient('mongodb+srv://goelanurag2003:So3PNlrVCW2NXSvi@cluster0.px4selc.mongodb.net/')
db = client['twitter_trends']
collection = db['trends']

chrome_driver_path = 'chromedriver.exe'

proxymesh_url = "http://anurag09:anurag@us-wa.proxymesh.com:31280"

def get_trending_topics():
    # Configure proxy
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxymesh_url,
        'sslProxy': proxymesh_url,
        'noProxy': ''  # set this value as desired
    })

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={proxymesh_url}')

    # Initialize the Chrome driver with proxy
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open Twitter login page
        driver.get("https://x.com/i/flow/login")
        time.sleep(8)
        username = driver.find_element(By.TAG_NAME, "input")
        username.send_keys("AnuragGoel2003")
        username.send_keys(Keys.RETURN)
        time.sleep(5)
        password = driver.find_element(By.NAME, "password")
        password.send_keys("goelanurag2003")
        password.send_keys(Keys.RETURN)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]'))
        )

        # Locate the "What’s Happening" section and fetch the top 5 trending topics
        trending_section = []
        for i in range(3, 8):
            trending_section.append(driver.find_element(By.XPATH, f'//div[@aria-label="Timeline: Trending now"]/div/div[{i}]/div/div/div/div[2]/span'))

        trends = [topic.text for topic in trending_section]
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Fetch IP address used       
        driver.get("https://api.ipify.org?format=text")
        ip_address = driver.find_element(By.TAG_NAME, 'pre').text

        trend_data = {
            "trend1": trends[0],
            "trend2": trends[1],
            "trend3": trends[2],
            "trend4": trends[3],
            "trend5": trends[4],
            "end_time": end_time,
            "ip_address": ip_address
        }

        collection.insert_one(trend_data)

        def convert_objectid_to_string(obj):
            if isinstance(obj, ObjectId):
                return str(obj)
            elif isinstance(obj, list):
                return [convert_objectid_to_string(item) for item in obj]
            elif isinstance(obj, dict):
                return {key: convert_objectid_to_string(value) for key, value in obj.items()}
            return obj

        return json.dumps(convert_objectid_to_string(trend_data))

    finally:
        driver.quit()

if __name__ == "__main__":
    result = get_trending_topics()
    print(result)
