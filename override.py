class op:
    def sum(self,n1,n2):
        z=n1+n2
        print("sum =",z)
class oowm (op):
    def mul(self,n1,n2):
        z=n1*n2
        print("mull =",z)


def main():
    o=oowm()
    o.sum(5,8)



if __name__ == '__main__':main()

