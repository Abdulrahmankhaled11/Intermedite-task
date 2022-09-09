
Names =['mahmoud','farida','ali','hassan','mohamed','khaled','taha']



# *** Transform all names to uppercase

#using normal list :

New_names =[]

for name in Names :
    New_names.append(name.upper())
print(New_names)

#using functional programming :

def upper(name):
    return name.upper()

New_names1 = map(upper,Names)
print(list(New_names1))


#using list comprehension :

New_names2 =[name.upper()for name in Names]
print(New_names2)


#Get the names that contains ‘a’ in a list


#using normal list :
contain_a =[]
for name in Names :
    if 'a' in name :
        contain_a.append(name)
print(contain_a)


#using functional programming :

def contain(name):
    if 'a' in name:
        return True
    else:
        return False


contain_a1 = filter(contain,Names)
print(list(contain_a1))

#using list comprehension :

contain_a2 =[name for name in Names if 'a' in name]
print(contain_a2)


# Get the names that starts with ‘t’ in a list

#using normal list :

contain_t =[]
for name in Names :
    if name[0]=='t':
        contain_t.append(name)
print(contain_t)



#using functional programming :

def containt(name):
     if name[0]=='t':
         return True
     else:
         return False
contain_t1 = filter(containt,Names)
print(list(contain_t1))


#using list comprehension :

contain_t2 =[name for name in Names if name[0]=='t']
print(contain_t2)


#Get the names that contains 2 or more ‘a’ letter

#using normal list :

contain2_a =[]
for name in Names :
    if name.count('a')>=2:
        contain2_a.append(name)
print(contain2_a)      



#using functional programming :

def check_2a(name):
    if name.count('a')>=2 :
        return True
    else:
        return False

contain2_a1 =filter(check_2a,Names)
print(list(contain2_a1))



#using list comprehension :


contain2_a2 =[name for name in Names if name.count('a')>=2]
print(contain2_a2)


# Unpack the list in
Numbers =[1,2,3,4,5,6,7,8]

# a,b , a= the first index , b = rest of the list :
a,*b = Numbers

# a = the first index , b = the last index
a,*_,b =Numbers

# a = the first index , b = the second index
 a,b,*_ =Numbers












        
        
