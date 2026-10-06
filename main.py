import random
import pyperclip
# Dictionary For Web Passwords

webpasswords = {

}
    # Ask user for Website

web = input("What website is this password is for? ")

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
print(" ")
print(f"Here is your password for {web}: {random_letters}")
print("Your password has been copied to clipboard!")

#Print Dictionary
print(" ")
print("All passwords: ")
for web, random_letters in webpasswords.items():
    print(f"{web} : {random_letters}")

#     Input for another Password
print(" ")
answer = input("Enter another password? (y/n):")
while answer == "y":

    web = input("What website is this password is for? ")

    # Create Passwords
    letters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*():';.,/><]}{[-_=+`~ABCDEFGHIJKLOMNOPQRSTUVWXYZ"

    random_letters = ""
    for i in range(12):
        random_letters += random.choice(letters)

    # Add to dictionary

    webpasswords[web] = random_letters

    # Pyperclip

    pyperclip.copy(random_letters)

    #Print out statements
    print(" ")
    print(f"Here is your password for {web}: {random_letters}")
    print("Your password has been copied to clipboard!")

    #Print Dictionary
    print(" ")
    print("All passwords: ")
    for web, number in webpasswords.items():
        print(f"{web} : {random_letters}")
    #     Input for another Password
    answer = input("Enter another password? (y/n):")
print("Thank you for trusting us.")