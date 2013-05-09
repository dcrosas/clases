#Grupo de estudio Python #Semana 2 - Desafio 1

#Descripción:
#Conversión de un valor binario a decimal

#Autor:
#Damià Crosas

def convertToDecimal(inNumber):
    Number=str(inNumber)
    nlength=len(Number)
    outNum=0    
    base=0
    
    for n in range(nlength):
        i = nlength - n - 1
        #base = n + 1
        digit = Number[i]
        if digit == '1':
            outNum += 2**n
    return str(outNum)        

def getInput(inQuestion):
    inNum = raw_input(inQuestion)
    #Validación que el número sea binario
    
    print convertToDecimal(inNum)

convertToDecimal(getInput("Ingresa un numero en binario:"))
