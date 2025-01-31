def SecondToTime(N):
	soat = N // 3600
	minut = (N % 3600) // 60
	sekunt = N % 60
	print("Soat:",soat,"minut:",minut,"sekunt:",sekunt)

def Week(M):
	week = ['Dushanba','Seshanba','Chorshanba','Payshanba','Juma','Shanba','Yakshanba']
	return week[M-1]