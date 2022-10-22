#This proggo outputs a list of values into a file


your_list = '1234567890-'
intCharactersNeeded = 5 #How many characters does each variable need to be?
#heads up if the number is too high it might crash lol
TempStorageFile = "Temp.txt"
FormattedOutput = "GeneratedList.txt"
openFile = open(TempStorageFile, "w")
complete_list = []
for current in range(intCharactersNeeded):
    a = [i for i in your_list]
    for y in range(current):
        a = [x+i for i in your_list for x in a]
#        print(a)
    complete_list = complete_list+a
print(complete_list)

#pause = input()


# replace the == with <= if lenght of variable inserted could be less than 5 characters
for item1 in complete_list:
	if len(item1) == intCharactersNeeded: openFile.write(item1 + "\n")
list1 = []



with open(TempStorageFile) as openFile:
	for line in openFile:
		list1.append(line.replace("\n",""))
intCounter1 = 0
openFile = open(FormattedOutput, "w")
for item1 in list1:
	intCounter1 += 1
	#for this example we are generating a list of ISBNs with a potential for a typo (thus accounting for -)
	openFile.write("ISBN: 978-1-"+ str(item1)+"-928-8\n")
	print(str(intCounter1) + "\n")
print(list2[0])
