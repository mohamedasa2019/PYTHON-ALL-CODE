def main():
    out=open("tennis.txt","a")  # "w" write   .  "a" append اضافه
    out.write("welcom in python file\n mohamed\n name:moustafa")
    out.close()
    readfile=open("tennis.txt","r")  # to read file
    for line in readfile:
        print(line)




















if __name__ == '__main__': main()
