import re
def main():


    rf=open("t1.text","r")
    for line in rf:
            if re.search("hell", line):
                print(line)









if __name__ == '__main__':main()