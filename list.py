def main():
    list_number=[]
    total=0
    for number in range (20):
        number=float(input('Enter the number '+format(number+1)+': '))
        list_number.append(number)
        total+=number
        average=total/len(list_number)

    print('The lowest number in the list',min(list_number))
    print('The highest number in the list',max(list_number))
    print('The total of the numbers in the list', format(total,',.2f'))
    print('The average of the numbers in the list',format(average,',.2f'))

main()

    
        
