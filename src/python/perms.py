#File contains code to obtain permutations using python itertools module
from itertools import permutations
#Save permutations to a list
#Replace palabraConocida for the word you know or a variation of the same word
listaPalabras = [''.join(palabra) for palabra in permutations('palabraConocida')]
#Save list to repo empty file wordListPy.txt, file is empty but it exists
#Change C:\Users\Username\path\to\your\file\wordList.txt for repo file in your pc, keep quotes
rutaAbsoluta = r"C:\Users\Username\path\to\your\file\wordListPy.txt"
permsTxt = open(rutaAbsoluta, 'w')
for palabra in listaPalabras:
  permsTxt.write("%s\n" % palabra)
permsTxt.close()
