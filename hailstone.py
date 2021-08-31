def holdcheck(hail: int, hailist: list):
	for n in hailist: 
		if(hail == n):
			return True
	return False


def hailloop(hail: int, a: int, b: int):
	hailist = [hail]
	while(0 < 1):

		if(hail % 2 != 0):
				hail = a * hail + b
		else:
				hail = int(hail/2)
		if (hail == 1):
			hailist += [hail]
			return hailist

		x = holdcheck(hail, hailist)
		if(x == True):
			return hailist
		else: hailist += [hail]
		if len(hailist) > 50:
			return -1

def uniqlo(holdlist: dict):
	k = 0
	# for z in range(1, int(15)):
	# 	uniq[z] = -1
	for i in holdlist:
		m = 0
		for n in range(1,i+1):
			if holdlist[i] == -1:
				break
			if n == i:
				#uniq[i] = holdlist[i]
				k += 1
				break
			if holdlist[i] == holdlist[n]:
				m += 1
			if m > 1:
				break

	return k


def hailstone(a: int, b: int):
	if (a % 2 == 0) & (b % 2 != 0):
		return "infinite"
	holdlist = {}
	for n in range(1, int(15)):
		holdlist[n] = hailloop(n, a, b)
	uniq_patterns = uniqlo(holdlist)
	return uniq_patterns


def printstone(a: int, b: int):
	for c in range(0, b + 1):
		print(a, c, hailstone(a, c))

x = 0

for z in range(0,11):
	printstone(x, (10 - x))
	x +=1