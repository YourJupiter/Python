from tkinter import *

t_text = 'Зображення трикутника'
r_text = 'Зображення прямокутника'
c_text = 'Зображення кола'
t_coords = [50, 200, 340, 200, 110, 60]
r_coords = [80, 50, 320, 200]
c_coords = [50, 10, 150, 110]
t_color = 'yellow'
r_color = 'blue'
c_color = 'pink'


def triangle():
    canvas.coords(c, (0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.itemconfig(t, fill=t_color, outline='white')
    canvas.coords(t, t_coords)
    text.delete(1.0, END)
    text.insert(1.0, t_text)
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 14), foreground='blue')


def rectangle():
    canvas.coords(c, (0, 0, 0, 0))
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.itemconfig(r, fill=r_color, outline='white')
    canvas.coords(r, r_coords)
    text.delete(1.0, END)
    text.insert(1.0, r_text)
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 14), foreground='black')


def circle():
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.itemconfig(c, fill=c_color, outline='white')
    canvas.coords(c, c_coords)
    text.delete(1.0, END)
    text.insert(1.0, c_text)
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 14), foreground='red')


def clear():
    text.delete(1.0, END)
    canvas.coords(c, (0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(t, (0, 0, 0, 0, 0, 0))


def text_settings():
    popup = Toplevel()

    nt = Label(popup, text="Новий текст для трикутника")
    nr = Label(popup, text="Новий текст для прямокутника")
    nc = Label(popup, text="Новий текст для кола")
    te = Entry(popup)
    re = Entry(popup)
    ce = Entry(popup)

    nt.grid(row=0, column=0)
    te.grid(row=0, column=1)

    nr.grid(row=1, column=0)
    re.grid(row=1, column=1)

    nc.grid(row=2, column=0)
    ce.grid(row=2, column=1)

    def assign_text_setting():
        global t_text, r_text, c_text
        c_text = ce.get() if ce.get() != '' else c_text
        r_text = re.get() if re.get() != '' else r_text
        t_text = te.get() if te.get() != '' else t_text
        popup.destroy()

    b = Button(popup, text="Готово", command=assign_text_setting)
    b.grid(row=3, column=0)


def choose_shape():
    popup = Toplevel()

    label = Label(popup, text="Виберіть фігуру")
    t = Button(popup, text="Triangle", command=lambda: [color_settings('t'), popup.destroy()])
    r = Button(popup, text="Rectangle", command=lambda: [color_settings('r'), popup.destroy()])
    c = Button(popup, text="Circle", command=lambda: [color_settings('c'), popup.destroy()])

    label.grid(row=0, column=0)
    t.grid(row=0, column=1)
    r.grid(row=0, column=2)
    c.grid(row=0, column=3)


def color_settings(shape):
    popup = Toplevel()

    label = Label(popup, text="Виберіть колір")
    red = Button(popup, text="Red", command=lambda: assign_color_settings('red'))
    green = Button(popup, text="Green", command=lambda: assign_color_settings('green'))
    blue = Button(popup, text="Blue", command=lambda: assign_color_settings('blue'))

    label.grid(row=0, column=0)
    red.grid(row=0, column=1)
    green.grid(row=0, column=2)
    blue.grid(row=0, column=3)

    def assign_color_settings(color):
        global t_color, r_color, c_color
        if shape == 't':
            t_color = color
        elif shape == 'r':
            r_color = color
        elif shape == 'c':
            c_color = color
        popup.destroy()


def size_setting():
    popup = Toplevel()

    label = Label(popup, text="Виберіть фігуру")
    t = Button(popup, text="Triangle", command=lambda: [choose_size('t'), popup.destroy()])
    r = Button(popup, text="Rectangle", command=lambda: [choose_size('r'), popup.destroy()])
    c = Button(popup, text="Circle", command=lambda: [choose_size('c'), popup.destroy()])

    label.grid(row=0, column=0)
    t.grid(row=0, column=1)
    r.grid(row=0, column=2)
    c.grid(row=0, column=3)

    def choose_size(shape):
        popup = Toplevel()

        label = Label(popup, text="Choose size")
        red = Button(popup, text="Small", command=lambda: assign_size_settings('s'))
        green = Button(popup, text="Medium", command=lambda: assign_size_settings('m'))
        blue = Button(popup, text="Big", command=lambda: assign_size_settings('b'))

        label.grid(row=0, column=0)
        red.grid(row=0, column=1)
        green.grid(row=0, column=2)
        blue.grid(row=0, column=3)

        def assign_size_settings(size):
            global t_coords, r_coords, c_coords
            tc = {'s': [50, 200, 200, 200, 110, 60], 'm': [50, 200, 340, 200, 110, 60], 'b': [10, 200, 400, 200, 200, 60]}
            rc = {'s': [50, 50, 150, 100], 'm': [75, 75, 250, 150], 'b': [80, 50, 320, 200]}
            cc = {'s': [30, 50, 70, 100], 'm': [50, 10, 150, 110], 'b': [70, 10, 200, 150]}
            if shape == 't':
                t_coords = tc[size]
            elif shape == 'r':
                r_coords = rc[size]
            elif shape == 'c':
                c_coords = cc[size]
            popup.destroy()


win = Tk()
b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
b_circle = Button(text="Коло", width=15, command=circle)
b_clear = Button(text="Очистити", width=15, command=clear)
t_settings = Button(text="Налаштування тексту", width=17, command=text_settings)
c_settings = Button(text="Налаштування кольору", width=18, command=choose_shape)
s_settings = Button(text="Налаштування розміру", width=18, command=size_setting)

canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)

t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0, 0, 0, 0)

b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_circle.grid(row=2, column=0)
b_clear.grid(row=3, column=0)
t_settings.grid(row=4, column=0)
c_settings.grid(row=5, column=0)
s_settings.grid(row=6, column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()
