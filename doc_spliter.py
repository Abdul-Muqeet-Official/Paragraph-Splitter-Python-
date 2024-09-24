path='c:/new folder/notebook.txt'
file=open(path).read()
print(file)

paragraph=file.split("\n\n")

for i , p in enumerate(paragraph):

	address='c:/new folder/muqeet_'+str(i+1)+'.txt'
	with open(address,'w')as file:
		file.write(p)
