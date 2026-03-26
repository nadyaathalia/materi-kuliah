#membuat struktur data dictionary
userlogin ={"name":"Nadya cakep banget","age":23, "Role":"penguasa dunia"}
print(type(userlogin));

#mengakses data dalam dictionary
print(f"Nama Akun : {userlogin['name']}")
print(f"Umur Akun : {userlogin['age']} tahun")
print(f"Role Akun : {userlogin['Role']}")

#akses data seluruh
print(userlogin.items())
print(userlogin.keys())
print(userlogin.values())

#menambahkan data baru dalam dictionary
userlogin["email"] = "nadyacakep@gmail.com"
print(userlogin)

#menghapus data big_On dari dictionary
userlogin.pop("email")
print(userlogin)

#mengubah data kedalam dictionari big-O 0(1)
userlogin["name"] = "user"
print(userlogin)

#nested dictionary
dbUser = {"user1":{"name":"Nadya","age":23, "Role":"ratu-atlantis"},
"user2":{"name":"Linda","age":25, "Role":"anak baik"},
"user3":{"name":"Rully","age":35, "Role":"anak jahat"}}

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