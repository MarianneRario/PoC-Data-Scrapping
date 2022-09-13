from flask import Flask
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time

app = Flask(__name__)

desired_capabilities = {
    "platformName": "Android",
    "appium:udid": "{192.0.0.0:5555}", # insert udid of your android device
    "appium:ignoreHiddenApiPolicyError": "true"
}

driver = webdriver.Remote(f"http://0.0.0.0:4723/wd/hub", desired_capabilities)

@app.route('/<num>')
def gcash_automate(num):
    WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, '(//android.widget.\
                    ImageView[@content-desc="description"])[1]'))).click()

    WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.\
                    FrameLayout/android.widget.LinearLayout/\
                    android.widget.FrameLayout/android.widget.\
                    LinearLayout/android.widget.FrameLayout/\
                    android.widget.FrameLayout/android.widget.\
                    RelativeLayout/android.view.ViewGroup/android.\
                    view.ViewGroup/android.widget.ScrollView/android.\
                    widget.LinearLayout/android.view.ViewGroup[1]/\
                    android.widget.FrameLayout[1]/android.widget.\
                    LinearLayout/android.widget.ImageView' ))).click()

    time.sleep(1)
    driver.execute_script("mobile: shell", {"command": "input text", "args": num})
    driver.execute_script("mobile: shell", {"command": "input text", "args": 1})

    driver.execute_script('mobile: shell', {'command': 'input', 'args': 'keyevent 61'})
    driver.execute_script('mobile: shell', {'command': 'input', 'args': 'keyevent 61'})
    driver.execute_script('mobile: shell', {'command': 'input', 'args': 'keyevent 61'})
    driver.execute_script('mobile: shell', {'command': 'input', 'args': 'keyevent 66'})

    time.sleep(0.1)

    name = driver.find_element(By.XPATH, "/hierarchy/android.widget.\
            FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout\
            /android.widget.LinearLayout/android.widget.FrameLayout/\
            android.widget.FrameLayout/android.widget.FrameLayout/\
            android.widget.LinearLayout/android.widget.RelativeLayout/\
            android.widget.ScrollView/android.widget.LinearLayout/android.\
            widget.LinearLayout[1]/android.widget.TextView[1]").text
    print('here')
    TouchAction(driver).tap(None, 54, 104, 1).perform()
    TouchAction(driver).tap(None, 54, 104, 1).perform()
    TouchAction(driver).tap(None, 54, 104, 1).perform()
    return name

if __name__ == '__main__': 
    app.run()