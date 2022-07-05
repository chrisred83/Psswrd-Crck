This folder contains an example of a wordlist using crunch

Command was: crunch 8 8 -o /path/to/file/wordList_0.txt -p L1k3N5us

Where:

  8 8 is minLength maxLength

  -o wordList_0.txt indicates to output words to the file: wordList_0.txt which you can change, notice that if no specific path is used file will be saved in
                    the location where you executed the command

  -p L1k3N5us indicates to obtain permutations of word L1k3N5us which you can change

If you want to create another wordList using permutations try using previous command with a different fileName and word so that you keep 
previously generated files

Once done save your generated file inside of folder: /src/python/ of this repo in your pc

Finally make sure to uncomment line 10 and comment line 9 of sndCmd.py then save it and execute it, so that it can use this file instead of the file created
by perms.py which is wordListPy.txt
