import sys
import sympy
import os
import random
import math
from cardgame import Deck



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

def da(a):
	a = ['T' if i == 10 else i for i in a]
	a = ['J' if i == 11 else i for i in a]
	a = ['Q' if i == 12 else i for i in a]
	a = ['K' if i == 13 else i for i in a]
	a = [str(i) for i in a]
	return a
	
def da2(a):
	a = ['T' if i == 't' else i for i in a]
	a = ['J' if i == 'j' else i for i in a]
	a = ['Q' if i == 'q' else i for i in a]
	a = ['K' if i == 'k' else i for i in a]
	a = [str(i) for i in a]
	return a

def da3(a):
	a = ['10' if i == 't' else i for i in a]
	a = ['11' if i == 'j' else i for i in a]
	a = ['12' if i == 'q' else i for i in a]
	a = ['13' if i == 'k' else i for i in a]
	a = [int(i) for i in a]
	return a
	
def da4(a):
	a = ['10' if i == 'T' else i for i in a]
	a = ['11' if i == 'J' else i for i in a]
	a = ['12' if i == 'Q' else i for i in a]
	a = ['13' if i == 'K' else i for i in a]
	a = [int(i) for i in a]
	return a

def check(a):
	a = ['10' if i == 't' else i for i in a]
	a = ['11' if i == 'j' else i for i in a]
	a = ['12' if i == 'q' else i for i in a]
	a = ['13' if i == 'k' else i for i in a]
	a = ''.join(a)
	if str.isdecimal(a):
		return True
	else:
		return False

def status(player):
	player.lv = __inilv + player.exp
	player.hp = player.inihp + player.lv * 50
	player.atk = int(player.iniatk + player.lv * 1.5)
	player.vit = player.inivit + player.lv 
	player.mp = player.inimp + player.lv//4
	player.sn = int(player.lv // 10 + 1)
		#print(player.sn)
	if player.sn > len(player.skill_name):
		player.sn = len(player.skill_name)

class Player:
	skill_name = ["リセット 消費MP:1","ヒール　消費MP:5","2ドロー 消費MP:3","ザ・ワールド　消費MP:10","手札が倍だドン 消費MP:10"]
	__inilv = 0
	inihp = 200
	iniatk = 50
	inivit = 50
	inimp = 5
	__skill_count = 5
	
	def __init__(self,name,lv,hp,atk,vit,mp,skill_number,exp):
		self.name = name
		self.lv = lv
		self.hp = hp
		self.atk = atk
		self.vit = vit
		self.mp = mp
		self.sn = skill_number
		self.exp = exp
	
	def attack(self,enemy,n,rev_flag):
		if n < 10**4:
			damage = int(((n**(1/2) * (self.lv // 4 + 1) * (self.atk)**2) // enemy.vit) * random.uniform(0.9,1.1))
		damage = int(((math.log(n) * (self.lv // 4 + 1) * (self.atk)**2) // enemy.vit) * random.uniform(1.8,2.2))
		if rev_flag:
			damage *= random.uniform(0,3) 
			damage = int(damage)
		c = random.randint(1,8)
		if c == 1:
			damage *= 2
			print("会心の一撃!")
		print(enemy.name + "に" + str(damage) +"のダメージ!")
		enemy.hp -= damage
		
	def skill_heal(self):
		healing = int((200 + self.lv * 50) * 0.3)
		print(self.name + "のhpが" + str(healing) + "回復した")
		self.hp += healing
	
	def skill_reset(self,tehuda,n):
		self.mp -= 1
		tehuda.clear()
		d = Deck.Deck()
		d.shuffle()
		tehuda += d.draw(num = n, num_inspect=True)
		tehuda = da4(tehuda)
		tehuda.sort()
		tehuda = da(tehuda)
		return tehuda
		
	def skill_draw_n(self,tehuda,n):
		self.mp -= 3
		d = Deck.Deck()
		d.shuffle()
		tehuda += d.draw(num = n, num_inspect=True)
		tehuda = da4(tehuda)
		tehuda.sort()
		tehuda = da(tehuda)
		return tehuda
		
	def skill_double(self,tehuda,n):
		self.mp -= 10
		tehuda.clear()
		d = Deck.Deck()
		d.shuffle()
		tehuda += d.draw(num = n, num_inspect=True)
		tehuda = da4(tehuda)
		tehuda.sort()
		tehuda = da(tehuda)
		return tehuda
	
class Enemy(Player):
	def __init__(self,name,lv,hp,atk,vit,exp):
		self.name = name
		self.lv = lv
		self.hp = hp
		self.atk = atk
		self.vit = vit
		self.exp = exp
		
	def attack(self,player):
		damage = int((((self.atk)**2)//player.vit)*random.uniform(0.8,1.0))
		print(player.name + "は" + str(damage) + "のダメージを受けた!")
		player.hp -= damage
		
def battle(n,enemy):
	status(player)
	double_flag = False
	tworld_flag = False
	rev_flag = False
	d = Deck.Deck()
	d.shuffle()
	tehuda = []
	tehuda += d.draw(num = n, num_inspect=True)
	tworld_count = 0
	while(True):
		g_flag = False
		flag = False
		tehuda = da4(tehuda)
		tehuda.sort()
		tehuda = da(tehuda)
		print(enemy.name + "  HP:" + str(enemy.hp))
		if rev_flag:
			print("革命中...")
		if tworld_count == 0:
			print("\n")
		else:
			print("ザ・ワールド　残り" + str(tworld_count) + "ターン\n") 
		print(player.name + "lv:" + str(player.lv) + "  HP:" + str(player.hp) + "  MP:" + str(player.mp))
		print("手札:" + " ".join(tehuda) + "\n")
		print("1:攻撃　　2:スキル")
		doing = input("行動を選択:")
		if str.isdecimal(doing):
			doing = int(doing)
		else:
			print("無効な入力だよ")
			input("press enter...")
			os.system("cls")
			continue
		if doing == 1:
			while(True):
				number = input("数を入力:")
				if number == '0':
					flag = True
					os.system("cls")
					break
				if not check(list(number)):
					print("無効な入力だよ")
					continue
				number_list = da2(list(number))
				number_num = da3(list(number))
				#print(number_num)
				#print("number = " + number)
				for i in number_list:
					#print("i = " + i)
					if not i in tehuda:
						print(i + "は手札にありません")
						input("press enter..")
						os.system("cls")
						flag = True
						break
				if flag:
					break
				t = len(number_num)
				p = 0
				for i in range(t):
					if number_num[i] < 10:
						p *= 10
					else:
						p *= 100
					p += number_num[i]
				if is_prime(p):
					player.attack(enemy,p,rev_flag)
					for i in number_list:
						tehuda.remove(i)
					d = Deck.Deck()
					d.shuffle()
					tehuda += d.draw(num = t, num_inspect = True)
					break
				elif p == 57:
					print("グロタンカット!")
					damage = int(enemy.hp * 0.1)
					print(enemy.name + "に" + str(damage) + "のダメージ!")
					enemy.hp -= damage
					g_flag = True
					for i in number_list:
						tehuda.remove(i)
					d = Deck.Deck()
					d.shuffle()
					tehuda += d.draw(num = t, num_inspect = True)
					break
				elif p == 1729:
					print("ラマヌジャン革命!")
					if rev_flag:
						rev_flag = False
					else:
						rev_flag = True
					for i in number_list:
						tehuda.remove(i)
					d = Deck.Deck()
					d.shuffle()
					tehuda += d.draw(num = t, num_inspect = True)
					break
				else:
					print("no prime!")
		elif doing == 2:
			#print(player.sn)
			for i in range(player.sn):
				print(str(i+1) + ":" + player.skill_name[i])
			skill_doing = input("スキルを選択:")
			if str.isdecimal(skill_doing):
				skill_doing = int(skill_doing)
			else:
				print("無効な入力だよ")
				input("press enter...")
				os.system("cls")
				continue
			if skill_doing == 0:
				os.system("cls")
				flag = True
			if skill_doing == 1:
				if player.mp <= 0:
					print("MPが足りないよ!")
					input("press enter...")
					os.system("cls")
					continue
				player.skill_reset(tehuda,n)
				os.system("cls")
				continue
			elif skill_doing == 2:
				if player.mp <= 4:
					print("MPが足りないよ!")
					input("press enter...")
					os.system("cls")
					continue
				player.skill_heal()
				input("press enter...")
				os.system("cls")
				continue
			elif skill_doing == 3:
				if player.mp <= 2:
					print("MPが足りないよ!")
					input("press enter...")
					os.system("cls")
					continue
				n += 2
				player.skill_draw_n(tehuda,2)
				os.system("cls")
				continue
			elif skill_doing == 4:
				if tworld_flag:
					print("もうつかえないよ")
					input("press enter...")
					os.system("cls")
					continue
				tworld_flag = True
				if player.mp <= 9:
					print("MPが足りないよ!")
					input("press enter...")
					os.system("cls")
					continue
				player.mp -= 10
				tworld_count = 2
				os.system("cls")
				continue
			elif skill_doing == 5:
				if double_flag:
					print("もうつかえないドン")
					input("press enter...")
					os.system("cls")
					continue
				double_flag = True
				if player.mp <= 9:
					print("MPが足りないよ!")
					input("press enter...")
					os.system("cls")
					continue
				n *= 2
				player.skill_double(tehuda,n)
				os.system("cls")
				continue
			else:
				continue
		elif doing == 3:
			enemy.hp = 0
		else:
			os.system("cls")
			continue
		if flag:
			continue
		if enemy.hp <= 0:
			print(enemy.name + "は倒れた!")
			print("you win!")
			exp = int(enemy.exp)
			if exp <= 0:
				exp = 0
			print("経験値を" + str(exp) + "手に入れた!")
			#if int(math.log(player.exp)) < int(math.log(player.exp + exp)):
				#print("レベルが上がった!")
			player.exp += exp 
			return True
		if g_flag:
			print(enemy.name + "はひるんでいる")
		elif not tworld_count == 0:
			tworld_count -= 1
			print(enemy.name + "は時間が止まっている!")
		else:
			enemy.attack(player)
		if player.hp <= 0:
			print(player.name + "は負けてしまった...")
			print("you lose...")
			return False
		input("press enter...")
		os.system("cls")

def main():
	os.system("cls")
	print("ver 2.1")
	l = int(input("初期レベルを設定:"))
	player.exp = l
	while True:
		wiles = Enemy("Wiles",1,1000,50,50,4)
		leibniz = Enemy("Libniz",5,5000,70,70,5)
		fibonacci = Enemy("Fibonacci",10,8000,100,50,10)
		turing = Enemy("Turing",20,30000,150,120,30)
		descartes = Enemy("Descartes",50,100000,200,250,50)
		euclid = Enemy("Euclid",100,800000,480,500,100)
		reimann = Enemy("Reimann",200,1600000,800,800,200)
		gauss = Enemy("Gauss",400,5000000,800,1000,200)
		euler = Enemy("Euler",600,10000000,1000,800,400)
		neumann = Enemy("Neumann",1000,99999999,2900,2900,1)
		enemy_list = [wiles,leibniz,fibonacci,turing,descartes,euclid,reimann,gauss,euler,neumann]
		enemy_number = len(enemy_list)
		status(player)
		player.sn = int(player.lv // 10 + 1)
		#print(player.sn)
		if player.sn > len(player.skill_name):
			player.sn = len(player.skill_name)
		os.system("cls")
		while True:
			status(player)
			print("あなたのレベル:" + str(l))
			for i in range(enemy_number):
				print(str(i+1) + ":" + str(enemy_list[i].name) + "(" + str(enemy_list[i].lv) + ")")
			n = input("敵を選択:")
			if n == 'r':
				player.exp = 1
				for i in range(enemy_number):
					os.system("cls")
					if not battle(11,enemy_list[i]):
						print("残念、負けちゃった...")
						input("press enter to finish")
						return 
					input("press enter...")
				return
			if str.isdecimal(n):
				n = int(n)
				break
			else:
				print("無効な入力だよ")
				input("press enter...")
				os.system("cls")
				continue
		os.system("cls")
		battle(11,enemy_list[n-1])
		input("press enter...")
		
player = Player("Player",1,0,0,0,0,1,1)
__inilv = 0
main()