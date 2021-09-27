users = ['ali', 'assaf', 'muhammed']

# Method 1
print(users[0]+','+users[1]+','+users[2])

# Method 2
for i in range(len(users)):

  if i != len(users)-1:
  
    print(users[i]+',', end='')
    
  else:print(users[i])

# Method 3
delimeter = ','
print(delimeter.join(users))
