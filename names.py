def get_names(file_name):
    list=[]
    f=open(file_name,'r')
    for line in f:
        list.append(line.rstrip('\n'))
    return list

def main():
    girl_names=get_names('GirlNames.txt')
    boy_names=get_names('BoyNames.txt')

    search=input("Enter a boy's or girl's name: ")
    found=0
    if search in girl_names:
        found=1
        print(search, "is the most popular girl's name")
    if search in boy_names:
        found=1
        print(search, "is the most popular boy's name")
    if found==0:
        print('Name not found')

main()

        
