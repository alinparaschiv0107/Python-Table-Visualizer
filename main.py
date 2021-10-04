# Imports
import tkinter as tk
import tksheet
import pandas as pd
from tkinter import filedialog

# Input a csv
root = tk.Tk()
root.title('Insert a csv file')
root.filename = filedialog.askopenfile(title="Select A File", filetypes = (("csv files","*.csv"),("all files","*.*")))
root.destroy()

# Read data from csv
df = pd.read_csv(root.filename.name, nrows= 10)
cols = list(df.columns)
vals = df.values.tolist()

# Visualization step
app = tk.Tk()
app.title("Table Visualizer")
app.resizable(height = None, width = None)
sheet = tksheet.Sheet(app,headers = cols)

sheet.grid()

sheet.set_sheet_data(data = vals,
               reset_col_positions = True,
               reset_row_positions = True,
               redraw = True,
               verify = True,
               reset_highlights = False
               )

sheet.enable_bindings(("single_select",
                       "drag_select",
                       "row_select",
                       "column_select",
                       "column_width_resize",
                       "arrowkeys",
                       "right_click_popup_menu",
                       "rc_select",
                       "rc_insert_row",
                       "rc_delete_row",
                       "rc_insert_column",
                       "rc_delete_column",
                       "copy",
                       "cut",
                       "paste",
                       "delete",
                       "undo",
                       "edit_cell"))

sheet.height_and_width(height = 500, width = 1000)
app.mainloop()