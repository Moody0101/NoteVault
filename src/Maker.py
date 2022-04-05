from util import (
	encode_, 
	decode_, 
	hash_, 
	verifypassword, 
	store, 
	read,
	exists
)

from vars import (
	RED,
	GREEN,
	YELLOW,
	BLUE,
	LIGHTYELLOW_EX,
	RESET
)

from dataclasses import dataclass
from os import path, environ, remove

INTRODUCTION = """
An interactive notebook to keep secret notes.
written by: Moody0101
Language: PYTHON 3.10

"""

@dataclass
class NoteBook:

	PATH: str = path.join(environ['USERPROFILE'], 'Nts.txt')

	def __init__(self):
		""" The starter method of the whole program. """
		if not exists(self.PATH):
			# Make new Notebook.

			self.MakeNewNoteBook()
		else:
			# Update the Notes.
			if self.checkPassword():
				self.menu()
			else:
				print(f"{RED}The password you provided is wrong!")

	def MakeNewNoteBook(self):
		""" if the user has not yet created a notebook, this one kicks in and makes one! """
		print(f"""
{GREEN}Looks like you don't have a notebook registered yet, you can add one by just setting a password!
""")
		with open(self.PATH, 'w') as file:
			password = input(f"{YELLOW}Enter a secure Password: ")
			file.write(encode_(hash_(password)))
			print(f"{GREEN}The Notebook has been created, you can add, delete, view notes now.")
			self.menu()

	def checkPassword(self) -> bool:
		""" returns True if the hash is identical. if not returns False """
		with open(self.PATH, 'r') as file:
			password = input(f"{YELLOW}Enter your password: ")
			return verifypassword(password, file.readlines()[0])

	def display(self):
		""" a Menu method to display the notes """
		print("\n")
		print(f"{LIGHTYELLOW_EX}============================YOUR NOTES============================")
		read(self.PATH)

	def clearNotes(self):
		""" a method to delete all the notes after checking the password once again. """

		if self.checkPassword():
			remove(self.PATH)
			print(f"{GREEN}The Notebook was deleted successfully!")
		else:
			print(f"{RED}The password you provided is wrong!")

	def addNote(self):
		""" method to add a note to the noteBook. """

		note = input(f"{YELLOW}Note to be added:{RESET} ")
		with open(self.PATH, "a") as file:
			file.write("\n")
			file.write(encode_(f"{str(note)}"))
			print(f"{GREEN}It was added successfully!!")

	def menu(self):
		""" When the password is correct, the user is granted the permession to enter to this menu."""
		self.run_ = True
		while self.run_:
			choice = input(f"""{YELLOW}
(1) Display notes.
(2) Add note.
(3) clear notes.
(00) EXIT
INPUT:{RESET} """)		
			try:
				if int(choice) == 1:
					self.display()
				elif int(choice) == 2:
					self.addNote()
				elif int(choice) == 3:
					self.clearNotes()
					self.quit()

				elif int(choice) == 0:
					self.quit()

			except Exception as e:
				print(f"{RED}The choice input should be a number!", e)

	def quit(self):
		for i in ['-','\\' , '|', '/']*2:
			print(f'{BLUE} quiting {i}', end="\r")
			sleep(.3)
		self.run_ = False

def main(): # {
	print(INTRODUCTION)
	NoteBook()
	print(RESET)
# }


if __name__ == '__main__': 
	
	main()

	print(RESET)

	# print(exists(path.join(environ['USERPROFILE'], 'Nts.txt')))