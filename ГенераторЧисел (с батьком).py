import re
#b = input()
cStr = "00F00151C0010F000"
#cStr = ""
arrLen = list(cStr)
maxLen = len(cStr)
iNext = 0
findSymbol = False
findZero = False
cGenSum =""
iGenSum = 0
nSum = 0
newStr = ""

print("arrLen = ",arrLen)
#Длинна строки больше 1
if (maxLen > 1):
    for i in range(len(arrLen)):  
        if (re.search("[^\\d]", arrLen[i])):
            iNext = i
            findSymbol = False
            findZero = True
            
        if ((findZero == True or findSymbol == False) and arrLen[i] == "0"):
            iNext = i

        if (re.search("[1-9]", arrLen[i])):
            findZero = False
            findSymbol = True

iNext = iNext+1        
nSum = maxLen-iNext
if (nSum > 0):
   cGenSum = cStr[iNext:maxLen] #подстрока
   iGenSum = int(cGenSum)+1
else:
   iGenSum = 1

newStr = cStr[0:iNext]

#Если длинна строки равно 1
if (maxLen == 1):
    if re.search("[^\\d]", arrLen[0]):
        newStr = cStr+1
    else:
        newStr = ""
        iGenSum = int(cStr)+1

cResultStr = newStr+str(iGenSum)


print("Позиция символа=",iNext, " maxLen=",maxLen, "iNext=",iNext," nSum=",nSum,"cGenSum=",cGenSum,"iGenSum=",iGenSum,"newStr=",newStr)
print("Текущее=", cStr,"Новый=",cResultStr) 
