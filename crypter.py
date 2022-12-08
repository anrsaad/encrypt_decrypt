
# import required module
from cryptography.fernet import Fernet
import os

os.system("cls")
enter = input("\n\nSlide your files here : \n \n \t >> ")
sdout = str(enter)


user = input("\n\n\t\t ~~ [enc] for Encrypting || [dec] for Decrypting ~~\n\n\t >>  ")
if user == "enc":
	os.system("cls")
	# key generation
	key = Fernet.generate_key()
	print(f"\tTHIS IS YOUR ENCRYPTED KEY. \n(Please keep it save and away from anyone, thank you ). \n\n >>\t{key}")


	with open('filekey.key', 'wb') as filekey:
		filekey.write(key)

	# opening the key
	with open('filekey.key', 'rb') as filekey:
		key = filekey.read()

	# using the generated key
	fernet = Fernet(key)

	# opening the original file to encrypt
	with open(sdout, 'rb') as file:
		original = file.read()
		
	# encrypting the file
	encrypted = fernet.encrypt(original)

	# opening the file in write mode and
	# writing the encrypted data
	with open(sdout, 'wb') as enc_file:
		enc_file.write(encrypted)

elif user == "dec":

	with open('filekey.key', 'rb') as filekey:
		key = filekey.read()
	# using the key
		fernet = Fernet(key)

	# opening the encrypted file
	with open(sdout, 'rb') as enc_file:
		encrypted = enc_file.read()

	# decrypting the file
	decrypted = fernet.decrypt(encrypted)

	# opening the file in write mode and
	# writing the decrypted data
	with open(sdout, 'wb') as dec_file:
		dec_file.write(decrypted)

else:
	print("this is not avalid choice")