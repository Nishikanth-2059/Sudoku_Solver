import tkinter as tk

# Constants
ROWS = 9
COLS = 9
CELL_WIDTH = 5
CELL_HEIGHT = 2  # Increased cell height
BORDER_WIDTH = 1
THICK_BORDER_WIDTH = 3

class TableApp:
    N = 9
    def __init__(self, root):
        self.root = root
        self.root.title("Table of Values")

        self.entries = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.create_table(0)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_table)
        self.submit_button.grid(row=ROWS + 1, columnspan=COLS, sticky="we")

        


    def create_table(self, flag):
        for row in range(ROWS):
            for col in range(COLS):
                # Determine border thickness
                left_border = THICK_BORDER_WIDTH if col % 3 == 0 else BORDER_WIDTH
                top_border = THICK_BORDER_WIDTH if row % 3 == 0 else BORDER_WIDTH
                right_border = THICK_BORDER_WIDTH if (col + 1) % 3 == 0 else BORDER_WIDTH
                bottom_border = THICK_BORDER_WIDTH if (row + 1) % 3 == 0 else BORDER_WIDTH
                
                # Create a frame to hold the entry with a border
                frame = tk.Frame(self.root, borderwidth=0)
                frame.grid(row=row, column=col, rowspan=1, columnspan=1, sticky="nsew")

                # Create the entry widget inside the frame
                entry = tk.Entry(frame, width=CELL_WIDTH, bd=0, justify="center", font = ('Arial', 15))
                entry.pack(padx=(left_border, right_border), pady=(top_border, bottom_border), ipadx=5, ipady=10)  # Increased padding
                entry.config(highlightthickness=1, highlightbackground="black")
                if flag == 1:
                    entry.insert(0, self.table[row][col])
                self.entries[row][col] = entry

    def convert(self, s):
        return [[int(cell) if cell else 0 for cell in row] for row in s]
    
    def isValid(self, grid, row, col, num):
        for i in range(9):
            if(grid[row][i]==num):
                return False
        for i in range(9):
            if(grid[i][col]==num):
                return False
        srow = row - row%3
        scol = col - col%3
        for i in range(3):
            for j in range(3):
                if(grid[srow+i][scol+j]==num):
                    return False
        return True
            
    def solve(self, grid, row, col):
        if col == self.N-1:
            nrow = row+1
            ncol = 0
        else:
            nrow = row
            ncol = col+1
            
        if row== self.N-1 and col == self.N-1:
            return True
        for i in range(9):
            for j in range(9):
                if grid[i][j]==0:
                    for k in range(1, 10):
                        if(self.isValid(grid, i, j, k)):
                            grid[i][j] = k
                            if(self.solve(grid, nrow, ncol)):
                                return True
                            grid[i][j] = 0
                    return False
        return True

    def submit_table(self):
        s_table = [[self.entries[row][col].get() for col in range(COLS)] for row in range(ROWS)]
        self.table = self.convert(s_table)
        btemp = self.solve(self.table, 0, 0)
        print(btemp)
        if btemp:
            self.create_table(1)
            print(btemp)
        else:
            print("No solution found")

if __name__ == "__main__":
    root = tk.Tk()
    app = TableApp(root)
    root.mainloop()
    