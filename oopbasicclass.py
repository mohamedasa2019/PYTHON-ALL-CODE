
class car:
    def getowner(self):
         print("owner is",self._name)
    def setowner(self,name):
        self._name=name



def main():
    mycar=car()
    mycar.setowner("zefta")
    mycar.getowner()







if __name__ == '__main__': main()
