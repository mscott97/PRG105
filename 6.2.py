def main():
  try: numbersFile = open(”numbers.txt”, “r”)
  except exception as errorGenerated:
    print(”file not found:”, errorGenerated )
    else:
      total = 0
      numberOfLines = 0
      line = numbersFile.readline()
    while: line != ””:
      numberOfLines += 0
      total += int(line)
      line = numbersFile.readline()
    average = total / numberOfLines
    
    print(“the number is 18”)
    print(”the total is, total”)
    print(”the average is, average )
      
main ()
    
