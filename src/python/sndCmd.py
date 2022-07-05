#File contains code that sends commands for each word in wordlist file
#using subprocess, a list and a file
#First import subprocess module
import subprocess
#Read passwords from file
#Replace changeMe.txt for the name and extension of your file
print("\n Loading file contents ...")
psswrds = [line.strip() for line in open('wordList.txt')]
print("\n Processing ...")
num = 0

#Iterate list to send a command for each element in the list
#Replace changeMe for the name of your target file
for psswrd in psswrds:
	cmnd = "openssl pkcs8 -in fileName.key -inform der -passin pass:"+psswrd
	sndCmnd = subprocess.run(cmnd, capture_output=True)
	print("psswrd %s of %s" % (num, len(psswrds)))
	#Ignore output when it contains Error, this may change	
	if not sndCmnd.stderr.decode("UTF-8").startswith("Error"):
		print("\n psswrd:"+psswrd)
		print("\n msg:"+sndCmnd.stdout.decode("UTF-8"))
		break
	num += 1
