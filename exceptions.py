def main():
    try:
        readfile = open("tennis.txt", "r")
        for line in readfile:
            print(line)
        readfile.close()
    except IOError:
        print("file not found")
    else:
      print("file is readed")




if __name__ == '__main__': main()


