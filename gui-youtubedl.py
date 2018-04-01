#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Łukasz Marcińczak
# date: 2018-04-01


import sys
import settings
import youtube_dl as ydl
from Tkinter import *
# from tkFileDialog import askoopenfilename


__wersja = "v2.0"
__autor = "Łukasz Marcińczak"
__data = "2018-03-09"


class App(Tk):

	def __init__(self, title="Hello World!"):
		Tk.__init__(self)
		self.title(title)
		self.resizable(0, 0)
		self.protocol("WM_DELETE_WINDOW", self.on_exit)
		
		self.txt_if_text = StringVar()
		self.txt_of_text = StringVar()
		self.txt_bs_text = StringVar()
		
		self.txt_if = Entry(self, textvariable=self.txt_if_text).grid(row=0, column=1, sticky=E+W)
		self.txt_of = Entry(self, textvariable=self.txt_of_text).grid(row=1, column=1, sticky=E+W)
		self.txt_bs = Entry(self, textvariable=self.txt_bs_text).grid(row=2, column=1, sticky=E+W)

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

		self.youtube = ydl.YoutubeDl({"outtmp1": "%(id)s%(ext)s"})
		with self.youtube:
			self.result = youtube.extract_info("https://www.youtube.com/watch?v=F57P9C4SAW4", download=False)
		
		if "enteries" in self.result:
			video = self.result["enteries"][0]
		else:
			video = result
			
		print(video)
		
		self.mainloop()

	def on_exit(self):
		self.zapisz_ustawienia()
		self.destroy()

	def zapisz_ustawienia(self):
		settings.write_settings(".settings.ini", ["if=" + self.txt_if_text.get(), "of=" + self.txt_of_text.get(), "bs=" + self.txt_bs_text.get()])
    
        

if __name__ == "__main__":
	try:
		myapp = App("LukiGG {}     {}   {}".format(__wersja, __autor, __data))
		myapp.run()
	except KeyboardInterrupt:
		print("\n\nProgram zakończony przez użytkownika.\n\n")
		sys.exit()

