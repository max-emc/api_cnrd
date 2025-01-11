from enigma.machine import EnigmaMachine
from random import choice, sample
from string import ascii_uppercase

class Enigma:

	def __init__(self, true_position=None, rotors=None):
		self.machine = EnigmaMachine.from_key_sheet()

		if true_position and rotors:
			self.true_position = true_position
			self.rotors = rotors
		else:
			self.true_position = "".join(choice(ascii_uppercase) for _ in range(3))
			self.rotors = [set(sample(ascii_uppercase, 4) + [self.true_position[i]]) for i in range(3)]

		self.words = [
			"UN",
			"DEUX",
			"TROIS"
		]
		self.text = "MON PARAGRAPHE A CODER"

		self.crypted_words = self.encrypt_words()
		self.crypted_text = self.machine.process_text(self.text)

	def encrypt_words(self):
		crypted_words = []

		for i in range(3):
			self.machine.set_display(self.true_position[:i+1] + "".join(list(self.rotors[i])[:2-i]))
			crypted_words.append(self.machine.process_text(self.words[i]))

		return crypted_words

	def decode(self, position):
	    decoded_words = []

	    for i in range(3):
	        self.machine.set_display(position[:i+1] + "".join(list(self.rotors[i])[:2-i]))
	        decoded_words.append(self.machine.process_text(self.crypted_words[i]))

	    decoded_text = self.machine.process_text(self.crypted_text)

	    return decoded_words, decoded_text.replace("X", " ")

if __name__ == "__main__":
	enigma = Enigma("AAA", [{'I', 'E', 'C', 'W'}, {'I', 'G', 'H', 'D', 'V'}, {'L', 'W', 'M', 'Z', 'V'}])
	print(enigma.encrypt_words())
	print(enigma.text)

	print(enigma.decode("ABC"))
	print(enigma.decode(enigma.true_position))

	print(enigma.rotors)
