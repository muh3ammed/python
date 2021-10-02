def gen(end):
  
    current = 0
    
    while current < end:

        yield current
        current += 1

for i in gen(5):print(i)
