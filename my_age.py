import datetime
def main():
    DOB=input("ENTER YOUR DOB:")
    yearnow=datetime.datetime.now().year
    Myage=yearnow - int(DOB)
    print("Your age is {} year".format(Myage))












if __name__ == '__main__': main()
