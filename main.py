# just a random useful and at the same time a rather very funny project and even addictive at some times when you are angry or just feeling you are a useless person on the web
# So here I am after wasting my couple of useless minutes on this weird project 


import pyautogui
import webbrowser
import time
import random


# our slap class in python
class Slap:
    def __init__(self):
        self.URL = "http://eelslap.com/"
        self.run_time = random.randint(60, 100)

    def open_webpage_in_browser(self):
        webbrowser.open(self.URL)


    def slap_time(self):
        for i in range(self.run_time):
            pyautogui.moveTo(100, 415, duration=3)
            pyautogui.moveTo(1000, 415, duration=2)

    def run(self):
        self.open_webpage_in_browser()
        time.sleep(2)
        self.slap_time()
       

if __name__ == "__main__":
    slap = Slap()
    slap.run()
