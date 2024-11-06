# for i in range (0,10,2):
#     print (i)
#     print(f'Perulangan ke-{i}')
#     print('perulangan berkali')

# # part 2
# jumlah = 15






# cara menegecek ganjil genapnya 
# for i in range (0,10):
#     if i % 2 == 0 :
#         print (f'{i}-Bilangan Genap')
#     else :
#         print(f'{i}-Bilangan Ganjil')


# # looping pada bentuk list

# fruits = ['duren','mangga','semangka','apel']

# for i in fruits:
#     print (i)

# untuk menambahakan indeks (nomor buah pada list)
# fruits = ['duren','mangga','semangka','apel']

# for i, buah in enumerate (fruits):
#     print (f'Buah ke-{i}:{buah}')


#data bentuk dictionary dan velues

# biodata = {
#     'nama' : 'almas',
#     'nim'  : '24090092',
#     'kelas': '1C',
#     'umur' :  19
#     }

# for data in biodata:
#     print(data)

# biodata = {
#     'nama' : 'almas',
#     'nim'  : '24090092',
#     'kelas': '1C',
#     'umur' :  19
#     }

# for data in biodata.values():
#     print(data)

#untuk memanggil seluruh data : 
# biodata = {
#     'nama' : 'almas',
#     'nim'  : '24090092',
#     'kelas': '1C',
#     'umur' :  19
#     }

# for label,value in biodata.items():
#     print(f'{label} : {value}')



#BREEAK N CONTINUE
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

for x in range (10):
    if x == 5:
        continue
    print(x)