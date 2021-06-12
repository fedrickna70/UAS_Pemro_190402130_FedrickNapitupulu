# Nama  : Fedrick Napitupulu
# Nim   : 190402130
# Ujian Akhir Semester Pemrograman Komputer TE-D

# section 1 : Membuat dengan hasil print ('str', 'float', 'int')
x = "Wortel"
y = 4.5
z = 12
print(x,y,z)
print(x)
print(y)
print(z)

# section 2 : Menentukan tipe dari hasil print
a = 2.3, 1.2
b = 11 , 60
c = "Teknik", "Elektro"
d = 12.20
e = 5
f = "USU"
g = 10.0
h = 66.99
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# section 3 : Python Number

x,y = 2, 4
y,x = 4, 2
print(x,y)
print(y,x)

# section 4 : Memotong huruf pada kalimat berdasarkan peletakkan huruf
ped = "Mahasiswa USU"
print(ped)
print(ped[::-3])
print(ped[3])
print(ped[3:])
print(ped.upper())
print(ped.lower())
print(ped.replace("S","m"))

# section 5 : Pyhton List
list1 = [2,4,6,8,10,12,14]
print(list1)
data1 = list1[0]
print(data1)
data2 = list1[-2]
print(data2)

# section 6 : Kombinasi python list
Motor = ['Yamaha', 'Honda', 'Suzuki']
print(Motor)
print(type (Motor))
Kendaraan =''.join(Motor)
print(Kendaraan)
print(type (Kendaraan))

# section 7 : Menunjukkan angka berapa kali muncul
Nilai = [10,8,6,7,8,9,9,9,8,10,12,11,9,8,10,6,9]
print(Nilai.count(6))
print(Nilai.count(7))
print(Nilai.count(8))
print(Nilai.count(9))
print(Nilai.count(10))
print(Nilai.count(11))
print(Nilai.count(12))

# section 8 : Membuat kalimat menjadi Besar ataupun Kecil
Jurusan = "Teknik Elektro"
Jurusan2 = "TEKNIK ELEKTRO"
print(Jurusan.lower()) # teknik elektro
print(Jurusan.upper()) # TEKNIK ELEKTRO
print(Jurusan.capitalize()) # Teknik elektro
print(Jurusan2.capitalize()) # Teknik elektro
print(Jurusan2.lower()) # teknik elektro
print(Jurusan2.upper()) # TEKNIK ELEKTRO

# section 9 :
Hari = ['rabu', 'kamis', 'jumat', 'sabtu']
Jadwal = map(str.upper, Hari)
print(list(Jadwal))

# section 10 : Dictionary
Biodata = {"ID":404,
           "Nama": "Fedrick Napitupulu",
           "Pekerjaan":"Mahasiswa",
           "Nim":"190402130"
           "Universitas Sumatera Utara"
            }
print(Biodata)



