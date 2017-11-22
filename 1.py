import random

key = random.randint(1,50)
result = ""
choice = ""
message = ""

while True:
	pastkey = float(input("Is there any masterkey you want to use, leave empty for random masterkey\n"))
	if pastkey == round(pastkey):
		break
	elif pastkey == "" :
		break
	else:
		print("The masterkey is always a whole number")


if pastkey <11 or pastkey >60 and not pastkey == "":
	print("Liar, we don't have any masterkey like that, we will be chosing a random one for you\n")
elif pastkey == "";
	pastkey = key + 10
else:
	key = pastkey - 10

while choice != "-1":
	choice = input("\n Type 1 to encrypt or 2 to decrypt a message\n")
	if choice == "1":
		message = input("\n Please enter a message to encrypt \n")
		for i in range(0, len(message)):
			result = result + chr(ord(message[i]) - 2*key)

		print (result + '\n\n')
		result = ''

	elif choice == "2":
		message = input("\n Please enter a message to decrypt \n")
		for i in range(0, len(message)):
			result = result + chr(ord(message[i]) + 2*key)

		print (result + "\n\n")
		result = ""

	elif choice != "-1":
		print("Invalid command, please try again")

print("You masterkey was" , str(pastkey), "please take note of it if you want to decrypt your message again!")

print("Press any key to exit")
