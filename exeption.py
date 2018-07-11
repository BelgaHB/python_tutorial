def main():


    try:

        rf=open("t1.text","r")
        for line in rf:
            print(line)
    except IOError :
        print("not found")
    else:
        print("\n    file is here")










if __name__ == '__main__':main()