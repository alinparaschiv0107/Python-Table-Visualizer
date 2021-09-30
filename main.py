import tkinter as tk

import tksheet

app = tk.Tk()

sheet = tksheet.Sheet(app)

sheet.grid()

sheet.set_sheet_data(data = [[]],
               reset_col_positions = True,
               reset_row_positions = True,
               redraw = True,
               verify = True,
               reset_highlights = False
               )

# table enable choices listed below:
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