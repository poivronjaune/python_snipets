import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title: str, min_size: tuple):
        super().__init__()
        
        # Main setup
        self.title(title)
        self.iconbitmap('./img/PoivronJauneNewStyle.ico')
        self.geometry(f"{min_size[0]}x{min_size[1]}")     
        self.minsize(min_size[0], min_size[0])   
        
        # Create widgets
        self.menu = Menu(self)
        self.main = Main(self)
        
        # Run
        self.mainloop()        


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ttk.Label(self, background='red').pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()
        self.create_layout()
        
        
    def create_widgets(self):
        self.menu_button1 = ttk.Button(self, text='Button 1')
        self.menu_button2 = ttk.Button(self, text='Button 2')
        self.menu_button3 = ttk.Button(self, text='Button 3')
        
        self.menu_slider1 = ttk.Scale(self, orient='vertical')
        self.menu_slider2 = ttk.Scale(self, orient='vertical')
        
        self.toggle_frame = ttk.Frame(self)
        self.menu_toggle1 = ttk.Checkbutton(self.toggle_frame, text='check 1')
        self.menu_toggle2 = ttk.Checkbutton(self.toggle_frame, text='check 2')
        
        self.entry = ttk.Entry(self)
        
    def create_layout(self):
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        
        self.menu_button1.grid(row=0, column=0, sticky='nswe', columnspan=2)
        self.menu_button2.grid(row=0, column=2, sticky='nswe')
        self.menu_button3.grid(row=1, column=0, columnspan=3, sticky='nswe')
        
        self.menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
        self.menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)
        
        self.toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        self.menu_toggle1.pack(side='left', expand=True)
        self.menu_toggle2.pack(side='left', expand=True)
        
        self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')
        
class Main(ttk.Frame):
    def __init__(self, parent):        
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        Entry(self, 'Entry 1', 'Button 1', 'green')
        Entry(self, 'Entry 2', 'Button 2', 'blue')
        
class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)
        
        label = ttk.Label(self, text=label_text, background=label_background)
        button = ttk.Button(self, text=button_text)
        label.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both', pady=10)
        self.pack(side='left', expand=True, fill='both', padx=20, pady=20)    
            
        
if __name__ == '__main__':
    App('Class Based App', (600,600))