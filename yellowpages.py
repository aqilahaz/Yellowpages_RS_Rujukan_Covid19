#Created by Aqilah Aini Zahra
#20 Februari 2022

listRumahSakit = [{
    'ID': '1A',
    'Provinsi' : 'Sumatera Selatan',
    'Nama' : 'RSU Lubuk Linggau',
    'Alamat': 'Jl. Yos Sudarso Lubuk Linggau',
    'No. Telepon': '(0733) 321013'
},
{
    'ID': '2A',
    'Provinsi' : 'Sumatera Selatan',
    'Nama' : 'RSU Kayu Agung',
    'Alamat': 'Jl. Raya Lintas Timur Kec. Kota Kayuagung',
    'No. Telepon': '(0712) 323889'
},
{
    'ID': '3A',
    'Provinsi' : 'Sumatera Selatan',
    'Nama' : 'RSUD Kabupaten Lahat',
    'Alamat': 'Jl. Mayor Ruslan I No. 28, Lahat',
    'No. Telepon': '(0731) 321785'
},
{
    'ID': '1B',
    'Provinsi' : 'Sumatera Barat',
    'Nama' : 'RSU Dr. M. Jamil Padang',
    'Alamat': 'Jl. Perintis Kemerdekaan, Padang',
    'No. Telepon': '(0751) 32372'
},
{
    'ID': '2B',
    'Provinsi' : 'Sumatera Barat',
    'Nama' : 'RSUD Dr. Achmad Mochtar',
    'Alamat': 'Jl. Dr A Rivai Bukittinggi',
    'No. Telepon': '(0752) 21720'
}]

def read_data():
    """Fitur Read Data berfungsi untuk menampilkan seluruh data kontak rumah sakit Rujukan Covid 19 Wilayah Sumatera Selatan
    dan Sumatera Barat. Pada fungsi ini kita dapat menampilkan seluruh data ataupun data tertentu berdasarkan dengan ID"""
    while True:
        menu_read = input('''
===== Data Kontak Telepon Rumah Sakit ====="
1. Kontak Telepon Seluruh Data
2. Kontak Telepon Data Tertentu
3. Kembali Ke Menu Utama

Silakan Pilih Sub Menu Menampilkan Data [1-3]: ''')
    
        if (menu_read == '1') :
            if len(listRumahSakit) !=0:
                print('Daftar Rumah Sakit Rujukan\n')
                for i in range(len(listRumahSakit)):
                    print('{}. ID: {}, Provinsi: {}, Nama: {}, Alamat: {}, No.Telepon: {} '.format(
                        i+1, listRumahSakit[i]['ID'], listRumahSakit[i]['Provinsi'], listRumahSakit[i]['Nama'],listRumahSakit[i]['Alamat'],listRumahSakit[i]['No. Telepon']))
            else:
                print("\n*****Tidak Ada Kontak Telepon Rumah Sakit Rujukan COVID-19*****")
        elif (menu_read == '2'):
            if len(listRumahSakit) !=0:
                id = input("Masukkan ID :").upper()
                print(f"Data siswa dengan ID: {id}")
                for index, i in enumerate(listRumahSakit):
                    if i['ID'] == id:
                        print(f"{index+1}, ID: {i['ID']}, Provinsi: {i['Provinsi']}, Nama: {i['Nama']}, Alamat: {i['Alamat']}, No. Telepon: {i['No. Telepon']} ")
                        break
                else:
                    print("*****Tidak ada data dengan ID tersebut*****")
            else:
                print("\n*****Tidak Ada Kontak Telepon Rumah Sakit Rujukan COVID-19*****") 
        elif(menu_read =='3'):
            break
        else:
            print('*****Menu Tidak Terdaftar*****')

def create_data():
    """Fitur Create Data berfungsi untuk Menambah Data Kotak Telepon Rumah sakit Rujukan Covid 19 Wilayah Sumatera Selatan
    dan Sumatera Barat. Pada fungsi ini user dapat menambah data Kontak Telepon  """
    while True:
        menu_create = input('''
===== Menambah Data Kontak Telepon Rumah Sakit ====="
1. Tambah Data Kontak Telepon Rumah Sakit
2. Kembali ke Menu Utama

Silakan Pilih Sub Menu Menambah Data [1-2]: ''')

        if(menu_create == '1'):
            id_create = input("Masukkan ID :").upper()
            for index, i in enumerate(listRumahSakit):
                if i['ID'] == id_create:
                    print("*****Data sudah ada*****")
                    break
            else:
                prov_rs = input("Masukkan nama Provinsi: ")
                nama_rs = input("Masukkan nama Rumah Sakit: ")
                alamat_rs = input("Masukkan alamat Rumah Sakit: ")
                telp_rs = input("Masukkan Nomor Telepon Rumah Sakit: ")
                while True:
                    yes_or_no = input("Apakah data akan disimpan (Y/N)? ").upper()
                    if yes_or_no == 'Y':
                        listRumahSakit.append({
                            'ID': id_create,
                            'Provinsi' : prov_rs,
                            'Nama': nama_rs,
                            'Alamat': alamat_rs,
                            'No. Telepon': telp_rs
                        })
                        print("*****Data Tersimpan*****")
                        break
                    elif yes_or_no == 'N':
                        break                    
        elif(menu_create =='2'):
            break 
        else:
            print('*****Menu Tidak Terdaftar*****')

def update_data():
    """Fitur Update Data berfungsi untuk melakukan update Data Kotak Telepon Rumah sakit Rujukan Covid 19 Wilayah Sumatera Selatan
    dan Sumatera Barat. Pada fungsi ini user dapat mengubah data Kontak Telepon  """
    while True:
        menu_update = input('''
===== Mengubah Data Kontak Telepon Rumah Sakit ====="
1. Ubah Data Kontak Telepon Rumah Sakit
2. Kembali ke Menu Utama

Silakan Pilih Sub Menu Ubah Data [1-2]: ''')
        if(menu_update == '1'):
            if len(listRumahSakit) !=0:
                id = input("Masukkan ID :").upper()
                for index, i in enumerate(listRumahSakit):
                    if i['ID'] == id:
                        print(f"ID: {i['ID']}, Provinsi: {i['Provinsi']}, Nama: {i['Nama']}, Alamat: {i['Alamat']}, No. Telepon: {i['No. Telepon']} ")
                        _flag = True
                        while _flag:
                            y_or_n = input("Tekan Y jika ingin lanjut update data atau N jika ingin cancel update: ").upper()
                            if y_or_n == 'N':
                                print("Data Tidak Terupdate")
                                break
                            elif y_or_n =='Y':
                                ket = input("Masukkan kolom keterangan yang akan diupdate: ").title()
                                ket2 = input(f"Masukkan {ket} baru: ")
                                while True:
                                    update = input("Apakah data akan diupdate (Y/N)?").upper()
                                    if update == 'Y':
                                        data_baru = {ket:ket2}
                                        i.update(data_baru)
                                        print("*****Data Updated*****")
                                        _flag = False
                                        break
                                    elif update == 'N':
                                        print("*****Data tidak terupdate*****")
                                        _flag=False
                                        break
                        break
                else:
                    print("*****Tidak ada data dengan ID tersebut*****")
            else:
                print("\n*****Tidak Ada Kontak Telepon Rumah Sakit Rujukan COVID-19*****")
        elif (menu_update =='2'):
            break

def delete_data():
    """Fitur Delete Data berfungsi untuk Menghapus Data Kotak Telepon Rumah sakit Rujukan Covid 19 Wilayah Sumatera Selatan
    dan Sumatera Barat. Pada fungsi ini user dapat menghapus data Kontak Telepon  """
    while True:
        menu_delete = input('''
===== Menghapus Data Kontak Telepon Rumah Sakit ====="
1. Hapus Kontak Telepon Rumah Sakit
2. Kembali ke Menu Utama

Silakan Pilih Sub Menu Hapus Data [1-2]: ''')

        if (menu_delete == '1'):
            if len(listRumahSakit) !=0:
                id_delete = input("Masukkan ID: ").upper()
                for index, i in enumerate(listRumahSakit):
                    if i['ID'] == id_delete:
                        _flag = True
                        while _flag:
                            hapus_data = input("Apakah data akan dihapus? (Y/N)").upper()
                            if hapus_data == 'N':
                                print("*****Data Tidak Terhapus****\n")
                                break
                            elif hapus_data == 'Y':
                                if listRumahSakit[index]['ID'] == id_delete:
                                    del listRumahSakit[index]
                                    print("*****Data Deleted*****")
                                    break
                        break
                else:
                    print("*****Tidak ada data dengan ID tersebut*****")
            else:
                print("\n*****Tidak Ada Kontak Telepon Rumah Sakit Rujukan COVID-19*****")
        elif (menu_delete == '2'):
            break

def MainMenu():
    while True:
        pilihanMenu = input('''
========================================================================================================
Selamat Datang di Buku Telepon Rumah Sakit Rujukan COVID-19 Provinsi Sumatera Selatan dan Sumatera Barat

List Menu :
1. Menampilkan Buku Telepon Rumah Sakit Rujukan
2. Menambahkan Data Telepon Rumah Sakit Rujukan
3. Mengubah Data Telepon Rumah Sakit Rujukan
4. Menghapus Data Telepon Rumah Sakit Rujukan
5. Exit

========================================================================================================

Silakan Pilih Menu [1-5] : ''')

        if(pilihanMenu =='1'):
            read_data()
        elif(pilihanMenu =='2'):
            create_data()
        elif(pilihanMenu =='3'):
            update_data()
        elif(pilihanMenu =='4'):
            delete_data()
        elif(pilihanMenu =='5'):
            print("Thank you and Good Bye!!!")
            break
        else:
            print("*****Pilihan yang Anda masukkan salah*****")
            
MainMenu()