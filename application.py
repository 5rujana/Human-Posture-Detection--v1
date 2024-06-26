import threading
from customtkinter import *
from pyglet import font
from PIL import Image
# variables
HEIGHT = 800
WIDTH = 800
FRAME_WIDTH = 750
FRAME_HEIGHT = 100
TEXT_FRAME_HEIGHT = 300
LIGHT_BLUE = "#C6DEF2"
BLUE = "#92BEE3"
DARK_BLUE = "#6AABD2"
font.add_file("Fonts/Bebas_Neue/BebasNeue-Regular.ttf")

desc_text = """1. Master Yoga Poses: Get real-time feedback on your yoga form to ensure proper alignment and maximize your practice.
2. Maintain Perfect Posture: Our model monitors your posture throughout the day, helping you stay upright and avoid slouching.
3. Level Up Your Gym Workouts: See your gym exercises graded in real-time, ensuring you perform them safely and effectively with proper form."""

# setting up the window

set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk(fg_color=BLUE)
app.geometry(f"{WIDTH}x{HEIGHT}")
app.title("Human Posture Detection")

# setting up the font
headerFont = CTkFont(family="Bebas Neue", size=50, weight="bold")
descFont = CTkFont(family="Bebas Neue", size=20)
buttonFont = CTkFont(family="Bebas Neue", size=25)

# setting up images
bgImage = Image.open("./images/MountainsECS.jpg")
background = CTkImage(light_image=bgImage,
                      dark_image=bgImage)

slouchImage = Image.open("./images/slouch.jpeg")
slouchImg = CTkImage(light_image=slouchImage,
                     dark_image=slouchImage)

yogaImage = Image.open("./images/yogaPose.jpg")
yogaImg = CTkImage(light_image=yogaImage,
                   dark_image=yogaImage)

gymImage = Image.open("./images/GymPose.jpg")
gymImg = CTkImage(light_image=gymImage,
                  dark_image=gymImage)


# functions

def button_clicked(num):
    print(f"Button {num} clicked")


def bg_resizer(e):
    if e.widget is app:
        i = CTkImage(bgImage, size=(e.width, e.height))
        bg_label.configure(text="", image=i)

# adding the background label
bg_label = CTkLabel(master=app, text="", image=background)
bg_label.place(relx=0, rely=0)


# setting up the frame

textFrame = CTkFrame(master=app, width=FRAME_WIDTH, height=TEXT_FRAME_HEIGHT, fg_color=DARK_BLUE)
textFrame.pack(expand=True)
textFrame.place(relx=0.5, rely=0.225, anchor=CENTER)

btnFrame1 = CTkFrame(master=app, width=FRAME_WIDTH, height=FRAME_HEIGHT, fg_color=LIGHT_BLUE)
btnFrame1.pack(expand=True)
btnFrame1.place(relx=0.5, rely=0.55, anchor=CENTER)

btnFrame2 = CTkFrame(master=app, width=FRAME_WIDTH, height=FRAME_HEIGHT, fg_color=BLUE)
btnFrame2.pack(expand=True)
btnFrame2.place(relx=0.5, rely=0.7, anchor=CENTER)

btnFrame3 = CTkFrame(master=app, width=FRAME_WIDTH, height=FRAME_HEIGHT, fg_color=DARK_BLUE)
btnFrame3.pack(expand=True)
btnFrame3.place(relx=0.5, rely=0.85, anchor=CENTER)


# adding the labels
heading = CTkLabel(master=textFrame, text="Human Posture Detection", font=headerFont, text_color="black")
heading.place(relx=0.5, rely=0.2, anchor=CENTER)

desc = CTkLabel(master=textFrame, text=desc_text, wraplength=FRAME_WIDTH - 50, font=descFont, justify="left")
desc.place(relx=0.5, rely=0.6, anchor=CENTER)

def runslouch():
    s.main()
def runyoga():
    y.main()
def rungym():
    g.main()
# adding the buttons and their backgrounds
slouchImg.configure(size=(FRAME_WIDTH, FRAME_HEIGHT + 200))
bgLabel1 = CTkLabel(master=btnFrame1, text="", image=slouchImg)
bgLabel1.place(relx=0.5, rely=1.4, anchor=CENTER)
button1 = CTkButton(master=btnFrame1, text="Posture Detection", font=buttonFont, text_color="black", fg_color=LIGHT_BLUE, command = m.slouch, hover_color=DARK_BLUE)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)

yogaImg.configure(size=(FRAME_WIDTH, FRAME_HEIGHT + 400))
bgLabel2 = CTkLabel(master=btnFrame2, text="", image=yogaImg)
bgLabel2.place(relx=0.5, rely=1, anchor=CENTER)
button2 = CTkButton(master=btnFrame2, text="Yoga Pose Detection", font=buttonFont, text_color="black", fg_color=LIGHT_BLUE, command=m.yogapose, hover_color=DARK_BLUE)
button2.place(relx=0.5, rely=0.5, anchor=CENTER)

gymImg.configure(size=(FRAME_WIDTH, FRAME_HEIGHT + 200))
bgLabel3 = CTkLabel(master=btnFrame3, text="", image=gymImg)
bgLabel3.place(relx=0.5, rely=0.5, anchor=CENTER)
button3 = CTkButton(master=btnFrame3, text="Gym Pose Detection", font=buttonFont,text_color="black", fg_color=LIGHT_BLUE, command=m.gympose, hover_color=DARK_BLUE)
button3.place(relx=0.5, rely=0.5, anchor=CENTER)

if __name__ == "__main__":
    app.bind("<Configure>", bg_resizer)
    app.mainloop()