

# creating a memory lst
myList = [chr(chNum) for chNum in list(range(ord('a'), ord('z')+1))]
print(myList)

# now let us have cipher word, cipher = lcem , word = jack
cipher = 'lcem'
cipher_lst = list(cipher)
print(cipher_lst)

# cipher key is l = j
cipher_key = 'j'
print('cipher key is %s = %s'%(cipher_lst[0],cipher_key))

# substituting j in place of l
print(cipher.replace(cipher_lst[0],cipher_key[0]))

# storing l=j in memory

memo1 = [cipher_lst[0],cipher_key]

print(memo1)

#now lets us verify the key with the mylist

for element1 in myList:
    if memo1[0]==element1 :
        print('%s = %s'%(memo1[0],cipher_key))

# as this works let take an input from the user now...
usr_input = input('enter the key value = ')
for element in memo1[0]:
    if usr_input==element:
        print('user input %s exists in the memory '%(element))
    else :
        print('user input does not exists in the memory.')