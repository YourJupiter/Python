from tkinter import *
import tkinter.filedialog


def load_file(ev):
    fn = tkinter.filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def save_file(ev):
    filename = tkinter.filedialog.asksaveasfile(mode='w', defaultextension="*.txt")
    if filename == '':
        return
    text = str(textbox.get(1.0, END))
    filename.write(text)
    filename.close()


root = Tk()
panelFrame = Frame(root, height=20, bg='blue')
textFrame = Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font='Arial 12', wrap='word')
scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
loadBtn = Button(panelFrame, text='Open')
loadBtn.bind('<Button-1>', load_file)
loadBtn.pack(side='left')
saveBtn = Button(panelFrame, text='Save')
saveBtn.bind('<Button-1>', save_file)
saveBtn.pack(side='right')

root.mainloop()
