def main():
    try:
        number_file = open("numbers.txt", "r")
    except Exception as errorGenerated:
        print("file is not found:", errorGenerated)
    else:
        total = 0
        number_of_lines = 0
        line = number_file.readline()

        while line != "":
            number_of_lines += 1
            total += int(line)
            line = total / number_of_lines
            print("The average is",)


main()
