from guizero import App, Box, Text, TextBox, PushButton, ButtonGroup, MenuBar, info, yesno, warn

# Define menu bar options and commands.
def File():
   info("info", "this is a guizero app")
    # ....

def About():
    yesno("title", "text")
    # ...

def Command():
    warn("title", "text")
    # ...

def Repeat():
    print('caca')
    # ...


# Create the GUI application.
appWidth = 1200
appHeight = 500
app = App(title="TEST", bg="#0eb200", width=appWidth, height=appHeight)
# Define menu bar options.
menubar = MenuBar(app, toplevel=["File", "About"],
                  options=[
                      [ ["View", File] ],
                      [ ["About", About] ]
                  ])
# Design the interface using the box widget.
top = Box(app, width="fill", height=appHeight / 2, align="top")
bottom = Box(app, width="fill", height=appHeight / 2, align="bottom")
left_interface = Box(top, width=appWidth / 2, align="left", layout="grid", border=True)
right_interface = Box(top, width=appWidth / 2, align="right")
b_left_interface = Box(bottom, width=appWidth / 2, align="left")
b_right_interface = Box(bottom, width=appWidth / 2, align="right")

# Left Interface
left_header = Text(left_interface, text="Right", color="#002699", size=20, grid=[0,0])
r_label = Text(left_interface, text="R :", color="#1a53ff", size=15, grid=[0,1])
r_input = TextBox(left_interface, grid=[1,1])
r_input.bg = "#ff5c33"
r_input.text_color = "#1a53ff"
g_label = Text(left_interface, text="G :", color="#1a53ff", size=15, grid=[0,2])
g_input = TextBox(left_interface, grid=[1,2])
g_input.bg = "#ff5c33"
g_input.text_color = "#1a53ff"
b_label = Text(left_interface, text="B :", color="#1a53ff", size=15, grid=[0,3])
b_input = TextBox(left_interface, grid=[1,3])
b_input.bg = "#ff5c33"
b_input.text_color = "#1a53ff"
adjust_button = PushButton(left_interface, grid=[2,4], width="20", text="Adjust", command=Command)
adjust_button.bg = "#002699"
adjust_button.text_color = "white"

# Right Interface
right_header = Text(right_interface, text="Left", color="#002699", size=20, align="top")
sensor_value = Text(right_interface, text="TEST", color="#002699", size=120)
status_text = Text(right_interface, text="Status: OK", color="green", size=15, align="bottom")
# Update the sensor value.
sensor_value.repeat(1000, Repeat)

# Bottom Left Interface
base_header = Text(b_left_interface, text="Bottom Left", color="#002699", size=20)
base_angle = ButtonGroup(b_left_interface, options=["0", "30", "45", "90", "135", "180"], selected="0", width=20, command=Command)
base_angle.text_size = 15
base_angle.text_color = "white"

# Bottom Right Interface
arm_header = Text(b_right_interface, text="Bottom Right", color="#002699", size=20)
arm_angle = ButtonGroup(b_right_interface, options=["0", "30", "45", "90", "135", "180"], selected="0", width=20, command=Command)
arm_angle.text_size = 15
arm_angle.text_color = "white"

# Start the loop.
app.display()
