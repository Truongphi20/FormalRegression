import numpy as np
import pandas as pd
from fractions import Fraction
import math

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

def dausis(l1,l2,du): # Tim list phan tich cua 2 list
	hs1,hs2 = quydong(l1,l2)

	dau1_index = len(hs1)-1
	dau2_index = len(hs2)-1
	#print(dau1_index,dau2_index)

	dau1_value = hs1[dau1_index]
	dau2_value = hs2[dau2_index]

	#print(dau1_value,dau2_value)

	rs = np.array([0]*(len(l1)+len(l2)-du))

	while dau1_index >= 0 and dau2_index >= 0:
		#print(dau1_index,dau2_index)

		tem = [0]*(len(hs1)+len(hs2)-du)
		if dau1_value > dau2_value:
			tem = dienso(dau1_index,len(l1)+dau2_index-du,dau2_value,tem)
			#print(f'0: {tem}')
			dau2_index = dau2_index - 1

			dau1_value = dau1_value - dau2_value
			dau2_value = hs2[dau2_index]

		elif dau1_value < dau2_value:
			#print(dau1_index,len(l1)+dau2_index-1,dau1_value)
			tem = dienso(dau1_index,len(l1)+dau2_index-du,dau1_value,tem)
			#print(f'1: {tem}')
			dau1_index = dau1_index - 1

			dau2_value = dau2_value - dau1_value
			dau1_value = hs1[dau1_index]

		else:
			tem = dienso(dau1_index,len(l1)+dau2_index-du,dau1_value,tem)
			#print(f'2: {tem}')
			dau1_index = dau1_index - 1
			dau2_index = dau2_index - 1

			dau1_value = hs1[dau1_index]
			dau2_value = hs2[dau2_index]

		rs = rs + np.array(tem)

		#print(dau1_index,dau2_index)
	return rs.tolist()[1:] 

#print(dausis([3,2,1],[1,2,3],2))

def leng(lista): # khoang cach cac diem
	lengths =[0]*(len(lista)-1)
	for i in range(len(lista)-1):
		lengths[i] = lista[i+1]-lista[i]
	return lengths

def khumau(lis): # Khu mau
	lis_frac = [Fraction(ele).limit_denominator() for ele in lis]
	#print(lis_frac)
	lis_nume = [frac.numerator for frac in lis_frac]
	#print(lis_nume)
	lis_deno = [frac.denominator for frac in lis_frac]
	#print(lis_deno)

	como_deno = math.lcm(*lis_deno)
	#print(como_deno)
	lis_eff = [como_deno/num for num in lis_deno]
	#print(lis_eff)
	new_lis = [int(lis_nume[i]*lis_eff[i]) for i in range(len(lis_eff))]
	#print(new_lis)
	return new_lis, como_deno


def Reparelib(lista): # Chuan bi thu vien

	base, scale = khumau([ele[0] for ele in lista])
	#print(base)

	lib_vals = {base[i]:lista[i][1] for i in range(len(lista))}
	#print(lib_vals)

	keys = [key for key in lib_vals]
	#print(keys)

	for k in range(len(keys)-1):
		lib_vals[keys[len(keys)-1-k]] =  lib_vals[keys[len(keys)-1-k]] - lib_vals[keys[len(keys)-2-k]]
	lib_vals.pop(keys[0])
	#print(lib_vals)

	lengths = leng(base)	# Do dai
	#print(lengths)

	new_keys = keys[1:]
	#print(new_keys)

	for length, key in zip(lengths,new_keys):
		lib_vals[key] = (lib_vals[key]/length,[1]*length)
	#print(lib_vals)

	return lib_vals, scale

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
		
		du = keys[k]-keys[k+1]+len(b_lis)
		#print(keys[k],keys[k+1],b_length)
		new_lis = dausis(a_lis,b_lis,du)
		#print(new_lis)
		
		new_val = (b_val - a_val)*b_length*a_length/sum(new_lis)
		
		lib_tem[keys[k+1]] = (new_val,new_lis)

	lib_vals = lib_tem
	#print(lib_vals)
	return lib_vals

def CheckStop(liba): # Check co dung thuat toan hay khong
	keys = [key for key in liba]
	vals = set([liba[key][0] for key in keys])
	return len(vals)

def NormalTable(table): # Binh thuong hoa list table
	len_empty = [len(table[0]) - len(lista) for lista in table]
	new_table = [[" "]*len_empty[i]+table[i] for i in range(len(len_empty))]
	return new_table

class HitThuc(): # Tinh hist thuc

	def __init__(self,lista):
		self.bac = 1 # Bac cua phuong trinh 
		self.last_vals, self.scale = Reparelib(lista)
		self.truc = list(self.last_vals.keys())
		self.vals = [[self.last_vals[key][0] for key in self.truc]]
		#print(last_vals)
		

		while CheckStop(self.last_vals) > 1:
			self.last_vals = Caculate(self.last_vals)
			#print(last_vals)
			keys = [key for key in self.last_vals]
			self.vals.append([self.last_vals[key][0] for key in keys])

			self.bac += 1

		self.trust = len(self.vals[-1])
		#print(bac)
	def vals_qt(self):
		return [sublis[0] for sublis in self.vals]

	def draw(self):
		truc = self.truc
		#print(truc[0:])
		vals = self.vals
		base = list(range(truc[0],truc[-1]+1))
		#print(base)

		table = [base]
		for b in range(self.bac):
			tem = []
			k = 0
			for num in base[base.index(truc[b]):]:
				if num in truc:
					#print(vals[b][k])
					tem.append(vals[b][k])
					k += 1
				else:
					tem.append(" ")
			#print(tem)
			table.append(tem)
		return pd.DataFrame(NormalTable(table)[1:],columns=table[0])


vals = [(-5,35),(-1,3),(0.5,-0.75),(3,3),(7,35),(11,99)]
print(HitThuc(vals).vals)



