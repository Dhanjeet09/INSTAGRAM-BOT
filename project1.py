from email import message
from time import sleep
from getpass4 import getpass
from instabot import Bot
from os import remove   

my_bot = Bot()

print("---welcome to instabot CLI APPLICATION---")
sleep(2)
print("Setting up the connection with https://www.instagram.com/", end="")
for i in range(3):
    sleep(2)
    print(".", end="")
sleep(2)
print()
print("connection establish")

username = input("username :")
password = getpass('Password : ')
my_bot.login(username=username, password=password)
print("--LOGGED IN SUCCESFULLY--")

while True:
    print("choose suitable option: ")
    print("""1. Follow user\n2. Unfollw user\n3.send message user\n4. post like\n5. Exit the app""")
    print("Enter option you choose: ", end="")
    n = int(input())
    if n == 1:
        user_id = input("username :")
        my_bot.follow(user_id)
    elif n == 2:
        user_id = input("username :")
        my_bot.unfollow(user_id)
    elif n == 3:
        user = input("Enter username: ")
        message = input("message you want to send: ")
        my_bot.send_message(message, user)
        print(f"--MESSAGE SUCCESFULLLY SENT TO {user}")
    elif n==4:
        user_id = input("username :")
        my_bot.download_photos(user_id)
        pass
    elif n == 5:
        my_bot.logout()
    print("Logging out the user", end="")
    for i in range(3):
        sleep(1)
        print(".", end="")
        print()
        sleep(2)
        print("Connection ended !")
        print("logged out successfully!")
        break
    else:
        print("Wrong Input Choose again")
remove('./confg')
