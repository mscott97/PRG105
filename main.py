def main():
    namesflie = open("names.txt", "r")

    line = namesflie.readline()

    while line != "":
        print(line.rstrip("\n"))
        line = namesflie.readline()


main()
