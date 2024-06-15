import webbrowser
import os
import time
import pyautogui


os.system("cls")
passw = pyautogui.password(
    text='Enter your password',
    title='User Access',
    mask='*')
print("Your password is "+ passw)
print("\n ______   __  __     ______     ______     ______     ______     ______     __  __    \n/\  == \ /\ \_\ \   /\  ___\   /\  ___\   /\  __ \   /\  == \   /\  ___\   /\ \_\ \  \n\ \  _-/ \ \____ \  \ \___  \  \ \  __\   \ \  __ \  \ \  __<   \ \ \____  \ \  __ \  \n \ \_\    \/\_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ \n  \/_/     \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/   \/_____/   \/_/\/_/ \n")
print("1.Search")
print("2.Html Scraping")
print("3.Update")
mode = input("Choose the mode of PySearch : ")
if mode == "1":
    type = input("Choose the extension of websites (.com, .org, .fr, .eu...) > ")
    if type == ".com":
        os.system("cls")
        print("\n ______   __  __     ______     ______     ______     ______     ______     __  __    \n/\  == \ /\ \_\ \   /\  ___\   /\  ___\   /\  __ \   /\  == \   /\  ___\   /\ \_\ \  \n\ \  _-/ \ \____ \  \ \___  \  \ \  __\   \ \  __ \  \ \  __<   \ \ \____  \ \  __ \  \n \ \_\    \/\_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ \n  \/_/     \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/   \/_____/   \/_/\/_/ \n")
        print("Extension : "+ type)
        while True:
            search = input("SEARCH > ")
            if search == "help":
                os.system("start WebSite/PySearch.html")

            webbrowser.open_new(search +".com")
    else:
        os.system("cls")
        print("\n ______   __  __     ______     ______     ______     ______     ______     __  __    \n/\  == \ /\ \_\ \   /\  ___\   /\  ___\   /\  __ \   /\  == \   /\  ___\   /\ \_\ \  \n\ \  _-/ \ \____ \  \ \___  \  \ \  __\   \ \  __ \  \ \  __<   \ \ \____  \ \  __ \  \n \ \_\    \/\_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ \n  \/_/     \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/   \/_____/   \/_/\/_/ \n")
        print("Extension : "+ type)
        while True:
            search = input("SEARCH > ")

            if search == "help":
                os.system("start PySearch.html")

            
            webbrowser.open_new(search + type)
if mode == "2":
    import requests
    import bs4
    search = input("Enter the web site url : ")

    site = requests.get(search)

    html = bs4.BeautifulSoup(site.content, "html.parser")

    import os
    os.system("cls")
    print(search , ":", "\n","\n", html)

if mode == "3":
    import time
    import os
    import pyautogui

    os.system("cls")
    choice = input("Do you want update PySearch (Y/n) : ")
    if choice == "Y":
        print("Install packages...")
        time.sleep(1)
        print("Install modules...")
        time.sleep(1)
        os.system("cls")
        print("10% -")
        time.sleep(1)
        os.system("cls")
        print("20% --")
        time.sleep(1)
        os.system("cls")
        print("30% ---")
        time.sleep(1)
        os.system("cls")
        print("40% ----")
        time.sleep(1)
        os.system("cls")
        print("50% -----")
        time.sleep(1)
        os.system("cls")
        print("60% ------")
        time.sleep(1)
        os.system("cls")
        print("70% -------")
        time.sleep(1)
        os.system("cls")
        print("80% --------")
        time.sleep(1)
        os.system("cls")
        print("90% ---------")
        time.sleep(1)
        os.system("cls")
        print("100% ----------")
        print("\nPySearch v1.2 installed")
        update = open("Logs.txt", "a+")
        update.write("-Version : 1.2\n-Tools : PySearch\n-Requires : Python 3.12, Windows 10, x64 and x32\n-Help : come to WebSite/PySearch.html for help")
        input("")
        