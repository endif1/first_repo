data =[[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
# [[3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]]
def data_mutar(x):
    y = x[1][2] #data y diisi dengan data index 0
    z = x[0][2] #data z diisi dengan data index 1
    a = x[2][2] #data a diisi dengan data index 2
    x[0][2] = a #setelah itu set data pada index 0 menjadi data z
    x[0][0] = z #setelah itu set data pada index 0 menjadi data y
    x[0][1] = y #setelah itu set data pada index 0 menjadi data a
    b = x[0][::1] # setelah itu data a diisi dengan data index 0 yang sudah dibalik
    c = x[1][::-1] # dan juga isi data b dengan data index 1 yang sudah dibalik 
    d = x[2][::-1]
    return [b,c,d] # simpan nilai a dan b bracket
print(data_mutar(data))