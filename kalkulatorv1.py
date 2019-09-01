def Penjumlahan():
	clearSceen()
	#MENU
	print("(===)>>>>>>>>>>PROGRAM PENJUMLAHAN<<<<<<<<<<(===)>")
	print("1.Penambahan")
	print("2.Pengurangan")
	print("3.Perkalian")
	print("4.Pembagian")
	print("0.Tutup")
	
	#Pilih Menu
	menu=input("Pilih Nomor :") #Input Nomor Menu
	
	#Cek Menu Pilihan
	if menu==1:
		penambahan()
		elif menu==2:
			pengurangan()
			elif menu==3:
				perkalian()
				elif menu==4:
					pembagian()
					elif menu==0:
						clearScreen()
						print("Bye")
						print("Hacked By BIO00000")
						else:
							print("Menu Tidak Di Temukan")
							display_menu()
							
							def display_menu()
							#Untuk menjeda program raw_input("0,5") 
							#Panggil fungsi Penjumlahan()Penjumlahan()
							
							import os
							def clear screen():
								#Sesuai OS yang dipakai os.system("clear") #linux
								#os.system("cls") #windows
								
								def penambahan():
									clear screen()
									print("(===)>>>>>>>>>>PENAMBAHAN<<<<<<<<<<(===)")
									x = input("Masukan Angka Pertama")
									y = input("Masukan Angka Kedua")
									
									hasil = x + y
									print = "HasilNya Adalah :",hasil
									display_menu()
									
									def pengurangan:()
									clear screen()
									print("(===)>>>>>>>>>>PENGURANGAN<<<<<<<<<<(===)")
									x = input("Masukan Angka Pertama :")
									y = input("Masukan Angka Kedua :")
									hasil = x - y 
									print "Hasilnya  Adalah :",hasil
									
									def perkalian:()
									clear screen()
									x = input("Masukan Angka Pertama :")
									y = input("Masukan Angka Kedua :")
									hasil = x * y 
									print "Hasilnya Adalah :",hasil
									
									def pembagian:()
									clear screen()
									x = input("Masukan Angka Pertama")
									y = input ("Masukan Angka Kedua")
									hasil = x / y
									print "Hasilnya Adalah :",hasil
									
									
									
									
								