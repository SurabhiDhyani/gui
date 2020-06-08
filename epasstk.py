import epass_db

from tkinter import *

tk=Tk()
tk.geometry("600x300")
tk.title("E-pass Form")
def getvals():
    print('We have received your information regarding E-pass')

    print(f"{namevalue.get(), agevalue.get(), phonevalue.get(), identityvalue.get(), travel_historyvalue.get(),zonevalue.get(), sympvalue.get(), purposevalue.get()} ")

    epass_db.create_record(namevalue.get(), agevalue.get(), phonevalue.get(), identityvalue.get(), travel_historyvalue.get(), zonevalue.get(), sympvalue.get(),purposevalue.get(), 1)

    with open("e-pass records.txt", "a") as f:
        f.write(f"{namevalue.get(), agevalue.get(), phonevalue.get(), identityvalue.get(), travel_historyvalue.get(), zonevalue.get(), sympvalue.get(), purposevalue.get}\n ")


Label(tk, text="Please fill the details for e-pass").grid(row=0, column=3)

name=Label(tk,text='Name of the Applicant')
age=Label(tk,text='Enter your age')
phone=Label(tk,text='Phone number')
identity=Label(tk,text='Id you are using')
travel_history=Label(tk,text='Have you travelled to any foreign country recently?')
zone=Label(tk,text='Zone you are coming from')
symp=Label(tk,text='Are you having any symptoms regarding fever?')
purpose=Label(tk,text='Purpose of your travel')

name.grid(row=1,column=2)
age.grid(row=2,column=2)
phone.grid(row=3,column=2)
identity.grid(row=4,column=2)
travel_history.grid(row=5,column=2)
zone.grid(row=6,column=2)
symp.grid(row=7,column=2)
purpose.grid(row=8,column=2)

namevalue=StringVar()
agevalue=StringVar()
phonevalue=StringVar()
identityvalue=StringVar()
travel_historyvalue=StringVar()
zonevalue=StringVar()
sympvalue=StringVar()
purposevalue=StringVar()
submit_detvalue=IntVar()

nameentry=Entry(tk,textvariable=namevalue)
ageentry=Entry(tk,textvariable=agevalue)
phoneentry=Entry(tk,textvariable=phonevalue)
identityentry=Entry(tk,textvariable=identityvalue)
travel_historyentry=Entry(tk,textvariable=travel_historyvalue)
zoneentry=Entry(tk,textvariable=zonevalue)
sympentry=Entry(tk,textvariable=sympvalue)
purposeentry=Entry(tk,textvariable=purposevalue)

nameentry.grid(row=1,column=3)
ageentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
identityentry.grid(row=4,column=3)
travel_historyentry.grid(row=5,column=3)
zoneentry.grid(row=6,column=3)
sympentry.grid(row=7,column=3)
purposeentry.grid(row=8,column=3)

submit_det=Checkbutton(text="Details submitted by me are true to my knowledge",variable=submit_detvalue)
submit_det.grid(row=9,column=3)

Button(text="Submit your details",command=getvals).grid(row=10,column=3)

tk.mainloop()
