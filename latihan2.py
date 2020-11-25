import os

try:
    file= input("Masukkan nama File anda:")
    if os.path.exists(file):
        mode= 'a'
    else:
        mode='r'

    isifile= open(file,mode)

    lanjut= True
    while(lanjut==True):
        data= input ('Data yang akan ditambahkan:')
        isifile.write('\n'+ data)
        opsi=input('Mau lagi?(y/n):')
        if(opsi=='y'):
            lanjut=True
        elif(opsi=='n'):
            lanjut=False
        else:
            print('Inputan Invalid')
            break

    isifile.close()
except FileNotFoundError:
    print('File Tidak Terdeteksi')
