#txtParserGUI
#python 3.10.12

import customtkinter





def button_function():    
    t = entry1.get()
    txt = f"{t}.txt"
    txt2 = f"{t}_parsed.txt"
    # Read contents of file
    with open(txt, 'r') as f:
        textFile = f.read()

    # Replace the target string
    textFile = textFile.replace('. ', '\n')
    textFile1 = textFile.replace('\n', '. ')

    # Write to the new file
    with open(txt2, 'w') as f:
        f.write(textFile1)





app = customtkinter.CTk()
app.geometry("600x200")
app.title("Text Parser")


# Build frame for window to look better
frame1 = customtkinter.CTkFrame(master = app)
frame1.pack(pady=10, padx=15, expand=True)

#Create place for inputs
entry1 = customtkinter.CTkEntry(master=frame1, width=200, placeholder_text="Enter the file path here...", )
entry1.pack(padx=25, pady=10)

#create a button to engage entry field
button1 = customtkinter.CTkButton(master=frame1, text="Enter", command=button_function)
button1.pack(padx=25, pady=10)


app.mainloop()