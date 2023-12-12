rating = int(input("Enter your rating from 1-5 : "))

if rating==1:
    print("Horrible!")
elif rating==2:
    print("Very Poor")
elif rating==3:
    print("Poor")
elif rating==4:
    print("Okay")
elif rating==5:
    print("Excellent!")
else:
    print("Error!" ,rating, "is not between 1 and 5")