#membuat struktur data dictionary
userlogin ={"name":"Budi","age":30, "Role":"admin"}
print(type(userlogin));

#mengakses data dalam dictionary
print(f"Nama Akun : {userlogin['name']}")
print(f"Umur : {userlogin['age']} tahun")
print(f"Role : {userlogin['Role']}")

#akses data seluruh
print(userlogin.items())
print(userlogin.keys())
print(userlogin.values())

#menambahkan data baru dalam dictionary
userlogin["email"] = "example@mail.com"
print(userlogin)

#menghapus data big_On dari dictionary
del userlogin["Role"]
print(userlogin)

#mengubah data kedalam dictionari big-O 0(1)
userlogin["Role"] = "user"
print(userlogin)

#nested dictionary
dbUser = {"user1":{"name":"Budi","age":30, "Role":"admin"},
"user2":{"name":"Siti","age":25, "Role":"user"},
"user3":{"name":"Andi","age":35, "Role":"guest"}}

print(dbUser)
#akses value base key
print(dbUser["user1"])

#melakukan pencarian data dalam dictionary
findword =  input("Masukkan Kata yang ingin dicari : ")
if findword in dbUser:
    print("Data ditemukan")
    print(dbUser[findword])
else: 
    print("Data tidak ditemukan")