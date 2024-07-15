from tkinter import *
root = Tk()
root.geometry('500x300')

def getvalse():
    print('Accepted')

Label(root, text = 'Python Registration form', font = 'ar 15 bold').grid(row=0, column=3)

name = Label(root, text='Name')
phone = Label(root, text='Phone')
gender = Label(root, text='Gender')
emergency = Label(root, text='Emergency')
payment = Label(root, text='Payment')

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry =  Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

checkbtn = Checkbutton(text = 'Remember me Subrat?', variable = checkvalue)
checkbtn.grid(row=6, column=3)

Button(text = 'Submit', command = getvalse).grid(row=7, column=3)


root.mainloop()



