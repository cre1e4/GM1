from PIL import ImageTk, Image
import tkinter as tk
import urllib
import webbrowser
import datetime
url= 'https://www.netflix.com/browse?jbv=70178217'

a = 1
b = 1.2
index = 0

label_width = 0
label_height = 0
select_index = 0
reached_left_end = 0
reached_right_end = 0
scroll_index = 1




def resize_image(event):

    global label_width
    global label_height
    global new_width1
    global new_height1
    
    new_width = int(event.width)
    new_height = int(event.height)
    
    # Resize the original image to fit the new dimensions
    resized_image = image1.resize((new_width, new_height))
    
    # Update the PhotoImage
    image_display = ImageTk.PhotoImage(resized_image)
    background.config(image=image_display)
    background.image = image_display  # Keep a reference to avoid garbage collection

    new_width = int(event.width * 1)
    new_height = int(event.height * 0.3)

    new_width1 = int(event.width * 0.2)
    new_height1 = int(event.height * 0.135)

    new_width2 = int(event.width * 0.2 * 1.2)
    new_height2 = int(event.height * 0.135 * 1.2)

    
    
    # Resize all images
    resized_image = image2.resize((new_width, new_height))
    image_display = ImageTk.PhotoImage(resized_image)
    overlay_label.config(image=image_display)
    overlay_label.image = image_display  

    # Resize Labels

    
    label_width = int(event.width*0.025)
    label_height = int(event.height*0.01)

    resized_image = image3.resize((new_width1, new_height1))
    image_display = ImageTk.PhotoImage(resized_image)

    image_display = ImageTk.PhotoImage(resized_image)
    label4.config(image=image_display)
    label4.image = image_display

    resized_image = image4.resize((new_width1, new_height1))
    image_display = ImageTk.PhotoImage(resized_image)

    image_display = ImageTk.PhotoImage(resized_image)
    label5.config(image=image_display)
    label5.image = image_display  

    resized_image = image5.resize((new_width1, new_height1))
    image_display = ImageTk.PhotoImage(resized_image)

    image_display = ImageTk.PhotoImage(resized_image)
    label6.config(image=image_display)
    label6.image = image_display

    resized_image = image6.resize((new_width1, new_height1))
    image_display = ImageTk.PhotoImage(resized_image)

    image_display = ImageTk.PhotoImage(resized_image)
    label7.config(image=image_display)
    label7.image = image_display  


def Open(event):
    webbrowser.open_new_tab(url)

def Scroll_left(event):
    global index
    global a
    global new_width1
    global new_height1
    a = 1.2
    b = 0.8
    index = index - 1
    print("right")
    print(index)

    new_width_1 = int(new_width1*a)
    new_height_1 = int(new_height1*a)

    new_width_2 = int(new_width1*b)
    new_height_2 = int(new_height1*b)

    if index == 1:
        resized_image = image3.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
        resized_image = image4.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label5.image = image_display
        resized_image = image5.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
        resized_image = image6.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display  
    elif index == 2:
        resized_image = image4.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label5.image = image_display
        resized_image = image5.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
    elif index == 3:
        resized_image = image5.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
        resized_image = image6.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display
    elif index == 4:
        resized_image = image6.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display
        resized_image = image6.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
    elif index == -1:
        resized_image = image6.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display
        resized_image = image7.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
        index = 4
    else:
        resized_image = image5.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
        resized_image = image4.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label6.image = image_display
        resized_image = image3.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
        resized_image = image6.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display
        index = 0


def Scroll_right(event):
    global index
    global a
    global new_width1
    global new_height1
    a = 1.2
    b = 0.8
    index = index + 1
    print("right")
    print(index)

    new_width_1 = int(new_width1*a)
    new_height_1 = int(new_height1*a)

    new_width_2 = int(new_width1*b)
    new_height_2 = int(new_height1*b)

    if index == 1:
        resized_image = image3.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
        resized_image = image4.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label5.image = image_display
        resized_image = image5.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
        resized_image = image6.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display  
    elif index == 2:
        resized_image = image4.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label5.image = image_display
        resized_image = image3.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
    elif index == 3:
        resized_image = image5.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
        resized_image = image4.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label5.image = image_display
    elif index == 4:
        resized_image = image6.resize((new_width_1, new_height_1))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display
        resized_image = image5.resize((new_width_2, new_height_2))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
    else:
        resized_image = image5.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label6.config(image=image_display)
        label6.image = image_display
        resized_image = image4.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label5.config(image=image_display)
        label5.image = image_display
        resized_image = image3.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label4.config(image=image_display)
        label4.image = image_display
        resized_image = image6.resize((new_width1, new_height1))
        image_display = ImageTk.PhotoImage(resized_image)
        label7.config(image=image_display)
        label7.image = image_display
        index = -1
        index = 0

    


    


    
events = []
root = tk.Tk()
root.title("Resizable Image in Tkinter")
root.geometry("800x600")

# Create a photoimage object of the image in the path
image1 = Image.open("C:/Users/Chris/Downloads/grey-white.png")
image2 = Image.open("C:/Users/Chris/Downloads/background.jpg")
image3 = Image.open("C:/Users/Chris/Downloads/thecrown.jpg")
image4 = Image.open("C:/Users/Chris/Downloads/houseofcards.png")
image5 = Image.open("C:/Users/Chris/Downloads/BBC.jpg")
image6 = Image.open("C:/Users/Chris/Downloads/Photos.png")
DisplayImage = ImageTk.PhotoImage(image1)
DisplayImage2 = ImageTk.PhotoImage(image2)
DisplayImage3 = ImageTk.PhotoImage(image3)
DisplayImage4 = ImageTk.PhotoImage(image4)
DisplayImage5 = ImageTk.PhotoImage(image5)
DisplayImage6 = ImageTk.PhotoImage(image6)
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)


background = tk.Label(frame, image=DisplayImage)
background.pack(fill=tk.BOTH, expand=True)


overlay_label = tk.Label(frame, image=DisplayImage2)
overlay_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)




label4 = tk.Label(frame, image=DisplayImage3)
label4.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

label5 = tk.Label(frame, image=DisplayImage4)
label5.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

label6 = tk.Label(frame, image=DisplayImage5)
label6.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

label7 = tk.Label(frame, image=DisplayImage6)
label7.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

label8 = tk.Label(frame, text="09:21 Thursday 30/05/2024", bg="black", fg="white", width=30, height=3,)
label8.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

label8.config(font=("Helvetica", 18, "bold"))


def update_time():
    global now
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    label8.config(text = time)
    root.after(1000, update_time)
    
    weekday_number = now.weekday()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_name = weekdays[weekday_number]
    stamp = (weekday_name, time)
    label8.config(text = stamp)


background.bind('<Configure>', resize_image)

def Scroll(event):
    global label_width
    global label_height
    
    a = 1.2
    enlarge_width = int(label_width*a)
    enlarge_height = int(label_height*a)
    label4.config(width=enlarge_width, height=enlarge_height)

    

root.bind("<Return>", Open)
root.bind("<Left>", Scroll_left)
root.bind("<Right>", Scroll_right)

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M: %S"))

root.after(1000, update_time)





root.mainloop()
