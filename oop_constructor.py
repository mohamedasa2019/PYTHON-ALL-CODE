
class car:
    def __init__(self,Name):
        self._Name=Name


    def getowner(self):
        print("owner is",self._Name)


def main():
    mycar=car("mohamed")
    mycar.getowner()









if __name__ == '__main__': main()
