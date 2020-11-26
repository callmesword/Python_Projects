import time
#function to check if the year is leap or not
def check_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
    
#output screen
print("Enter a year and check if its leap or not.\n(enter 0 to exit the program)")
#user choice
try:
    user = int(input("===> "))
except:
    print("invalid number! enter a valid one.")
    user = int(input("===> "))
while True:
    if user == 0:
        print("Closing....")
        time.sleep(1)
        break
    else:
        check_leap_year(user)
        try:
            user = int(input("===> "))
        except:
            print("invalid number! enter a valid one.")
            user = int(input("===> "))
