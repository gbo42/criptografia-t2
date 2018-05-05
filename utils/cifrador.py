import playfair as pf

key = "gato"

stringText = pf.generateMatrixString(key)

charDict = []
pf.generateMatrixDict(charDict, stringText)

matrix = [[0 for x in range(5)] for y in range(5)]
pf.generateMatrix(matrix, stringText)

inputtext = open("cifrado", "r")

exittext = open("cifrado2", "w+")

cifrado = ""
while True:
    stringText = inputtext.read(2)
    if len(stringText) == 0 or '\n' in stringText:
        break
    par = pf.getValues(matrix, charDict, stringText, -1)
    cifrado += par[0] + par[1]

exittext.write(cifrado)
