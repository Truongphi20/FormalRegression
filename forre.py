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

#print(dausis([1],[1,1,1]))

def leng(lista): # khoang cach cac diem
	lengths =[0]*(len(lista)-1)
	for i in range(len(lista)-1):
		lengths[i] = lista[i+1][0]-lista[i][0]
	return lengths

def Reparelib(lista): # Chuan bi thu vien

	lib_vals = {ele[0]:ele[1] for ele in lista}
	#print(lib_vals)

	keys = [key for key in lib_vals]

	for k in range(len(keys)-1):
		lib_vals[keys[len(keys)-1-k]] =  lib_vals[keys[len(keys)-1-k]] - lib_vals[keys[len(keys)-2-k]]
	lib_vals.pop(keys[0])
	#print(lib_vals)

	lengths = leng(lista)	# Do dai
	#print(lengths)

	new_keys = keys[1:]
	#print(new_keys)

	for length, key in zip(lengths,new_keys):
		lib_vals[key] = (lib_vals[key]/length,[1]*length)
	#print(lib_vals)

	return lib_vals

def Caculate(lib_vals): # Giai hist thuc 1 bac
	keys = [key for key in lib_vals]
	lib_tem = {}
	for k in range(len(keys)-1):
		a_val = lib_vals[keys[k]][0]
		a_lis = lib_vals[keys[k]][1]
		a_length =  sum(a_lis)

		b_val = lib_vals[keys[k+1]][0]
		b_lis = lib_vals[keys[k+1]][1]
		b_length =  sum(b_lis)
		
		new_lis = dausis(a_lis,b_lis)
		#print(new_lis)
		new_val = (b_val - a_val)*b_length*a_length/sum(new_lis)
		
		lib_tem[keys[k+1]] = (new_val,new_lis)

	lib_vals = lib_tem
	#print(lib_vals)
	return lib_vals

def HitThuc(lista): # Tinh hist thuc
	lib_vals = Reparelib(lista)
	print(lib_vals)

	lib_vals = Caculate(lib_vals)
	print(lib_vals)

	lib_vals = Caculate(lib_vals)
	print(lib_vals)

	lib_vals = Caculate(lib_vals)
	print(lib_vals)

vals = [(1,0),(3,24),(4,60),(7,336),(8,504),(10,990)]
HitThuc(vals)




