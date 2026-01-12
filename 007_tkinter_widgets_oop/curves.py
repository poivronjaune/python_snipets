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
        self.canvas = Canvas(self, 500, 500)
        
        # Run
        self.mainloop()     

class Canvas(ttk.Frame):
    def __init__(self, parent, width, height):
        super().__init__(parent)

        self.width = width
        self.height = height        
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        
        # Draw coordinate axes for reference
        self.center_x, self.center_y = self.width // 2, self.height // 2  
        self.canvas.create_line(0, self.center_y, width, self.center_y, fill="gray") # X-axis
        self.canvas.create_line(self.center_x, 0, self.center_x, height, fill="gray") # Y-axis

        self.draw_parabola(0, 0, 20, 'red')        
        self.draw_parabola(0, 0, 100, 'blue')        
        
        self.pack(side='left', expand=True, fill='both', padx=20, pady=20)

    def draw_parabola(self, offset_x, offset_y, scale_factor, color):
        # Parabola Parameters
        scale = scale_factor  # Scale factor to make the curve visible
        points = []
        # Calculate points for x from -20 to 20
        for x in range(-20, 21):
            y = x**2  # The parabola function
            
            # Transform math coordinates to screen coordinates
            # Screen X = center + (math x * scale)
            # Screen Y = center - (math y * scale) (subtraction inverts the Y-axis)
            screen_x = self.center_x + (x * scale) + offset_x
            screen_y = self.center_y - (y * scale) - offset_y
            
            points.append((screen_x, screen_y))

        # create_line can take a flattened list of points to draw a connected line
        self.canvas.create_line(points, fill=color, width=2, smooth=True)        
        
if __name__ == "__main__":
    App('Curves', (600,600))        
    