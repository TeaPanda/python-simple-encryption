import random

key = random.randint(1,50)
result = ""
choice = ""
message = ""


while True:
	try:
		pastkey = str(input("Is there any masterkey you want to use, leave empty for random masterkey\n"))
		if str(pastkey) == "":
			break
		elif float(pastkey) != round(float(pastkey)):
			print("The masterkey is always a whole number")
			continue
		else:
			break
	except ValueError as e:
		print("Only numbers please")
		continue

while True:
    try:
        if (float(pastkey) < 11) or (float(pastkey) > 60):
            print("Liar, we don't have any masterkey like that, we will be chosing a random one for you\n")
            break
        elif pastkey == "":
            pastkey = key + 10
            break
        else:
            key = int(pastkey) - 10
            break
    except ValueError as e:
        break


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
