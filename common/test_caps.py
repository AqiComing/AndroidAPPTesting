import os,sys

import yaml
from appium import webdriver

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

def caps():
    caps_config_path = os.path.join(base_dir, 'config','caps_config.yaml')
    with open(caps_config_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps={
        "platformName": data["platformName"],
        "platformVersion": data["platformVersion"],
        "deviceName": data["deviceName"],
        "appPackage": data["appPackage"],
        "appActivity": data["appActivity"]

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
    # driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

if __name__ == '__main__':
    caps()
