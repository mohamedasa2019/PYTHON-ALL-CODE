








import re
def main():

    readfile=open("tennis.txt","r")  # to read file
    for line in readfile:
        if re.search("(mo|sa-fa)",line):
         print(line)
    readfile.close()








if __name__ == '__main__': main()




