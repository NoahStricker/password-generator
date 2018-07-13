#main setup
from secrets import choice , randbelow
runing = True
conected = True
#define functions
def makePassword():
	chars = [['`','1','2','3','4','5','6','7','8','9','0','-','=','[',']',',''\\',';','\'',',','.','/','~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"','<','>','?'],['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['Z', 'J', 'C', 'F', 'M', 'R', 'E', 'B', 'K', 'P', 'L', 'U', 'G', 'D', 'Y', 'H', 'A', 'O', 'T', 'I', 'X', 'W', 'N', 'V', 'Q', 'S']]
	password = ''
	for i in range(50):
		password += choice(chars[randbelow(3)])
	return password
#main code
print('welcome to Noah\'s password generator')
print('to make a secure password please disconnect from the internet for safty reasions') 
while conected:
	if input('are you conected to the internet y/n') == 'y':
		print('please disconnect from the internet before making your password')
	else:
		conected = False
while runing:
	print('your new password is:',makePassword())
	if input('do you want another password y/n') == 'n':
		runing = False
print('have a nice day')
input() #to prevent the project from exiting to soon
	
