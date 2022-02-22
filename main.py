#!/usr/bin/env python3

import requests
import sys
import pyperclip
import clipboard

def getURLID():
    text = clipboard.paste()
    text = text.strip()
    result = 0
    if len(text) <= 6:
        return text
    else:
        idPreSlice = text.find("?id=")
        idSlice = idPreSlice + 4

        result = text[idSlice:(len(text))] 
    
    return result

def extractMeetingURL(InformationExtract):
    InformationExtract = str(InformationExtract)
    t = InformationExtract.find('"live_class_link":"')
    add = 19
    t = t +add

    z = InformationExtract.find('","zoom_password"')

    url = InformationExtract[t:z]
    return url




classDefaultURL = "https://ap.zinedu.com/student/get-live-class-join-status/?status_id="

if len(sys.argv) == 2:
    websiteURLID = sys.argv[1]
else:
    websiteURLID = getURLID()

completeURL = classDefaultURL+websiteURLID

informationExtract = requests.get(completeURL,allow_redirects=True).content

MeetingURL = extractMeetingURL(informationExtract)

print(MeetingURL)

pyperclip.copy(MeetingURL)
