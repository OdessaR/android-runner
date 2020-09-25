# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# import ahk

# firefox = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
# from selenium import webdriver

# driver = web.Firefox(firefox_binary=firefox)
# driver.get("http://www.yahoo.com")
# ahk.start()
# ahk.ready()
# ahk.execute("Send,^s")
# ahk.execute("WinWaitActive, Save As,,2")
# ahk.execute("WinActivate, Save As")
# ahk.execute("Send, C:\\path\\to\\file.htm")
# ahk.execute("Send, {Enter}")

from selenium import webdriver
import pyautogui
import time
import logging
import os
import glob
from pathlib import Path
import subprocess


# print(os.path.sep)
BASE_DOWNLOAD_FOLDER = ["", "home", "user", "Downloads"]



logging.basicConfig(level=logging.INFO)

def fetch(url: str, save_path: str):
    logging.info("Starting webbrowser")
    driver = webdriver.Firefox()

    logging.info("Going to: %s" % url)
    driver.get(url)
    time.sleep(2.5)

    logging.info("Opening file save dialog")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(0.75)

    logging.info("Writing path to save: %s" % save_path)
    pyautogui.write(save_path, interval=0.1)
    time.sleep(0.1)

    logging.info("Saving...")
    pyautogui.press('enter') 
    time.sleep(2.5)

    logging.info("Closing browser")
    driver.quit()


urls = ["google.nl", "nos.nl"]
for url in urls:
    folder_path = BASE_DOWNLOAD_FOLDER + [url]
    jsbeautifier_path = BASE_DOWNLOAD_FOLDER + [url, "jsbeautifier"]
    purified_path = BASE_DOWNLOAD_FOLDER + [url, "pure"]
    save_path = folder_path + [url]
    
    try:
        os.mkdir(os.path.sep.join(folder_path))
    except Exception as e:
        logging.error(e)
    try:
        os.mkdir(os.path.sep.join(jsbeautifier_path))
    except Exception as e:
        logging.error(e)
    try:
        os.mkdir(os.path.sep.join(purified_path))
    except Exception as e:
        logging.error(e)

    fetch("http://%s" % url, os.path.sep.join(save_path))

    jsbeautifiers = []
    for js_file in glob.glob(os.path.sep.join(save_path) + "**/*.js", recursive=True):
        file_name = js_file[len(os.path.sep.join(save_path)+"_files/"):]
        jsbeautifier_file_location = os.path.sep.join(jsbeautifier_path + [file_name])
        subprocess.call("js-beautify '%s' > %s" % (js_file, jsbeautifier_file_location), shell=True)
        logging.info("js-beautify '%s' > '%s'" % (js_file, jsbeautifier_file_location))
        jsbeautifiers.append(jsbeautifier_file_location)

    for js_file in jsbeautifiers:
        lines_to_delete = []
        try:
            stdout = subprocess.check_output("purecheck '%s'" % js_file, shell=True).decode("utf-8")
            if not stdout.startswith("Impure function"): continue
            for line in stdout.split("\n"):
                parts = line[26:].split(")")[0].split(",")
                if len(parts) != 2: continue
                lines_to_delete.append(int(parts[0]))
        except: continue

        js_lines = []
        with open(js_file, "r") as f: js_lines = f.readlines()
        for line_number in sorted(set(lines_to_delete), reverse=True):
            js_lines.pop(line_number-1)

        pure_path = os.path.sep.join(purified_path + [js_file[len(os.path.sep.join(jsbeautifier_path+[""])):]])
        
        with open(pure_path, "w") as f: js_lines = f.writelines(js_lines)
        logging.info("New pure js file: %s" % pure_path)

        try:
            subprocess.call("rm -rf '%s'" % os.path.sep.join(folder_path + ["%s_files" % url]))
        except Exception as e:
            logging.error(e)
        try:
            subprocess.call("rm -rf '%s'" % os.path.sep.join(folder_path + ["%s_files" % url]))
        except Exception as e:
            logging.error(e)

        # print("".join(js_lines))

    


