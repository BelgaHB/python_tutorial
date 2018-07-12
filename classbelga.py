import self


class person:
    def __init__(self,**kwargs):
        self.data= kwargs

    def getname(self):
    print("name1" ,self.data["name"])

def main():
    myhome=person(name="belga",age=24, work= "student")
    myhome.getname()











if __name__ == '__main__':main()