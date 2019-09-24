def mukemmelSayilar():
	liste = []

	
	for sayi in range(1,1000):
		toplam = 0

		for i in range(1,sayi): 
			if sayi % i == 0:
				toplam += i
				if sayi == toplam:
					liste.append(sayi)
	return liste


print("1 ile 1000 Arasındaki Mükemmel Sayılar:",mukemmelSayilar())