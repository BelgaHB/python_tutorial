import datetime
def main():
    d1=input("دخل عمرك")
    dn=datetime.datetime.now().year

    y1=dn-int(d1)
    print("yor age is {}".format(y1))




if __name__ == '__main__':main()
