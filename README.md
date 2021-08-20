'CipherText V2.5'	User Commands


NAME
	CipherText V2.5 - Caesar Cipher Program

SYNOPSIS
	'CipherText V2.5' [OPTION]... [KEY/SHIFT VALUE]... [INPUT]...

DESCRIPTION
	Encode or decode a line of text using the Caesar cipher, this is a basic cipher
	which uses a shift value to encode and decode a message by shifting the position of characters
	relative to their position in the alphabet.
	You can read more about the Caesar cipher and its history here:
	https://en.wikipedia.org/wiki/Caesar_cipher
	
	-e, --encrypt
		encodes the inputted string with the entered shift value and returns the encoded message.
		you may also use a negative value key with this option to decode, however it is not recommended.
	
	-d, --decrypt
		decodes an inputted message with the entered key value
		
	-t,
		unit test mode, to ensure program is functioning correctly
		
BUGS & LIMITATIONS
	due to the way certain symbols such as & | $ etc these may break the shell, any input string ideally 
	should be encompassed by quotation marks to ensure the program completes without error.
	If the string contains no spaces this can be ignored
		
EXAMPLES
	python3 'CipherText V2.2' -e 13 'hello this is a secret message'
	python3 'CipherText V2.2' -e 13 hellothisisasecretmessage
	python3 'CipherText V2.2' --decrypt 13 DHWUYDHSJ

AUTHOR
	Written by Oskar Petersen.
	
REPORTING BUGS
	Please dont.
	
COPYRIGHT
	Copyright  ©  2021  Free Software Foundation, Inc.  License GPLv3+: GNU
        GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
        This is free software: you are free  to  change  and  redistribute  it.
        There is NO WARRANTY, to the extent permitted by law.

CyberSec Cert IV			August 2021				'CipherText V2.5'	
