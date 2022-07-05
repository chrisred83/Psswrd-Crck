#File contains code to obtain permutations using python itertools module
from itertools import permutations
#Save permutations to a list
#Replace palabraConocida for the word you know or a variation of the same word
listaPalabras = [''.join(palabra) for palabra in permutations('palabraConocida')]
#Save list to a previously created file, file is empty but it exists
#Change C:\Users\Username\path\to\your\file\fileName.extension for the path of your file, keep quotes
rutaAbsoluta = r"C:\Users\Username\path\to\your\file\fileName.extension"
permsTxt = open(rutaAbsoluta, 'w')
  for palabra in palabras:
    permsTxt.write("%s\n" % palabra)
  permsTxt.close()
