def normal(hs1,hs2): # Bo sung do dai hs1 theo kich thuoc hs2

	hsan = []	# Tao list moi
	for ele in hs1:
		tem = []
		tem = [ele]*sum(hs2)
		hsan.extend(tem)
	#print(hsan)
	return hsan

def extenda(hs1,hs2): # Keo dai hai list de co chung do dai
	hsan = normal(hs1,hs2)
	hsbn = normal(hs2,hs1)

	return hsan, hsbn




