Def ReadGirlnamesFromFile(Filename):
GirlsNameFile = open(filename, “r”) 
GirlnamesList = []

Girlname = girlsnamesfile.readline()

While Girlname != “”:
Girlname = Girlname.rstrip(“/n”)
GirlnameList.append(girlname)
Girlname = girlNamesFile.readline()

Return Girlsnamelist

Def ReadBoynamesFromFile(Filename):
BoyNameFile = open(filename, “r”) 
BoynamesList = []

BoyName = boysnamesfile.readline()

While Boyname != “”:
Boyname = boyname.rstrip(“/n”)
BoynameList.append(Boyname)
Boyname = boyNamesFile.readline()

Return Boynamelist

Def getUserSearchNames:

UserSearchName = input(“Please enter a first name”)
UserSearchNameList = []

While UserSearchName != “-1”:
UserSearchNameList.append(UserSearchName)
UserSearchName = input (“Please enter the next name to” +\ “search for or -1 to continue:” 

Return UserSearchNameList





