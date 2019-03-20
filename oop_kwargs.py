class car:
    def __init__(self,**kwargs):
        self.data=kwargs

    def getowner(self):
        print("owner name",self.data["name"])
        print("car model",self.data["model"])
        print("year".capitalize(),self.data["year"])
    def set_model(self,model):
        self.data["model"]=model
    def get_model(self):
        print("car model",self.data["model"])

def main():
    mycar=car(name="mohamed".capitalize(),model="mercedes",year="2020")
    mycar.getowner()
    ablacar=car(name="abla",model="bmw",year="2020")
    ablacar.getowner()

    #abla model set
    ablacar.set_model('2021')
    ablacar.get_model()











if __name__ == '__main__': main()
