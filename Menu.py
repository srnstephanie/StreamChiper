import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, ttk, filedialog
import pathlib
import os
import RC4

class MenuPage(ttk.LabelFrame):

    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Menu()

    def Menu(self):
        # title
        self.isFile = False
        self.intro = Label(self, text = 'My Own Stream Chiper', font = "Helvetica 10 bold", justify=CENTER)
        self.intro.grid(sticky="n", row = 0, columnspan = 1, pady = 2, padx = 5)
        self.Frames = Frame(self)
        self.Frames.grid(row = 2, sticky = "w", pady = 2)
        self.Framess()
        self.Frames.tkraise()
        self.intro = Label(self, text = 'Stephanie Hutagalung-18220001', font = "Helvetica 8", justify=CENTER)
        self.intro.grid(sticky="e", row = 3, columnspan = 1, pady = 2, padx = 5)
        

    def Framess(self):
        self.Frames = Frame(self)
        # this will create a label widget 
        self.Frames.l1 = Label(self.Frames, text = "Input")
        self.Frames.l2 = Label(self.Frames, text = "Key")
        self.Frames.l3 = Label(self.Frames, text = "Mode")
        self.Frames.l5 = Label(self.Frames, text = "Output")
        self.Frames.l1.grid(row = 2, column = 0, sticky = "w", pady = 2)
        self.Frames.l2.grid(row = 3, column = 0, sticky = "w", pady = 2)
        self.Frames.l3.grid(row = 4, column = 0, sticky = "w", pady = 2)
        self.Frames.l5.grid(row = 7, column = 0, sticky = "w", pady = 2)
        # this will arrange entry widgets
        self.Frames.e1 = scrolledtext.ScrolledText(self.Frames, wrap=tk.WORD,
                                            width=80, height=4,
                                            font=("Times New Roman", 10))

        self.Frames.e2 = scrolledtext.ScrolledText(self.Frames, wrap=tk.WORD,
                                            width=80, height=4,
                                            font=("Times New Roman", 10))
        self.Frames.e3 = LabelFrame(self.Frames)
        self.Frames.radioe3 = IntVar()
        ttk.Radiobutton(self.Frames.e3, text="Encrypt", variable=self.Frames.radioe3, value=1).grid(sticky="w", row = 1, column = 0)
        ttk.Radiobutton(self.Frames.e3, text="Decrypt", variable=self.Frames.radioe3, value=2).grid(sticky="w", row = 1, column = 1)

        self.Frames.e5 = scrolledtext.ScrolledText(self.Frames, wrap=tk.WORD,
                                            width=80, height=4,
                                            font=("Times New Roman", 10))
        self.Frames.e1.grid(sticky="w", row = 2, column = 1, pady = 2)
        self.Frames.e2.grid(sticky="w", row = 3, column = 1, pady = 2)
        self.Frames.e3.grid(sticky="w", row = 4, column = 1, pady = 2)
        self.Frames.e5.grid(sticky="w", row = 7, column = 1, pady = 2)
        self.Frames.b1 = Button(self.Frames,text="Add file", command=lambda:self.open_text())
        self.Frames.b2 = Button(self.Frames,text="Save file", command=lambda:self.save_text())
        self.Frames.b3 = Button(self.Frames, width=10, text = "Run", command =lambda:self.run())
        self.Frames.b4 = Button(self.Frames, width=10,text = "Reset", command=lambda:self.reset())
        self.Frames.b1.grid(row=2, column = 2, pady = 2, padx = 5)
        self.Frames.b2.grid(sticky="w", row=7, column = 2, pady = 2, padx = 5)
        self.Frames.b3.grid(sticky="n", row=6, columnspan = 3, pady = 2, padx = 5)
        self.Frames.b4.grid(sticky="n", row=8, columnspan = 3, pady = 2, padx = 5)
        self.Frames.grid(row = 2, sticky = "w", pady = 2)

    def startPage(self):
        self.mainloop()

    def open_text(self):
        try:
            self.filename = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/'
                )
            self.isFile = True
            self.Frames.e1.delete('0.0', tk.END)
            self.Frames.e1.insert(tk.END, 'Tekan run untuk memproses file')
        except:
            False

    def save_text(self):
        try:
            filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*')
            )

            save = filedialog.asksaveasfile(
                mode='w',
                title='Save file',
                initialdir='/',
                filetypes=filetypes,
                defaultextension=".txt")
            output = ''
            output = self.Frames.e5.get("1.0", "end-1c")
            save.write(output)
            save.close 
        except:
            False


    def run(self):
        try:
            self.input = self.Frames.e1.get("1.0", "end-1c" )
            self.key = self.Frames.e2.get("1.0", "end-1c")
            self.mode = self.Frames.radioe3.get()
            self.typeoutput = self.Frames.e5
            self.keyy = self.Frames.e2
            self.output =''
            if self.key != '':
                if self.isFile:
                    with open(self.filename, 'rb') as f:
                        fileinput = f.read()
                    f.close()
                    self.input = fileinput.decode("latin-1")
                    if self.mode == 1:   
                        output = RC4.enkrip(self.input, self.key)
                    elif self.mode == 2:
                        output = RC4.dekrip(self.input, self.key)
                    self.output = output.encode("latin-1")
                    with open(self.filename, "wb") as f:
                        f.write(self.output)
                    f.close()
                    self.isFile = False
                    self.output= 'proses berhasil'
                else:
                    if self.mode == 1:
                        self.output = RC4.enkrip(self.input, self.key)
                    elif self.mode == 2:
                        self.output = RC4.dekrip(self.input, self.key)
            else:
                self.output = 'Masukkan key agar pesan dapat diproses.'
            self.typeoutput.delete('0.0', tk.END)
            self.typeoutput.insert(tk.END, self.output)
        except:
            self.isFile = False
            False
        
    
    def reset(self):
        self.Frames.e1.delete('0.0', tk.END)
        self.Frames.e2.delete('0.0', tk.END)
        self.Frames.e5.delete('0.0', tk.END)