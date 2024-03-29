# recap2

# may god bless me

# misc
import time
import os


# webdriver tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request


# speech recognition
import speech_recognition as sr
from pydub import AudioSegment





def checkbox(driver):
    wait = WebDriverWait(driver, 3)
    elements = driver.find_elements(By.TAG_NAME, "iframe")
    for i in elements:
        try:
            driver.switch_to.frame(i)
            checkbox = driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border")
            checkbox.click()
            driver.switch_to.default_content()
            break
        except:
            pass

    else:
        print("No checkbox found skipping!")


def audio_button(driver):
    wait = WebDriverWait(driver, 3)
    elements = driver.find_elements(By.TAG_NAME, "iframe")
    global x
    for x in elements:
        try:
            driver.switch_to.default_content()
            driver.switch_to.frame(x)
            audio_button = driver.find_element(By.CSS_SELECTOR, "#recaptcha-audio-button")
            audio_button.click()
            print('found yeah yeah')
            driver.switch_to.default_content()
            break
        except:
            pass
    else:
        raise Exception("audio button not found") # raise for Exception

def download_audio(driver):
    wait = WebDriverWait(driver, 3)
    try:
        driver.switch_to.frame(x)
        valid = driver.find_element(By.ID, ':2')
        audio_element = driver.find_element(By.TAG_NAME, "audio")
        audio_source_url = audio_element.get_attribute("src")
        urllib.request.urlretrieve(audio_source_url, "aud.mp3")
        print("audio link downloaded")
    except Exception as e:
        raise Exception("error occured") # raise for Exception



def mpeg2flac():
    audio = AudioSegment.from_mp3("aud.mp3")
    audio.export("aud.flac", format="flac")
    os.remove("aud.mp3")


def speech2text():
    recognizer = sr.Recognizer()
    with sr.AudioFile("aud.flac") as source:
        audio_data = recognizer.record(source)

    try:
        api = "POVM26FPJ6536YNBDK6J4UDOIIUQ667H"
        text = recognizer.recognize_wit(audio_data, api)
        return text
    except:
        print("Speech Recognition could not understand audio. Using backup speech-recognition..")
        text = backup_speech2text()
        return text


def backup_speech2text():
    recognizer = sr.Recognizer()
    with sr.AudioFile("aud.flac") as source:
        audio_data = r.record(source)
    try:
        backup_text = r.recognize_google(audio_data)
        return backup_text
    except:
        pass



def text_input(driver, text):
    wait = WebDriverWait(driver, 3)
    response = driver.find_element(By.CSS_SELECTOR, "#audio-response")
    response.send_keys(text + Keys.RETURN)
    try:
        valid = driver.find_element(By.NAME, "Multiple correct solutions required - please solve more.")
        print("Error occurred using backup speech-recognition")
        backup_text = backup_speech2text()
        response.send_keys(backup_text + Keys.RETURN)
    except:
        pass



def recaptcha(driver):
    checkbox(driver)
    time.sleep(1)
    audio_button(driver)
    time.sleep(1)
    download_audio(driver)
    mpeg2flac()
    text_input(driver, text = speech2text())