import random
import pyperclip
# Dictionary For Web Passwords

webpasswords = {

}
    # Ask user for Website

web = input("What website is this password is for?")

    # Create Passwords
letters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*():';.,/><]}{[-_=+`~ABCDEFGHIJKLOMNOPQRSTUVWXYZ"

random_letters = ""
for i in range(12):
    random_letters += random.choice(letters)

#     # Add to dictionary

webpasswords[web] = random_letters

#     # pyperclip

pyperclip.copy(random_letters)

    #Print out statements

print(f"Here is your password for {web}: {random_letters}")
print("Your password has been copied to clipboard!")

#Print Dictionary
print("All passwords: ")
for name, number in webpasswords.items():
    print(f"{web}: {random_letters}")

#     Input for another Password
answer = input("Enter another password? (y/n):")
while answer == "y":

    web2 = input("What website is this password is for?")

    # Create Passwords
    letters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*():';.,/><]}{[-_=+`~ABCDEFGHIJKLOMNOPQRSTUVWXYZ"

    random_letters2 = ""
    for i in range(12):
        random_letters += random.choice(letters)

    # Add to dictionary

    webpasswords[web2] = random_letters

    # Pyperclip

    pyperclip.copy(random_letters)

    #Print out statements

    print(f"Here is your password for {web2}: {random_letters}")
    print("Your password has been copied to clipboard!")

    #Print Dictionary
    print("All passwords: ")
    for name, number in webpasswords.items():
        print(f"{web}" or f"{web2} : {random_letters}")

    #     Input for another Password
    answer = input("Enter another password? (y/n):")