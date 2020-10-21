#!/usr/bin/python3
import subprocess
import time
import pyautogui
import sys
meeting_id=0;
meeting_pass=0;
with open("config/meeting_id_pass.txt", "r") as file:
    data = file.readlines()
    meeting_id = data[0]
    meeting_pass = data[1]

#location of zoom application
subprocess.Popen("zoom");
#wait for the application to open
time.sleep(13)
print("Sleep over")
#join btn
join_btn_coord = pyautogui.locateOnScreen("img/join_btn.png");
print(join_btn_coord)
pyautogui.moveTo(join_btn_coord[0],join_btn_coord[1])
print("MOving")
pyautogui.click()
time.sleep(2)
meeting_id_coord =  pyautogui.locateOnScreen("img/input_meeting_id.png")
pyautogui.moveTo(meeting_id_coord[0]+40, meeting_id_coord[1])
pyautogui.click()
pyautogui.write(meeting_id)
pyautogui.press("return")
time.sleep(3)

time.sleep(2)
meeting_pass_coord = pyautogui.locateCenterOnScreen("img/pass_input.png")
pyautogui.moveTo(meeting_pass_coord[0], meeting_pass_coord[1])
pyautogui.click()
pyautogui.write(meeting_pass)
pyautogui.press("return")



