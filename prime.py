import random
import sympy
import sys

def is_prime(n):
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True
def fx(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	for i in range(n):
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				num[i] = j
				fx(n)
			k[i] = 14
			return
		elif k[i] == -1:
			continue
		else:
			num[i] = k[i]
	p = 0
	for i in range(n):
		if num[i] < 10:
			p *= 10
		else:
			p *= 100
		p += num[i]
	if p > kmin and p < kmax and is_prime(p) == True:
		#print('p=',p)
		pl.append(p)
		ad(n)
		pc += 1
	return
def ad(n):
	global pa
	global pal
	global pc
	pa.clear()
	for i in range(n):
		if num[i] == 10:
			pa += 'T'
		elif num[i] == 11:
			pa += 'J'
		elif num[i] == 12:
			pa += 'Q'
		elif num[i] == 13:
			pa += 'K'
		else:
			pa += str(num[i])
	v = ''.join(pa)
	pal.append(v)
def adc(n):
	global pa
	global pal
	global pc
	pa.clear()
	for i in range(n):
		if num[i] == 10:
			pa += 'T'
		elif num[i] == 11:
			pa += 'J'
		elif num[i] == 12:
			pa += 'Q'
		elif num[i] == 13:
			pa += 'K'
		else:
			pa += str(num[i])
	pa = [i for i in pa if not i == '0']
	v = ''.join(pa)
	return v
def fxa(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	for i in range(n):
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				#print(i,j)
				num[i] = j
				fxa(n)
			k[i] = 14
			return
		elif k[i] == -1:
			continue
		elif k[i] == -2:
			num[i] = 'a'
		else:
			num[i] = k[i]
	num = [i for i in num if not i == -3]
	#print(num)
	p = map(str, num)
	p = ''.join(p)
	#print(p)
	for i in an:
		#print('i=',i)
		kp = p
		#print(kp)
		kp = kp.replace('a',str(i))
		#print(kp)
		kp = int(kp)
		#print(type(kp))
		if kp > kmax or kp <kmin:
			return
		if is_prime(kp) == False:
			return
	print(adc(n))
	return
def fxc(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	#print(cn)
	for i in range(n):
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				#print(i,j)
				num[i] = j
				fxc(n)
			k[i] = 14
			return
		elif k[i] == -1:
			continue
		elif k[i] == -4:
			num[i] = 'c'
		else:
			num[i] = k[i]
	num = [i for i in num if not i == -3]
	#print(num)
	p = map(str, num)
	p = ''.join(p)
	#print(p)
	cnn = cn.copy()
	#print(cn)
	#print(cnn)
	for i in cn:
		#print('i=',i)
		kp = p
		#print(kp)
		while 1:
			kp = kp.replace('c',str(i),1)
			if not 'c' in kp:
				break
		#print(kp)
		kp = int(kp)
		#print(type(kp))
		if kp > kmax or kp <kmin:
			return
		if is_prime(kp) == False:
			#print(cn,cnn)
			cnn.remove(i)
			#print(cn,cnn)
			continue
	if cnn:
		#print(p,'(c=',cnn,')')
		cnn = ['T' if i == 10 else i for i in cnn]
		cnn = ['J' if i == 11 else i for i in cnn]
		cnn = ['Q' if i == 12 else i for i in cnn]
		cnn = ['K' if i == 13 else i for i in cnn]
		print(adc(n),'(c=',cnn,')')
	return
def fxbb(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	#print('test fxb')
	for i in range(n):
		#print(i,k[i],num[i])
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				#print(i,j)
				num[i] = j
				fxbb(n)
			k[i] = 14
			return
		elif k[i] == -5:
			k[i] = -1
			for j in bn:
				num[i] = j
				fxbb(n)
			k[i] = -5
			return
		elif k[i] == -1:
			continue
		elif k[i] == -2:
			num[i] = 'a'
		else:
			num[i] = k[i]
	num = [i for i in num if not i == -3]
	#print(num)
	p = map(str, num)
	p = ''.join(p)
	#print(p)
	#print('i=',i)
	kp = p
	#print(kp)
	#kp = kp.replace('a',str(i))
	#print(kp)
	kp = int(kp)
	#print(type(kp))
	if kp > kmax or kp <kmin:
		return
	if is_prime(kp) == False:
		return
	print(adc(n))
	return
def fxb(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	#print('test fxb')
	for i in range(n):
		#print(i,k[i])
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				#print(i,j)
				num[i] = j
				fxb(n)
			k[i] = 14
			return
		elif k[i] == -5:
			k[i] = -10
			for l in bn:
				#print(i,l)
				num[i] = l
				fxb(n)
			k[i] = -5
			return 
		elif k[i] == -1:
			continue
		elif k[i] == -10:
			continue
		elif k[i] == -2:
			num[i] = 'a'
		else:
			num[i] = k[i]
	num = [i for i in num if not i == -3]
	#print(num)
	p = map(str, num)
	p = ''.join(p)
	#print(p)
	for i in an:
		#print('i=',i)
		kp = p
		#print(kp)
		kp = kp.replace('a',str(i))
		#print(kp)
		kp = int(kp)
		#print(type(kp))
		if kp > kmax or kp <kmin:
			return
		if is_prime(kp) == False:
			return
	print(adc(n))
	return
def ph(n,q):
	global pc
	if q == 0:
		p = 0
		for i in range(n):
			if num[i] < 10:
				p *= 10
				p += num[i]
			else:
				p *= 100
				p += num[i]
		if is_prime(p) == True:
			for i in range(pc):
				if pl[i] == p:
					return
			pl.append(p)
			print(p)
			ad(n)
			pc += 1
		return
	for i in range(n):
		if flag[i] == 1:
			continue
		flag[i] = 1
		if k[i] == 14:
			for j in range(i,14):
				num[q-1] = j
				ph(n,q-1)
		else:
			num[q-1] = k[i]
			ph(n,q-1)
		flag[i] = 0
def fxz(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	for i in range(n):
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				#print(i,j)
				num[i] = j
				fxz(n)
			k[i] = 14
			return
		elif k[i] == -1:
			continue
		elif k[i] == -2:
			num[i] = 'a'
		elif k[i] == -3:
			num[i] = 'z'
		else:
			num[i] = k[i]
	num = [i for i in num if not i == -3]
	#print(num)
	p = map(str, num)
	p = ''.join(p)
	#print(p)
	for i in range(1,14):
		kp = p
		kp = kp.replace('z',str(i),10)
		kp = int(kp)
		#print(kp)
		if is_prime(kp) == True:
			print(kp)
	return
def fxy(n):
	global k
	global p
	global pc
	global num
	global pl
	global pal
	for i in range(n):
		if k[i] == 14:
			k[i] = -1
			for j in range(1,14):
				#print(i,j)
				num[i] = j
				fxy(n)
			k[i] = 14
			return
		elif k[i] == -5:
			k[i] = -10
			for l in bn:
				#print(i,l)
				num[i] = l
				fxy(n)
			k[i] = -5
			return 
		elif k[i] == -6:
			num[i] = 0
		elif k[i] == -10:
			continue
		elif k[i] == -1:
			continue
		else:
			num[i] = k[i]
	num = [i for i in num if not i == -3]
	#print(num,bn)
	p = map(str, num)
	p = ''.join(p)
	#print(p)
	kp = p
	kp = int(kp)
	#print(yn)
	if yc == 0:
		for w in yn:
			#print(w)
			kp += w
			#print(kp)
			if kp > kmax or kp <kmin:
				kp -= w
				return
			if is_prime(kp) == False:
				kp -= w
				return
			kp -= w
	else:
		for w in ynn:
			kp += w
			if kp > kmax or kp <kmin:
				kp -= w
				return
			if is_prime(kp) == False:
				kp -= w
				return
			kp -= w
	print(adc(n)+'y')
	return
print('ver6.1')
print('apply x ,y,z,a,b,c,ab')
while 1:
	jflag = False
	aflag = False
	zflag = False
	yflag = False
	cflag = False
	bflag = False
	kmax = 10**15
	kmin = 0
	num = [-3] * 100
	pc = 0
	pl = []
	pa = ['0']
	pal = []
	mflag = [0] * 100000
	maisuu = [[0] * 13 for i in range(100000)]
	p = 0
	kp = 0
	flag = [0] *100

	ap = input('input num:')
	t = len(ap)
	if 'x' in ap:
		jflag = True
		kn = input('input cards:')
		int(kn)
		if int(kn) != 0:
			kmax = 10**(int(kn))
			kmin = 10**(int(kn)-1)
		elif int(kn) == 0:
			kmax = 10**15
			kmin = 0
	if 'a' in ap:
		aflag = True
		an = input('input in a:').split()
		an = ['10' if i == 't' else i for i in an]
		an = ['11' if i == 'j' else i for i in an]
		an = ['12' if i == 'q' else i for i in an]
		an = ['13' if i == 'k' else i for i in an]
		#an = list(an)
		an = [int(i) for i in an]
		an.sort()
	if 'z' in ap:
		zflag = True
	if 'y' in ap:
		yflag = True
		yc = input('quadruplet:0  twin quadruplet:9  :')
		yc = int(yc)
		yn = [1,3,7,9]
		ynn = [1,3,7,9,31,33,37,39]
	if 'c' in ap:
		cflag = True
		cn = input('input in c:').split()
		cn = ['10' if i == 't' else i for i in cn]
		cn = ['11' if i == 'j' else i for i in cn]
		cn = ['12' if i == 'q' else i for i in cn]
		cn = ['13' if i == 'k' else i for i in cn]
		cn = [int(i) for i in cn]
		cn.sort()
	if 'b' in ap:
		bflag = True
		bn = input('input in b:').split()
		bn = ['10' if i == 't' else i for i in bn]
		bn = ['11' if i == 'j' else i for i in bn]
		bn = ['12' if i == 'q' else i for i in bn]
		bn = ['13' if i == 'k' else i for i in bn]
		bn = [int(i) for i in bn]
		bn.sort()
	k = list(ap)
	k = ['10' if i == 't' else i for i in k]
	k = ['11' if i == 'j' else i for i in k]
	k = ['12' if i == 'q' else i for i in k]
	k = ['13' if i == 'k' else i for i in k]
	k = ['14' if i == 'x' else i for i in k]
	k = ['-2' if i == 'a' else i for i in k]
	k = ['-3' if i == 'z' else i for i in k]
	k = ['-4' if i == 'c' else i for i in k]
	k = ['-5' if i == 'b' else i for i in k]
	k = ['-6' if i == 'y' else i for i in k]
	k = [int(i) for i in k]
	#print(aflag,bflag,cflag,zflag)
	if bflag and aflag:
		fxb(t)
		print('\n')
		continue
	if yflag == True:
		fxy(t)
		print('\n')
		continue
	if bflag == True:
		fxbb(t)
		print('\n')
		continue
	if zflag == True:
		fxz(t)
		print('\n')
		continue
	if aflag == True:
		fxa(t)
		print('\n')
		continue
	if cflag == True:
		fxc(t)
		print('\n')
		continue
	elif jflag == False and aflag == False:
		p = 0
		for i in range(t):
			if k[i] < 10:
				p *= 10
			else:
				p *= 100
			p += k[i]
		if is_prime(p):
			print(p,'is prime number')
		else:
			print(p,'=',sympy.factorint(p))
		print('\nyes:9 no:0')
		r = input('search combination?:')
		if r == '9':
			ph(t,t)
			print('\n')
		else:
			print('\n')
			continue
	else:
		fx(t)
	pl = [i for i in pl if not i == 0]
	pal = [i for i in pal if not i == '0']
	for i in range(pc):
		for j in range(i+1,pc):
			if pl[i]>pl[j]:
				pl[i],pl[j] = pl[j],pl[i]
				y = pal[i]
				pal[i] = pal[j]
				pal[j] = y
	for i in range(pc):
		for j in range(t):
			if pal[i][j] == '1':
				maisuu[i][0] += 1
			elif pal[i][j] == '2':
				maisuu[i][1] += 1
			elif pal[i][j] == '3':
				maisuu[i][2] += 1
			elif pal[i][j] == '4':
				maisuu[i][3] += 1
			elif pal[i][j] == '5':
				maisuu[i][4] += 1
			elif pal[i][j] == '6':
				maisuu[i][5] += 1
			elif pal[i][j] == '7':
				maisuu[i][6] += 1
			elif pal[i][j] == '8':
				maisuu[i][7] += 1
			elif pal[i][j] == '9':
				maisuu[i][8] += 1
			elif pal[i][j] == 'T':
				maisuu[i][9] += 1
			elif pal[i][j] == 'J':
				maisuu[i][10] += 1
			elif pal[i][j] == 'Q':
				maisuu[i][11] += 1
			elif pal[i][j] == 'K':
				maisuu[i][12] += 1
		for j in range(13):
			if maisuu[i][j] > 4:
				mflag[i] = 1
	for i in range(pc-2,1,-1):
		if mflag[i] == 0:
			for j in range(i+1,pc):
				if maisuu[i] == maisuu[j]:
					mflag[i] = 1
	for i in range(pc):
		if mflag[i] == 0:
			print(pal[i])
	#print('number is',pc)
	print('\n')