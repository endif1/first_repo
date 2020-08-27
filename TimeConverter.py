def timeConverter(seconds):

    if seconds > 359999:
        print('Invalid Input')# jika user memasukkan nilai lebih dari 359999, 
    elif float(seconds):
        print('Invalid Input')# bilangan desimal
    elif seconds <0:
        print('Invalid Input')# bilangan negatif
    elif str(seconds): 
        print('Invalid Input')# maupun memasukkan string akan keluar notifikasi. Invalid Input
        
    hours = seconds/3600 #satu jam adalah 3600 detik
    minutes = (seconds-hours*3600) /60 #satu jam adalah 60 menit
    second = (seconds - hours*3600 - minutes*60) #satu menit adalah 60 detik
    print(int(hours),':',int(minutes),':',int(second))
    
             
print(timeConverter(3600)) 