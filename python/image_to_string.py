from time import sleep
from PIL import Image
from pytesseract import image_to_string

class Bot:
	def __init__(self):
		self.navigate()
	def tel_recon(self):
		image = Image.open('tel.gif')
		print(image_to_string(image))

	def navigate(self):
		self.tel_recon()

def main():
	b = Bot()

if __name__ == '__main__':
	main()