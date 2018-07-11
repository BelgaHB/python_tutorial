def main():

    A=open("t1.text","w")
    A.write("go to hell A \n "
            "you are not well came here")
    A.close()

    ## I added a comment
    rf=open("t1.text","r")
    for line in rf:
        print(line)









if __name__ == '__main__':main()