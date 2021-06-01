from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageEnhance
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
num = 1
# Functions


def watermarker():
    global num
    files = [(("image Files", ".png .jpg"), ("all files", "*.*"))]
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select A File",
                                            filetypes=files)
    for filename in filenames:

        image = Image.open(filename).convert("RGBA")
        txt = Image.new('RGBA', image.size, (255, 255, 255, 0))
        width, height = image.size
        font = ImageFont.truetype("impact.ttf", int(width/5))
        d = ImageDraw.Draw(txt)
        text = textbox.get(1.0)
        d.text((int(width/5), int(height/5)), text, fill=(255, 0, 0, 15), font=font)
        combined = Image.alpha_composite(image, txt)
        combined.save(f'images/watermark{num}.png')
        num += 1
    showinfo(title="Success", message="Find your watermarked Images in images directory! ")
# UI SETUP


window = Tk()
window.title("WaterMarker")
window.config(padx=50, pady=50)

test_canvas = Canvas(window)
test_frame = Frame(test_canvas)
vertical_scroll = Scrollbar(window)

label = Label(text="Write the text to be set as a watermark. and click the button to find images")
label.pack()

textbox = Text(width=15, height=1)
textbox.pack()

btn = Button(text="Find", command=watermarker)
btn.pack()

window.mainloop()
