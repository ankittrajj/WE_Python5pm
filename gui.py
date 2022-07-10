from tkinter import *

window = Tk()

window.title('My first gui code')

def click():
    enter_text = text_entry.get()
    output.delete(0.0,END)
    try:
        define = my_dict[enter_text]
    except:
        define = "not available"
    output.insert(END,define)

# text entry

text_entry = Entry(window,width = 20,bg = 'white')
text_entry.grid(row=2,column=5,sticky=W)
# text box
output = Text(window,width=10,height=10,background='white')
output .grid(row=0,column=1,stick=W)

# text label
Label(window,text='Enter something useful!!',bg='red',fg='black',font='aerial 12 bold').grid(row=0,column=0,sticky=W)

# submit button

Button(window,text = 'Submit',width=5,command=click,bg = 'black',fg='white').grid(row=2,column=2,sticky=W)


my_dict = {
    'animal':['dogs','cats'],
    'bug':'some error in the code'
}

window.mainloop()


#wap to make a text label!!