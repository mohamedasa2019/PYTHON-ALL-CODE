class operation:
    def sum(self,n1,n2):
        sumresult=n1+n2
        print("sum=",sumresult)
    def sub(self,n1,n2):
        subresult=n1-n2
        print("sub=",subresult)
class operationwithmul(operation):
    def mul(self,n1,n2):
        mulresult=n1*n2
        print("mul=",mulresult)

    def sub(self,n1,n2):
        subresult=n1-n2+5
        super().sub(n1,n2)
        print("sub=",subresult)






def main():

    opmul=operationwithmul()
    opmul.mul(2,10)
    opmul.sub(4,2)
    opmul.sum(10,9)


if __name__ == '__main__': main()
