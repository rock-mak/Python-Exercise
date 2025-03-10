file = open('Training_01.txt','r')
content = file.readlines()
category = set()
for line in content:
    category.add(line.split("/")[2])
category = ", ".join(category)

print("Category as follow: \n", category)
print("There are %s categories in the image content" %(len(category)+1))
