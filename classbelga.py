class home:
    def __init__(self,name):
        self._name=name
    def getname(self):
        print("name is",self._name)

def main():
    myhome=home("belga")
    myhome.getname()











if __name__ == '__main__':main()