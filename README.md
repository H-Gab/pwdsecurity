# pwdsecurity

Leet, date handling   
Nicknames handling : convert names into nicknames   
country : deduct informations from countries ? Famous sports/artists/groups...   

genDic.py : function to aggregate everything in order to create a txt output of different passwords

index.html : Form to create a correctly formatted csv

## Usage


To use this program you need to launch gendic.py using python3. If you want to use the html yo uwill need to copy past the csv created inside the folder of the program.

You can put different thing as input : 
-l : the type of leet you want(none, simple, basic and complex)
-sc : if added as input the program will include the special character inside the dictionary creation.
-m : if added as input the program will include the miscmiscellaneous information inside the dictionary creation.
-t : Will print the estimated time, estimated number of combination and the estimated size of file created.
-v : Will activate the verbose
-c : You need to add the password you want to compare after the -c

Example of command
python3 .\genDic.py -l simple -t -sc -m -c Nathan1707

## Resources

https://www.ibm.com/docs/en/baw/20.x?topic=security-characters-that-are-valid-user-ids-passwords

### Dictionnaries 
https://wiki.skullsecurity.org/index.php?title=Passwords#Statistics -> dictionnaires + name lists   
https://github.com/fivethirtyeight/data/blob/master/most-common-name/surnames.csv   

#### Nicknames
https://github.com/MrCsabaToth/SOEMPI/blob/master/openempi/conf/name_to_nick.csv    
https://github.com/carltonnorthern/nicknames/blob/master/names.csv   

#### Pet names   
https://github.com/jgolbeck/petnames   
https://www.kaggle.com/code/residentmario/pet-names-versus-baby-names/input?select=dogNames2.csv   

#### First names (concerning family relatives)
https://pypi.org/project/names-dataset/!<>