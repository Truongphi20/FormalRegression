from fractions import Fraction
import re
import numpy as np
import argparse


# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-f", "--formula", help = "Sum formula of function")
parser.add_argument("-v",'--version', action='version', version='%(prog)s 1.0',help = 'show version')
parser.add_argument("-s", "--start", default= "1", help = "Start point (default = 1)")
parser.add_argument("-t", "--step", default= "1", help = "Step (default = 1)")

# Read arguments from command line
args = parser.parse_args()

def listToString(s): #Convert list to string
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def chart(val):
		# Find coefficient
	seri_x = list(range(1,val+2,1))
	seri_y = list(range(0,val+1,1))

	list_0 = [1]
	list_poli = []
	for i in range(1,val+2):
		list_tem = ['']*i
		list_poli.append(list_tem)

	list_poli[0][-1] = Fraction(1,1)
	for i in range(1,val+1):
		for k in range(1,i+1):
			list_poli[i][-k] = Fraction(list_poli[i-1][-k]/seri_x[i+1-k]*seri_y[i])
		
		sum_tem = 0
		for n in range(1,i+1):
			sum_tem += list_poli[i][-n]

		list_poli[i][-i-1] = 1 - sum_tem

	#print(list_poli)
	return list_poli

def formal_for(in_for): # Covert string to formal string
	# Read formula input
	infor_add1 = re.sub(r'(^[+-]?|[+-])(x)',r'\g<1>1x',in_for) # Add 1 before x
	infor_addx = re.sub(r'(x)([^^]|$)',r'\g<1>^1\g<2>',infor_add1) # Add ^1 after x
	#print(infor_addx)
	infor_addfr = re.sub(r'([+-]\d+)$',r'\g<1>x^0',infor_addx) # Add x^0 after free efficient
	#print(infor_addfr)
	infor_addfir = re.sub(r'^(\d+)',r'+\g<1>',infor_addfr) # Add + before the positive first 
	return infor_addfir

def dic_eff(in_for): # Creat a dic efficient dic
	formal_string = formal_for(in_for)
	#print(formal_string)

	efficients = re.findall(r'[+-]\d+', formal_string)
	#print(efficients)

	factors = re.findall(r'\^(\d+)', formal_string)
	#print(factors)

	dic = {int(factors[i]):Fraction(efficients[i]) for i in range(len(factors))}
	#print(dic)

	max_fac = max([int(factor) for factor in factors])
	#print(max_fac)

	range_fac = list(range(max_fac+1))
	#print(range_fac)

	for num in range_fac:
		if num not in dic:
			dic[num] = Fraction(0,1)
	#print(dic)
	return dic, max_fac

def calculate_vals(in_for): # Compute values
	dic, max_fac = dic_eff(in_for)
	#print(dic)

	list_vals = list(map(lambda lista: np.array(lista),chart(max_fac)))
	#print(list_vals)

	final_vals = [list_vals[i]*dic[i] for i in range(len(list_vals))]
	#print(final_vals)
	return final_vals

def power_eff(in_for,step): # Calculate power efficiency
	vals = calculate_vals(in_for)
	# print(vals)

	dic_rs = {}
	for order_list, lists in enumerate(vals):
		#print(order_list)
		for order_val, val in enumerate(lists):
			if order_val+1 not in dic_rs:
				dic_rs[order_val+1] = val*step**order_list 
			else:
				dic_rs[order_val+1] += val*step**order_list

	#print(dic_rs)
	return dic_rs

def Sum_Formula(in_for,step): #Find sum formula 
	eff = power_eff(in_for,step)
	#print(eff)

	powers = list(eff.keys())
	#print(powers)

	eff_powers = [eff[power] for power in powers]
	#print(eff_powers)

	# Create a degree functional form
	pt = ['*x^'+str(i) for i in powers]
	#print(pt)

	# Create a list sign
	dau = []
	for i in eff_powers:
		if i < 0:
			dau.append('')
		else:
			dau.append('+')
	#print(dau)

	# Combine to create list result
	ketqua = []
	for i in range(len(dau)):
		ketqua.append(dau[i])
		ketqua.append(eff_powers[i])
		ketqua.append(pt[i])

	formula = "".join(list(map(lambda x :x.__str__(),ketqua)))
	#print(formula)
	return formula

def findc(in_for,num): # Find constant
	tem = in_for.replace('^','**')
	# print(tem)
	# print(num)
	# print(tem.replace('x', num))
	constant = -1*Fraction(eval(tem.replace('x', num)))
	#print(constant)
	return constant

def find_final(formula,start,step):
	# print(start-step)
	# print(formula)
	constant = findc(formula,f'({start-step})')
	#print(constant)

	if constant != 0:
		final_for = str(constant)+"*x^0"+formula
	else:
		final_for = formula

	#print(final_for)
	return final_for

#in_for = "x^3-x^2+x"

def find_final_step(formula,step,start):
	final = Sum_Formula(formula,Fraction(step))
	# print(final)

	hs = re.split(r'\*x\^\d',final)[:-1:]
	# print(hs)

	mu = re.findall(r'\^(\d)',final)
	# print(mu)

	hs_new = []
	for h, m in zip(hs,mu):
		hs_new.append(Fraction(h)/Fraction(step)**int(m))
	#print(hs_new)

	final_step = ''
	for hs, m in zip(hs_new,mu):
		if hs < 0:
			final_step += str(hs)+'*x^'+str(m)
		else:
			final_step += '+'+str(hs)+'*x^'+str(m)
	# print(final_step)
	rs = find_final(final_step,Fraction(start),Fraction(step))

	return rs

print(find_final_step(args.formula,args.step,args.start))
