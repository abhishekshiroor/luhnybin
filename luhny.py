luhnIntegers = { '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
luhnMultiples = { '0' : 0, '1' : 2, '2' : 4, '3' : 6, '4' : 8, '5' : 1, '6' : 3, '7' : 5, '8' : 7, '9' : 9}
luhnMask="XXXXXXXXXXXXXXXX"
luhnLength=[16,15,14]

def isLuhny(cardNum):
	sum=0
	for idx,num in enumerate(reversed(cardNum)):
		if num not in luhnIntegers.keys():return False
		if idx%2==0:
			sum+=luhnIntegers[num]
		else:
			sum+=luhnMultiples[num]
	return sum%10==0
		
def luhnCheck(cardNum):
	cardNum=cardNum.replace('-','').replace(' ','')
	newCardNum=cardNum
	if len(cardNum) < 14:return cardNum
	
	for jdx,lower in enumerate(luhnLength):
		upper=0
		while(len(cardNum)-lower>=0):
			if isLuhny(cardNum[len(cardNum)-lower:len(cardNum)-upper]):
				newCardNum=newCardNum.replace(newCardNum[len(newCardNum)-lower:len(newCardNum)-upper],luhnMask[0:luhnLength[jdx]])
			lower+=1
			upper+=1
	return newCardNum

def reformat(maskedNum,cardNum):
	for idx,c in enumerate(cardNum):
		if c in [' ','-']:
			maskedNum.insert(idx,c)
	return "".join(maskedNum)

while True:
	try:
		cardNum = raw_input()
		print reformat(list(luhnCheck(cardNum.strip())),cardNum)
	except EOFError, e:
		break