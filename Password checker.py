test = "james"


#print(first_char.isupper())

#isLower()

print(test.find("a") )
#Return the index if it finds it



# Step 1:
# Prompt the user to enter their password
# Check the following:
# - If the password contains the letter z
# - If the password ends with an !
# - If the password begins with any uppercase letter
# If yes to all three, print "Accepted!"
# If any of these are not true, print "Rejected!"
password = input("Enter your password pls")

first_char = password[0]
print(first_char.isupper())
if password.find("z"):
    
    if first_char.isupper():
    
        if password.find("!"):
           print("Accepted!")
    
else:
    print("Rejected!")