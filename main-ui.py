import customtkinter as ctk
import tkintermapview
from tkinter import TclError

#Default appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Initialized default colors
default_dark = {
    "fg": "#242424",
    "button": "#1f538d",
    "hover": "#144870",
    "border": "#1f538d",
    "entry_fg": "#343638"
}

#Main window setup
main = ctk.CTk()
main.title("Shortest path comparison: Dijkstra vs Bellman-Ford")
main.geometry("1000x600")
main.resizable(False, False)
main.configure(fg_color=default_dark["fg"])

#Default font
try:
    default_font = ("Winky-Sans", 12, "bold")
except TclError:
    print("Warning: Winky Sans font not found. Using Helvetica instead.")
    default_font = ("Helvetica", 12, "bold")

#Entry fields with labels
entry_frame = ctk.CTkFrame(main, fg_color="transparent")
entry_frame.place(x=293, y=33)

entry = ctk.CTkEntry(entry_frame, 
                    placeholder_text="From Location",
                    width=440, 
                    height=40,
                    font=default_font,
                    border_color=default_dark["border"],
                    border_width=1)
entry.pack()

entry1 = ctk.CTkEntry(entry_frame,
                      placeholder_text="To Location",
                      width=440,
                      height=40,
                      font=default_font,
                      border_color=default_dark["border"],
                      border_width=1)
entry1.pack(pady=10)

def handle_theme(theme):
    #Store theme colors
    default_colors = {
        "Dark": {
            "fg": "#242424",
            "button": "#1f538d",
            "hover": "#144870",
            "border": "#1f538d",
            "entry_fg": "#343638",
            "text_border_width": 1
        },
        "Light": {
            "fg": "#ebebeb", 
            "button": "#3a7ebf",
            "hover": "#325882",
            "border": "#3a7ebf",
            "entry_fg": "#dbdbdb", 
            "text_border_width": 1
        },
        "Barbie": {
            "fg": "#f658b8", 
            "button": "#FF1493",
            "hover": "#FFB6C1",
            "border": "#FF1493",
            "entry_fg": "#FFE6F3", 
            "text_border_width": 2 
        }
    }
    
    colors = default_colors[theme]
    
    #Update appearance mode first
    if theme == "Barbie":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode(theme.lower())
    
    #Update all widget colors
    main.configure(fg_color=colors["fg"])
    map_frame.configure(fg_color=colors["entry_fg"])
    button_frame.configure(fg_color="transparent")
    entry_frame.configure(fg_color="transparent")
    map_container.configure(fg_color="transparent")
    
    #Update interactive elements
    theme_selector.configure(
        fg_color=colors["button"],
        button_color=colors["button"],
        button_hover_color=colors["hover"]
    )
    
    for widget in [entry, entry1]:
        widget.configure(
            fg_color=colors["entry_fg"],
            border_color=colors["border"],
            border_width=colors["text_border_width"]
        )
    
    for btn in [play_button, button, button1]:
        btn.configure(
            fg_color=colors["button"],
            hover_color=colors["hover"]
        )
    
    text.configure(
        fg_color=colors["entry_fg"],
        border_color=colors["border"],
        border_width=colors["text_border_width"]
    )

#Theme selector
theme_var = ctk.StringVar(value="Dark")
theme_selector = ctk.CTkOptionMenu(main,
                                 values=["Light", "Dark", "Barbie"],
                                 variable=theme_var,
                                 command=handle_theme,
                                 width=120,
                                 height=30,
                                 font=default_font)
theme_selector.place(x=16, y=15)

#Add variable to track selected algorithm
selected_algorithm = ctk.StringVar(value="none")

#Map viewer and play button layout - repositioned
map_container = ctk.CTkFrame(main, fg_color="transparent")
map_container.place(x=264, y=151)

#Play button on left side of map
play_button = ctk.CTkButton(
    main,
    text="▶",
    width=40,
    height=100,
    font=("Helvetica", 20, "bold"),
    state="disabled",
    fg_color=default_dark["button"],      
    hover_color=default_dark["hover"],    
    command=lambda: print(f"Running {selected_algorithm.get()} algorithm...")
)
play_button.place(x=203, y=151) # Positioned to the left of map

map_frame = ctk.CTkFrame(map_container, width=500, height=280)
map_frame.pack()
map_frame.pack_propagate(False)
map_viewer = tkintermapview.TkinterMapView(master=map_frame)
map_viewer.pack(fill="both", expand=True)

#Modern buttons with sidebar frame
button_frame = ctk.CTkFrame(main, fg_color="transparent")
button_frame.place(x=785, y=174)

def select_algorithm(algo_name):
    selected_algorithm.set(algo_name)
    play_button.configure(state="normal")
    
    #Current theme colors
    current_theme = theme_var.get()
    theme_colors = {
        "Dark": {"selected": "#1f538d", "unselected": ("gray75", "gray25")},
        "Light": {"selected": "#3a7ebf", "unselected": ("gray75", "gray25")},
        "Barbie": {"selected": "#FF1493", "unselected": "#f658b8"}
    }
    
    colors = theme_colors[current_theme]
    
    #Update button colors based on current theme
    button.configure(fg_color=colors["unselected"] if algo_name != "dijkstra" else colors["selected"])
    button1.configure(fg_color=colors["unselected"] if algo_name != "bellman-ford" else colors["selected"])

button = ctk.CTkButton(
    button_frame,
    text="Dijkstra's",
    width=150,
    height=40,
    font=default_font,
    command=lambda: select_algorithm("dijkstra")
)
button.pack()

button1 = ctk.CTkButton(
    button_frame,
    text="Bellman-Ford",
    width=150,
    height=40,
    font=default_font,
    command=lambda: select_algorithm("bellman-ford")
)
button1.pack(pady=10)

#Text area
text = ctk.CTkTextbox(main,
                      width=455,
                      height=120,
                      font=default_font,
                      border_color=default_dark["border"], 
                      border_width=1) 
text.place(x=287, y=452)

main.mainloop()