import tkinter as tk


current_effect = 0

def set_up_advancer():
    count = 0
    border_effects = [
        tk.FLAT,
        tk.SUNKEN,
        tk.RAISED,
        tk.GROOVE,
        tk.RIDGE,
    ]
    def advancer():
        nonlocal count, border_effects
        print('advancing')
        effect = border_effects[count]
        frame_a.config(relief=effect, borderwidth=8)
        count = (count + 1) % len(border_effects)
        frame_a.pack()
        frame_b.pack(side = tk.LEFT, fill = tk.BOTH)

root = None
root = tk.Tk()
assert root != None

root.title = 'steves_dvd_database'
root.geometry('640x480')

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="\nSTEVES DVD DATABASE\n")
label_a.pack()

advance = set_up_advancer()
button_a = tk.Button(master=frame_a, text='Press Me', command=advance)
button_a.pack()

scrollbar = tk.Scrollbar(master=frame_b)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

mylist = tk.Listbox(frame_b, yscrollcommand = scrollbar.set)
for line in range(8):
   mylist.insert(tk.END, "This is line number " + str(line))
   
mylist.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = mylist.yview )

frame_a.pack()
frame_b.pack(side = tk.LEFT, fill = tk.BOTH)

root.mainloop()