import numpy as np

def quydong(l1,l2): # Quy dong hai list
	l1_n = [ele*sum(l2) for ele in l1]
	l2_n = [ele*sum(l1) for ele in l2]
	return l1_n, l2_n

def dienso(start,end,value,lista): # Dien so cho list dua vao index dau va cuoi
	i = start + 1
	while i <= end:
		lista[i] = value
		i += 1
	return lista

def dausis(l1,l2): # Tim list phan tich cua 2 list
	hs1,hs2 = quydong(l1,l2)

	dau1_index = len(hs1)-1
	dau2_index = len(hs2)-1
	#print(dau1_index,dau2_index)

	dau1_value = hs1[dau1_index]
	dau2_value = hs2[dau2_index]

	#print(dau1_value,dau2_value)

	rs = np.array([0]*(len(l1)+len(l2)))

	while dau1_index >= 0 and dau2_index >= 0:
		#print(dau1_index,dau2_index)

		tem = [0]*(len(hs1)+len(hs2))
		if dau1_value > dau2_value:
			tem = dienso(dau1_index,len(l1)+dau2_index,dau2_value,tem)
			#print(f'0: {tem}')
			dau2_index = dau2_index - 1

			dau1_value = dau1_value - dau2_value
			dau2_value = hs2[dau2_index]

		elif dau1_value < dau2_value:
			#print(dau1_index,len(l1)+dau2_index-1,dau1_value)
			tem = dienso(dau1_index,len(l1)+dau2_index,dau1_value,tem)
			#print(f'1: {tem}')
			dau1_index = dau1_index - 1

			dau2_value = dau2_value - dau1_value
			dau1_value = hs1[dau1_index]

		else:
			tem = dienso(dau1_index,len(l1)+dau2_index,dau1_value,tem)
			#print(f'2: {tem}')
			dau1_index = dau1_index - 1
			dau2_index = dau2_index - 1

			dau1_value = hs1[dau1_index]
			dau2_value = hs2[dau2_index]

		rs += np.array(tem)

		#print(dau1_index,dau2_index)
	return rs.tolist()[1:] 






