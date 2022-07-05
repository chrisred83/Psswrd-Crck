# Psswrd-Crck
Repo for password cracking examples

First example added was a dictionary attack using Python and a Permutation approach (Later on used Crunch just to generate a wordlist)

Motivation

I created this repo because i had a problem with a private key file that i needed to complete a process of verification during covid-19 and i did not had
the chance to go through all the process again just to get a new private key file with a new password

Problem

The password used was different from the password saved in the file (passphrase) and since i had no clue what happened i decided to investigate and come up with a solution since time was not on my side it took me some days instead of MONTHS (phew)

Pros

I knew which characters were used (unique) so i only had to gather information on how to create a dictionary (wordlist) from the known string
I knew some programming and after reading for a while i decided to use Python (Mindblowing)
I knew some cibersecurity concepts (Theory only) and i briefly saw some techniques to crack passwords but never tried them (Challenge)
I have worked with certificates and i know a few things that helped me out to know which questions i had to ask through the cli (Glad i took my time)

Solution

  Certificates
    
    Since i had git installed i simply used openssl packed with git the only thing here was setting openssl in my path (Windows)
    
    Once ready generate a keypair in pkcs1 format with/without encryption (To see if there was any difference in the output)
    
    Then issue check/inform command from openssl to see the difference in the output shown in cli (This helped me to decide 
    what to put in python script as a filter) when word/psswrd used was right/wrong. I mentioned inform command because the key i was trying to 
    crack was in pkcs8 format
    
  Programming
  
    First i got permutations of a String using Python intertools and save them to a list
    
    Second create a file from the previous list
    
    Third how was i supposed to issue a command for each word in the previous file ? 
    
      That was the next thing to investigate and again using python i read that i could use subprocess module and send a command as a string
      only changing the word/psswrd for each command. So now i had to read each word/psswrd from the file and iterate all the file 
      using Python open function and a for loop i was like: this is fine
    
    Finally i had to adjust the condition that was in charge of ignoring wrong word/psswrds and that made the trick 
    also added a counter to see the progress of the cracking process (just how many words were left to try)

Conclusion

This was entertaining i am not really a super programmer but i have to recognize that this situation was a great opportunity to learn interesting
things from different subjects the only thing here is why in such conditions i felt like in a desperate escape or something
