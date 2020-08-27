def urai(x):
    a = ''
    if len(x)==4: #jika huruf sama dengan 4
        print((x[0]*2)+x[1]+x[0]+x[1]+x[2]+x[2]+x[0:],end='')
    elif len(x)==5: #jika huruf sama dengan 5
        print((x[0]*2)+x[1]+x[0]+x[1]+x[2]+x[2]+x[1])
    elif len(x)>5: #jika huruf lebih dari 5
        print((x[0]*2)+x[1]+x[0]+x[1]+(x[2]*2+x[3]+x[5]))


print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

# Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika