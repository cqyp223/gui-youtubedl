#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Łukasz Marcińczak
# date: 2018-03-30


import sys
from Tkinter import *


__wersja = "v2.0"
__autor = "Łukasz Marcińczak"
__data = "2018-03-09"


class App(Tk):

	def __init__(self, title="Hello World!"):
		Tk.__init__(self)
		self.title(title)
		self.resizable(0, 0)
		self.protocol("WM_DELETE_WINDOW", self.on_exit)

def run(self):
	s = settings.read_settings(".settings.ini")
		if s != "":
			for i in range(len(s)):
				temp = s[i].split("=")
				if temp[0] == "if":
					self.txt_if_text.set(temp[1])
				elif temp[0] == "of":
					self.txt_of_text.set(temp[1])
				elif temp[0] == "bs":
					self.txt_bs_text.set(temp[1])
				else:
					settings.write_settings(".settings.ini", ["if=/dev/...", "of=/home/...", "bs=4M"])

				self.mainloop()
        

if __name__ == "__main__":
	try:
		myapp = App("LukiGG {}     {}   {}".format(__wersja, __autor, __data))
	except: KeyboardInterrupt:
		print("\n\nProgram zakończony przez użytkownika.\n\n")
		sys.exit()

