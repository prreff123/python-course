yearAge = int(input("What is your Age/year of birth\n"))

if yearAge<125:
    isAge = True

elif(yearAge>1900):
    isyear = True

else:
    print("There was some problem with your age/year of birth")
    exit()

if isAge:
    yearAge = 2022 - yearAge

print(f"You will be 100 years old in {yearAge}")            