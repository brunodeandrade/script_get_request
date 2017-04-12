import requests

hora_inicio = 14
minuto_inicio = 00
segundo_inicio = 00

for k in range(hora_inicio, 23):
	horasString = ""
	if k < 10:
		horasString = "0"+str(k)
	else:
		horasString = str(k)

	for j in range(minuto_inicio,60):
		minutosString = ""
		if j < 10:
			minutosString = "0"+str(j)
		else:
			minutosString = str(j)

		for i in range(segundo_inicio, 60):
			segundosString = ""
			if i < 10:
				segundosString = "0"+str(i)
			else :
				segundosString = str(i)
			print("Hora: "+horasString+minutosString+segundosString+"  ")
			# print("Hora: "+horasString+minutosString+segundosString+"\n")
			url = "https://idecan.s3.amazonaws.com/concursos/259/61_10032017"+horasString+minutosString+segundosString+".pdf"
			r = requests.get(url)
			if r.content[0] != "<":
				print "URL: "+url
				break

