str1 = raw_input().lower().replace(" ","")
list1 = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for item in str1:
    list1.append(item)

count = 0
for item in alpha:
    if item in list1:
        count = 1
    else:
        count = 0
        break
    
if count == 1:
    print "PANGRAM"
else:
    print "NOT PANGRAM"
    
    
#ALTERNATIVE
str1 = raw_input().lower().replace(" ","")
list1 = list(set(str1))
count = 0
for item in list1:
    count += 1
if count == 26:
    print "PANGRAM"
else:
    print "NOT PANGRAM"
