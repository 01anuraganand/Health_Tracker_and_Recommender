from tkinter import *
import tkinter
from tkinter import messagebox
import datetime
root=Tk(className=" Health Tracker and Recommender")
root.iconbitmap('images/medical.ico')
root.geometry("1080x720")

#Function of menu bar command
#->>>Creating  About us Function of menu bar
def menu_about():
    response=messagebox.showinfo("About us","Developed by : Anurag Anand(11901877), Sushant Kumar(11902398), Pabitra Panda(11903542) \nContact us:  \nE-mail: track.health@gmail.com \nPhone: +91 1800125690  \nGet more info at www.TrackHealth.org")

def menu_new_file():
    for widget in panel_2.winfo_children():
       widget.destroy()
    check_button=Button(panel_2,text="Click here to Enter your Information",bg="white",padx=10,pady=10,command=m_window)
    check_button.pack(anchor=CENTER,pady=10)
    
def submit_fn():
    messagebox.askokcancel("askokcancel", "Want to continue?") 
    
#creating Frame root
frame_root=LabelFrame(root,bg="white")
frame_root.pack()

#creating Whole Window pane 
panel_1=PanedWindow(relief="raised")
panel_1.pack(fill=BOTH,expand=True)

#Creating Left Pane screen

left_label=Frame(panel_1,width=100)
panel_1.add(left_label)

#Creating Right and centered Pane

panel_2=Frame(panel_1,relief=FLAT,bg="white")
panel_1.add(panel_2)




#Creatoin of Main Window

def m_window():
    for widget in panel_2.winfo_children():
       widget.destroy()
    
    x = datetime.datetime.now()
    Label(panel_2,text="\nEnter your Bio Data...",font=30,bg="white").pack(anchor=N)
    Label(panel_2, text="\nTime:",bg="white").pack(anchor=NE)
    Label(panel_2, text=x,bg="white").pack(anchor=NE)
    
    Label(panel_2, text="\nFirst Name:",bg="white").pack()
    f_name=Entry(panel_2,border=5,width=30)
    f_name.pack()
    Label(panel_2, text="Last Name:",bg="white").pack()
    l_name=Entry(panel_2,border=5,width=30)
    l_name.pack()
    
    var=IntVar()
    male=Radiobutton(panel_2,text="Male",bg="white",variable=var,value=True,command=None)
    male.pack()
    female=Radiobutton(panel_2,text="Female",bg="white",variable=var,value=False,command=None)
    female.pack()
    
    Label(panel_2, text="Age:",bg="white").pack()
    age=Entry(panel_2,border=5,width=30)
    age.pack()
    Label(panel_2, text="Address:",bg="white").pack()
    address=Entry(panel_2,border=5,width=30)
    address.pack()
    Label(panel_2, text="Contact No:",bg="white").pack()
    contact=Entry(panel_2,border=5,width=30)
    contact.pack()
    #submit button
    submit_button=Button(panel_2,text="Submit",relief=RAISED,padx=30,pady=10,font="Algerian",bg="white",command=submit_fn)
    submit_button.pack()
    #check yourself button
    check_button=Button(panel_2,text=" Check Yourself",relief=RAISED,bg="white",padx=30,pady=10,font="Algerian",command=check_health_alloption)
    check_button.pack()

m_window_canvas=Canvas(panel_2,height=600,width=500,bg="white",relief=RAISED)
m_window_canvas.pack(expand=YES,fill=BOTH,side="left")
gig=PhotoImage(file='images/apple_.gif')
button1=Button(m_window_canvas,text="Click here to Enter your Information",bg="#3FEBD8",font=8,relief="raised",padx=5,pady=5,command=m_window)
button1.pack(side="right",pady=10)
m_window_canvas.create_image(300,300,image=gig)



# Check Yourself Button Command
def check_health():
    #BMI calculation function
    a=float(height.get())
    b=float(weight.get())
    c=float(a * b)
    bmi = b/(a*a) 
    Label(check_health_canvas,text ="Generated Report\n",font=20,bg="white").pack(side="top")
    Label2=Label(check_health_canvas)
    if ( bmi < 16):
        Label2.configure(text = "\nPhysical Status: Severely Underweight",font=18,bg="white")

    elif ( bmi >= 16 and bmi < 18.5):
        Label2.configure(text ="\nPhysical Status: Underweight",font=18,bg="white")

    elif ( bmi >= 18.5 and bmi < 25):
        Label2.configure(text ="\nPhysical Status: Healthy",font=18,bg="white")

    elif ( bmi >= 25 and bmi < 30):
        Label2.configure(text = "\nPhysical Status: Overweight",font=18,bg="white")

    elif ( bmi >=30):
        Label2.configure(text ="\nPhysical Status:Severely Overweight",font=18,bg="white")

    Label1=Label(check_health_canvas)
    b=('BMI Index')
    a=(b,bmi)
    Label1.configure(text = a,font=18,bg="white")
    Label1.pack(anchor=NW)
    Label2.pack(anchor=NW)
    
    #Sugar Level Calculation function
    sugar=int(sugar_level.get())
    Label1=Label(check_health_canvas)
    if sugar>100:
          Label1.configure(text="\nSugar Level : High.",font=18,bg="white")
    elif sugar<60:
        Label1.configure(text="\nSugar Level : Low.",font=18,bg="white")
    else:
        Label1.configure(text="\nSugar Level : Fine.",font=18,bg="white")
    Label1.pack(anchor=NW)
   
    #Blood Pressure Level calculation function
    #->>>>>Global check health function for Blood Pressure
    bpl_Label=Label(check_health_canvas)
    def low_bp(up,down):
            bpl_Label.configure(text="\nyou are facing LOW blood pressure",font=18,bg="white")
            bpl_Label.pack(anchor=NW)
            
    bpn_Label=Label(check_health_canvas)
    def normal_bp(up,down):
                bpn_Label.configure(text="\nEnjoy you life",font=18,bg="white")
                bpn_Label.pack(anchor=NW)
                
               
    def high_bp(up,down):
                bp_high=up
                bp_low=down
                bph_Label=Label(check_health_canvas)
                
                if((int(bp_high)<130 and int(bp_high)>=120 )and int(bp_low)<=80):
                    bph_Label.configure(text="\nyou area in PREHYPERTENTION STAGE",font=18,bg="white")
                elif((int(bp_high)<140 and int(bp_high)>=130) and int(bp_low)<90):
                    bph_Label.configure(text="\nYou are in HYPERTENTION STAGE 1",font=18,bg="white")
                elif((int(bp_high)<180 and int(bp_high)>=140) and int(bp_low)<120):
                    bph_Label.configure(text="\nYou are in HYPERTENTION STAGE 2",font=18,bg="white")
                else:
                    bph_Label.configure(text="\nYou are in HYPERTENSIVE CRISIS(Final stage of HYPERTENTIOIN",font=18,bg="white")
                bph_Label.pack(anchor=NW)
                    
    # main BP caller function
    global up
    up=int(bp_high.get())
    global down
    down =int(bp_low.get())
    bp_Label=Label(check_health_canvas)
    if(up<90 and up>=40 and down<60 and down>=40):
        low_bp(up,down)
            
    elif(up<120 and up>=90 and down<80):
        normal_bp(up,down)
            
    elif(up>=120 and down>=80):
        high_bp(up,down)            
    else:
        bp_Label.configure(text="\nPlease enter a valid blood pressure",font=18,bg="white")
        bp_Label.pack(anchor=NW)
    
#->>Entry in check yourself
#check_health_alloption

def check_health_alloption():
    for widget in panel_2.winfo_children():
       widget.destroy()
    
    Label(panel_2,text="Track your Health Status...",font=("Algerian",20),bg="white").pack(anchor=N)
    
    #canvas inside panel_2 for report generatioin
    global check_health_canvas
    check_health_canvas=Canvas(panel_2,bg="white",width=500,height=400)
    check_health_canvas.pack(fill=BOTH,side="right")
    
    #BMI
    global height
    Label(panel_2,text="BMI Calulator",font=18,bg="white").pack(anchor=NW)
    Label(panel_2, text="\nHeight (metre):",bg="white").pack(anchor=NW)
    height = Entry(panel_2,border=5,width=30)
    height.pack(anchor=NW)            
    global weight
    Label(panel_2, text="Weight (Kg):",bg="white").pack(anchor=NW)
    weight =Entry(panel_2,border=5,width=30)
    weight.pack(anchor=NW) 
    
    #Sugar Level
    
    global sugar_level
    Label(panel_2,text="\nSugar Level Calulator",font=18,bg="white").pack(anchor=NW)
    Label(panel_2, text="\nSugar Level:",bg="white").pack(anchor=NW)
    sugar_level=Entry(panel_2,border=5,width=30)
    sugar_level.pack(anchor=NW)
    
    #Blood Pressure
 
    global bp_high
  
    Label(panel_2,text="\nBlood Pressure Calulator",font=18,bg="white").pack(anchor=NW)
    Label(panel_2,text="\nBP(Upper):",bg="white").pack(anchor=NW)
    bp_high=Entry(panel_2,border=5,width=30)
    bp_high.pack(anchor=NW)
    global bp_low
    Label(panel_2,text="BP(Lower)",bg="white").pack(anchor=NW)
    bp_low=Entry(panel_2,border=5,width=30)
    bp_low.pack(anchor=NW)
    
    
    #Repport Generate button
    button1=Button(panel_2,text="Generate report",bg="#3FEBD8",padx=10,pady=10,command=check_health)
    button1.pack(anchor=SW,pady=10)

#other_disease_contents
def other_diseases():
        for widget in cnvs.winfo_children():
            widget.destroy()
        Label3=Label(cnvs,text='',bg="white",font=40)
        Label3.pack(pady=20)
        temp=sp.get()
        if(temp=='Dengue'):
                Label3.configure(text="***Dengue home treatment***\n\n1.Papaya Leaf Juice\n2.Goat Milk\n3.Giloy Juice\n4.Guava Juice\n5.Apple Juice\n6.Neem Leaves\n7.Kiwi Juice\n8.Vitamin K\n9.Turmeric\n10.Tulsi Leaves")
        elif(temp=="Malaria"):
                Label3.configure(text="***Malaria home treatment***\n\n1.Orange Juice\n2.Ginger\n3.Lime or lemon Juice\n4.Holy Basil\n5.Warm Water\n6.Grapeffruit Juice\n7.Berries")
        elif(temp=="Corona"):
                Label3.configure(text="***Corona home treatment***\n\n1.Warm water\n2.Giloy\n3.Tulsi(Basil)\n4.Turmeric powder\n5.Vitamin C rich foods(Kiwi,orange,papaya...)")
        elif(temp=="Typhoid"):
                Label3.configure(text="***Typhoid home treatment***\n\n1.Drink lots of fluids\n2.Garlic\n3. Basil\n4.Apple cider vinegar\n5.Cold compress")
        elif(temp=="Common Cold"):
                Label3.configure(text="***Common Cold home treatment***\n\n1.Garlic\n2.Raw Honey\n3.Ginger\n4.Chicken Soup\n5. Red Onion\n6.Black Pepper\n7.Turmeric Milk")
        else:
                Label3.configure(text="***Allergies home treatment***\n\n1.Use HEPA filters\n2.Butterbur\n3.papaya and pineapple\n4.Honey\n5.Vitamin C")
               
    
#Button2   command
def health_recom_fn():
    for widget in panel_2.winfo_children():
        widget.destroy()
   
    panel_2.pack_forget()
    
    w = Label(panel_2, text ='Choose Diseases', font = "50",bg="white")  
    w.pack(pady=20) 
    
    
    global sp
    sp = Spinbox(panel_2,values=("Dengue","Malaria","Corona","Typhoid","Common Cold","Allergies"),bg="white",fg="Black",font=30) 
    
    sp.pack()
    #calling other_diceases function
    disease_compute=Button(panel_2,text="Check",border=1,relief="raised",bg="white",font=20,command=other_diseases)
    disease_compute.pack(pady=20)
    global cnvs
    cnvs=Canvas(panel_2,width=0,height=0,bg="white")
    cnvs.pack(expand=YES,fill=BOTH,padx=20)
    
    
 
    
#Creating Menu Bar:
menu_bar=Menu(root)
root.config(menu=menu_bar)

#creating File Menu
file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New File",command=menu_new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)

#creating View Menu
view_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="View",menu=view_menu)
view_menu.add_command(label="Enter your Info",command=m_window)
view_menu.add_separator()
view_menu.add_command(label="Check Yourself",command=check_health_alloption)
view_menu.add_command(label="Health Recommender",command=health_recom_fn)

#creating Help Menu
help_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="New...",command=None)
help_menu.add_separator()
help_menu.add_command(label="About us",command= menu_about)

    
    #Adding Logo to Left Pane
canvas=Canvas(left_label,width=0,height=0)
canvas.pack(expand=YES,fill=BOTH,padx=20)
gig1=PhotoImage(file='images/Logo.gif')
canvas.create_image(100,150,image=gig1)

#Adding Button to Left Pane

redbutton=Button(left_label,text=" Check Yourself",relief=RAISED,padx=45,pady=70,font="Algerian",command=check_health_alloption)
redbutton.pack()

button=Button(left_label,text="Health Recommender",relief=RAISED,padx=20,pady=70,font="Algerian",command=health_recom_fn)
button.pack()


root.resizable(False,False)
root.mainloop()
