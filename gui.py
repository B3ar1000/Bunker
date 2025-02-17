import customtkinter as ctk

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")

x=900

y=600

root = ctk.CTk()
root.geometry(f"{int(x)}x{int(y)}")


def resize_window(x,y):
    root.geometry(f"{int(x)}x{int(y)}")

def show_frame(frame):
    frame.tkraise()

frame1 = ctk.CTkFrame(root)
frame1.grid(row=0, column=0, sticky="nsew")

# Configure the window's grid
frame1.grid_rowconfigure(0, weight=1, minsize=x)  # Adjust row height
frame1.grid_columnconfigure(0, weight=1, minsize=y)  # Adjust column width

# Create a grid with y rows and x columns inside the frame
def grid(frame,x,y):
    for col in range(x):
        frame.grid_columnconfigure(col, weight=1, minsize=100)
    for row in range(y):
        frame.grid_rowconfigure(row, weight=1, minsize=100)


# Create a grid with x rows and y columns inside the frame1
grid(frame1, x//100,y//100)

frame2 = ctk.CTkFrame(root)
frame2.grid(row=0, column=0, sticky="nsew")



label = ctk.CTkLabel(frame1, text="Bunker", font=("Roboto", 36))
label.grid(row=0, column=4)

game_button = ctk.CTkButton(frame1, text = "Start Game", fg_color="green", width=200, height=48, command=lambda: show_frame(frame2))
game_button.grid(row=1, column = 3, columnspan=3, rowspan=1)

exit_button = ctk.CTkButton(frame1, text = "Exit", fg_color="red", width=100, height=24)
exit_button.grid(row=5, column=4)

show_frame(frame1)

grid(frame2, x//100,y//100)


def disable_a_widget(widget):
    widget.configure(state="disabled")

def enable_a_widget(widget):
    widget.configure(state="normal")

def toggle_widget_state(switch, widget):
    if switch.get() == 1:  # If switch is "on"
        enable_a_widget(widget)  # Enable the widget
    else:
        disable_a_widget(widget)  # Disable the widget



label = ctk.CTkLabel(frame2, text="Bunker", font=("Roboto", 36))
label.grid(row=0, column=4)

# # #User Entries # # #

label = ctk.CTkLabel(frame2, text="Bunker Name", font=("Roboto", 24))
label.grid(row=1, column=1, sticky="n", columnspan=2, rowspan=1)

Bunker_name = ctk.CTkEntry(frame2, placeholder_text="Your Bunker Name")
Bunker_name.grid(row=1, column=1, columnspan=2, rowspan=1)

label = ctk.CTkLabel(frame2, text="Number of Players", font=("Roboto", 24))
label.grid(row=1, column=3, sticky="n", columnspan=2, rowspan=1)

N_of_players = ctk.CTkEntry(frame2, placeholder_text="Number of Players")
N_of_players.grid(row=1, column=3, columnspan=2, rowspan=1)

# # # User Checkboxes # # #


raid_option_checkbox = ctk.CTkCheckBox(frame2, text="Turn on Raids")
raid_option_checkbox.grid(row=1, column=6, sticky="n")

obstacle_option_checkbox = ctk.CTkCheckBox(frame2, text="Turn on Obstacles")
obstacle_option_checkbox.grid(row=1, column=6)

# # # Age limit gui # # #


age_limit_option_switch = ctk.CTkSwitch(frame2, text="Set Limit Age", command=lambda: toggle_widget_state(age_limit_option_switch, age_limit_slider))
age_limit_option_switch.grid(row=1, column=6, sticky="s")

age_label = ctk.CTkLabel(frame2, text="Age Limit: 49", font=("Roboto", 16), state="disabled")
age_label.grid(row=2, column=6, sticky="n", pady=10)  # Position above the slider with padding

def update_label(label, value):
    label.configure(text=f"Age Limit: {int(float(value))}")  # Update label with slider value

age_limit_slider = ctk.CTkSlider(frame2, from_=49, to=80, state="disabled", command=lambda value: update_label(age_label, value))
age_limit_slider.grid(row=2, column=6)

# # # Difficulty gui # # #

difficulty_option_switch = ctk.CTkSwitch(
    frame2, text="Preset Difficulty", command=lambda: toggle_widget_state(difficulty_option_switch, difficulty_menu))

difficulty_option_switch.grid(row=3, column=6, sticky="s")

difficulty_menu = ctk.CTkOptionMenu(frame2, values=["Easy", "Medium", "Hard"])
difficulty_menu.grid(row=4, column=6, sticky="n", pady=10)



#defualt values
age_limit_slider.configure(state="disabled")
difficulty_menu.configure(state="disabled")
final_age_limit = 80 


exit_button = ctk.CTkButton(frame2, text = "Back", fg_color="red", width=100, height=24, command=lambda: show_frame(frame1))
exit_button.grid(row=5, column=4)



root.mainloop()