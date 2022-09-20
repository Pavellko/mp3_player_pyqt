z = input()

for i in z:
    if not (i.isalpha() or  i.isalnum()):    
        if i == ' ':
            z = z.replace(i, '-')
        z = z.replace(i, '')
print(z)
