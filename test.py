# https://live.zinedu.com/?id=303487
def getURLIDCheck():
    text = "https://live.zinedu.com/?id=303487"
    result = 0
    if len(text) <= 6:
        return text
    else:
        idPreSlice = text.find("?id=")
        idSlice = idPreSlice + 4

        result = text[idSlice:(len(text))] 
        print(result)
    
    return result



getURLIDCheck()