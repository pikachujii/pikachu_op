from telethon.sessions import StringSession

from telethon.sync import TelegramClient

import random

from colorama import Fore, Style, Back

pikachu_op = """
 ______  _____  _    _           ______  _     _  _     _           _____   ______  
(_____ \(_____)| |  / )   /\    / _____)| |   | || |   | |         / ___ \ (_____ \ 
 _____) )  _   | | / /   /  \  | /      | |__ | || |   | |        | |   | | _____) )
|  ____/  | |  | |< <   / /\ \ | |      |  __)| || |   | |        | |   | ||  ____/ 
| |      _| |_ | | \ \ | |__| || \_____ | |   | || |___| | _______| |___| || |      
|_|     (_____)|_|  \_)|______| \______)|_|   |_| \______|(_______)\_____/ |_|      
                                                                                    


 

  






"""

logo = """

"""

bhai_bolte = """

#Legendary PIKACHU ⚡BOT          

Made With Love By PIKACHU ⚡BOT

"""

                                                                                                            

print("")

print(Style.BRIGHT + Fore.MAGENTA + pikachu_op)

print(Style.RESET_ALL)

print(Style.BRIGHT + Fore.BLUE + logo)

print(Style.RESET_ALL)

print(Style.BRIGHT + Fore.CYAN + Back.BLUE + bhai_bolte)

print(Style.RESET_ALL)

print("""Welcome To PIKACHUBOT String Generator By @biharibhaiji""")

print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")

API_HASH = input("API_HASH: ")

while True:

    try:

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:

            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")

            print("")

            session = client.session.save()

            client.send_message(

                "me",

                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @pikachu_userbots For Any Help !",

            )

            print(

                "Thanks for Choosing PIKACHUBOT Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"

            )

    except:

        print("")

        print(

            "Wrong phone number \n make sure its with correct country code. Example : +919811099992 ! Kindly Retry"

        )

        print("")

        continue

    break

