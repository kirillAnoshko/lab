import tkinter as tk
import generator


class Game:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.cols = 51 
        self.rows = 27
        self.tile_size =
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(expand=True, fill='both')
        self.draw_maze()
        self.window.mainloop()

    def draw_maze(self) -> None:
        for row_idx, row in enumerate(self.rows):
            for col_idx, col in enumerate(self.cols):
                self.canvas.create_rectangle(
                    0, 0, 100, 100, fill='red'
                )   


Game()