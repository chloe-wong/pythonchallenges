print ("Welcome to the Competency Challenge.")
print("Here is your phrase:'Twisty turns are spelled supercalifragilisticexpialidocious.'")
phrase = str(input("Please (perfectly)input the phrase."))

if phrase == 'Twisty turns are spelled supercalifragilisticexpialidocious.':
    print("good job!")
    repeat = str(input("Please (perfectly)input the phrase again."))
    if phrase == 'Twisty turns are spelled supercalifragilisticexpialidocious.':
        print("Congratulations, you have passed and are now cleared for work.")
    else:
        print("Sorry, you have failed. Please try again.")
else:
    print("Sorry, you are ineligible and unverified")