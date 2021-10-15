from tkinter import *
import mysql.connector as con
db = con.connect(host = "localhost",user = "root",password ="",database = "hotel")
cur = db.cursor()
def bookARoom():
    roomBookw =  Toplevel(gui)
    roomBookw.configure(background = "Antique White")
    roomBookw.geometry("1366x768")
    w = Canvas(roomBookw,width = 4,height = 768,bg = "Antique White")
    w.place(x = 700 , y = 0)
    w.create_line(2,75,2,600,fill  ="red",dash = (4,4))
    Label(roomBookw,text = "Please Fill up following details",fg = "red",bg = "Antique White",font = "Rockwell 30").place(x = 400,y = 10)
    Label(roomBookw,text = "Details Regarding Person",fg = "red",bg = "Antique White",font = "Rockwell 22").place(x = 50,y = 100)
    Label(roomBookw,text = "Full Name:",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 150)
    Label(roomBookw,text = "Contact No.:",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 200)
    Label(roomBookw,text = "Email Id:",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 250)
    Label(roomBookw,text = "Address:",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 300)
    Label(roomBookw,text = "Date Of Birth:",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 350)
    Label(roomBookw,text = "ID:",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 400)
    e1 = Entry(roomBookw,width = 25)#name
    e1.place(x =250 , y = 160)
    e2 = Entry(roomBookw,width = 25)#ContactNo
    e2.place(x =250 , y = 210)
    e3 = Entry(roomBookw,width = 25)#email
    e3.place(x =250 , y = 260)
    e4 = Entry(roomBookw,width = 45)#Address
    e4.place(x =250 , y = 310)
    e5 = Entry(roomBookw,width = 25)#Dateofbirth
    e5.place(x =250 , y = 360)
    idvar = StringVar(roomBookw)
    idvar.set("Id")
    option = OptionMenu(roomBookw,idvar,"Aadhar Card","Pan Card","Driving Liscense","Voter ID Card","Freedom Fighter Card","Rashan Card")
    option.place(x = 250,y = 410)
    Label(roomBookw,text = "Check-In Date",fg = "Red",bg = "Antique White",font = "Georgia 20").place(x =50,y = 450)
    e6 = Entry(roomBookw,width = 25)
    e6.place(x = 250,y = 460)
    #Section 2
    Label(roomBookw,text = "Select Room",fg = "red",bg = "Antique White",font = "Rockwell 22").place(x = 800,y = 100)
    v = IntVar(roomBookw)
    Radiobutton(roomBookw,text = "Type A",fg = "Red",bg = "Antique White",font = "Rockwell 20",variable = v,value = 1).place(x = 800,y = 150)
    Radiobutton(roomBookw,text = "Type B",fg = "Red",bg = "Antique White",font = "Rockwell 20",variable = v,value = 2).place(x = 1000,y = 150)
    Label(roomBookw,text = "Price Rs. 1999",fg = "Red",bg ="Antique White",font = "Raleway 18").place(x = 800,y = 200)
    Label(roomBookw,text = "Price Rs. 2499",fg = "Red",bg ="Antique White",font = "Raleway 18").place(x = 1000,y = 200)
    
    #RoomBook
    def BookedRoom():
        name = str(e1.get())
        contact = str(e2.get())
        email = str(e3.get())
        add = str(e4.get())
        dob = str(e5.get())
        dcheck = str(e6.get())
        if len(name) == 0 or len(contact) == 0 or len(email) == 0 or len(add) == 0 or len(dob) == 0:
            Popup = Toplevel(roomBookw)
            Label(Popup,text = "Please Fill Up the Details").pack()
        elif len(contact) != 10:
            Popup = Toplevel(roomBookw)
            Label(Popup,text = "Please Enter a valid contact number").pack()
        elif "@" not in email:
            Popup = Toplevel(roomBookw)
            Label(Popup,text = "Please Enter a valid E-mail Address").pack()
        elif len(str(v.get())) == 0:
            Popup = Toplevel(roomBookw)
            Label(Popup,text = "Please Select Room Type").pack()
        else:    
            BookedRoomW = Toplevel(roomBookw)
            BookedRoomW.configure(background = "Antique White")
            BookedRoomW.geometry("600x400")
            RoomDict = {'101' : 1,'102': 1,'103': 2 ,'104' : 2,'105' : 1,'106':1}
            
            query = "SELECT ROOMNO FROM ROOMS WHERE ROOM_AVAILABLE = \'TRUE\'"
            string = ""
            cur.execute(query)
            for y in cur.fetchall():
                z = y[0]
            
                if str(RoomDict.get(z)) == str(v.get()):
                    a = "UPDATE ROOMS SET ROOM_AVAILABLE = \'FALSE\' WHERE ROOMNO = \'%s\' "
                    cur.execute(a%(z,))
                    db.commit()
                    string = "Congratulations You Have Successfully Booked Room" + str(z)
                    
                    ins = "INSERT INTO USER_DETAILS VALUES(\'"+ name +"\',\'"+ contact +"\',\'" + email +"\',\'" + add +"\',\'" + dob +"\',\'"+ dcheck +"\',\'"+ idvar.get() + "\',\'"+ str(z)+"\')"
                    
                    cur.execute(ins)
                    db.commit()
                    break
                else:
                    string = "Not Booked"
                    string2 = ""
                    string3 = ""
            Label(BookedRoomW,text = string,fg = "red",bg = "Antique White",font = "Georgia 25").pack()
            
    Button(roomBookw,text = "Book Room",fg = "Red",bg ="Orange",font = "BodoniFLF 16",command = BookedRoom,relief = FLAT).place(x = 1200,y = 600) 
def admin():
    def adminopen():
        LoginId = str(e1.get())
        password = str(e2.get())
        if LoginId == "admin" and password  == "admin":
            adminW = Toplevel(adminw)
            adminW.configure(background = "Antique White")
            adminW.geometry("800x800")
            Label(adminW,text = "Welcome Employee",fg = "Red",bg = "Antique White",font = "Rockwell 30").place(x = 100,y = 50)
            def seeCust():
                CustW = Toplevel(adminW)
                CustW.configure(background = "Antique White")
                CustW.geometry("1366x768")
                n = 80
                cur.execute("SELECT * FROM CUSTOMER_DETAILS")
                for y in cur:
                    
                    name = str(y[0])
                    Contact = str(y[1])
                    email = str(y[2])
                    add = str(y[3])
                    dob = str(y[4])
                    dcheck = str(y[5])
                    Id = str(y[6])
                    room = str(y[7])
                    if name == "None":
                        continue
                    else:
                        n = n + 20
                       
                        Label(CustW,text = "Room Booked " + room,bg = "Antique White").place(x = 150,y = n)
                        def details():
                            det = Toplevel(CustW)
                            Label(det,text = "Name: " + name,bg = "Antique White").place(x = 100,y = 100)
                            Label(det,text = "COntact Number: " + Contact,bg = "Antique White").place(x = 100,y = 200)
                            Label(det,text = "E-Mail ID: " + email,bg = "Antique White").place(x = 100,y = 300)
                            Label(det,text = "Residential Address: " + add,bg = "Antique White").place(x = 100,y = 400)
                            Label(det,text = "Date of Birth " + dob,bg = "Antique White").place(x = 100,y = 500)
                            Label(det,text = "ID: " + Id,bg = "Antique White").place(x = 100,y =550)
                            Label(det,text = "Date of Check-In " + dcheck,bg = "Antique White").place(x = 100,y = 600)
                        Button(CustW,text = "See Full Details",command = details,bg = "Antique White",relief = FLAT).place(x = 250,y = n)
                        
                               
            def seeRoom():
                roomW = Toplevel(adminW)
                roomW.configure(background = "Antique White")
                roomW.geometry("800x800")
                n = 80
                cur.execute("SELECT * FROM ROOMS")
                for y in cur:
                    n = n+20
                    roomNo = str(y[0])
                    roomAvail = str(y[2])
                    if roomAvail == "TRUE":
                        roomAvail = "Vacant Room"
                    else:
                        roomAvail = "Not Vacant"
                    Label(roomW,text = "Room No." + roomNo,bg = "Antique White").place(x = 100,y = n)
                    Label(roomW,text = "Room Available" + roomAvail,bg = "Antique White").place(x = 400,y = n)
            def checkOut():
                roomW = Toplevel(adminW)
                roomW.configure(background = "Antique White")
                
                roomVar = StringVar(roomW)
                roomVar.set("Select Room No.")
                option = OptionMenu(roomW,roomVar,"101","102","103","104","105","106")
                option.pack()
                def do():
                    room = roomVar.get()
                    checkoutw = Toplevel(roomW)
                    Label(checkoutw,text = "Done").pack()
                    room = roomVar.get()
                    cur.execute("UPDATE ROOMS SET ROOM_AVAILABLE = TRUE WHERE ROOMNO =" + str(room))
                    db.commit()
                Button(roomW,text = "Update Status",bg = "Orange",relief = FLAT,command = do).pack()
            Button(adminW,text = "See Customer Details",relief = FLAT,font = "Orbitron 20",fg = "Light Blue",bg = "Antique White",command = seeCust).place(x = 50,y = 350)
            Button(adminW,text = "Check Out",relief = FLAT,font = "Orbitron 20",fg = "Light Blue",bg = "Antique White",command = checkOut).place(x = 250,y = 500)
            Button(adminW,text = "See Room Status",relief = FLAT,font = "Orbitron 20",fg = "Light Blue",bg = "Antique White",command = seeRoom).place(x = 450,y = 350)
        elif len(LoginId)== 0 or len(password) == 0:
            adminW = Toplevel(adminw)
            Message(adminW,text = "Please enter Credentials").pack()
        else:
            adminW = Toplevel(adminw)
            
            Message(adminW,text = "Invalid Credentials").pack()

    
    adminw = Toplevel(gui)
    adminw.configure(background = "Antique White")
    adminw.geometry("800x800")
    Label(adminw,text = "Please Login to get Admin access",fg = "Red",bg = "Antique White",font = "Rockwell 30").place(x = 100,y = 50)
    Label(adminw,text = "Login Id",fg  = "Black",bg  = "Antique White",font = "Verdana 25").place(x = 350,y = 250)
    Label(adminw,text = "Password",fg  = "Black",bg  = "Antique White",font = "Verdana 25").place(x = 350,y = 350)
    e1 = Entry(adminw,width = 25)
    e1.place(x = 350,y = 300)
    e2 = Entry(adminw,show = "*",width = 25)
    e2.place(x = 350,y = 400)
    Button(adminw,text = "Get access",fg = "Red",bg = "Blue",command = adminopen).place(x = 400,y = 500)
    

    
    
    
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background  = "Black")
    gui.geometry("1024x768")
    gui.title("Hotel Management Software SHALIMAR")
    photo = PhotoImage(file = "l.png")
    Label(gui,image = photo,border = 0).place( x= 350,y = 100) 
    Button(gui,text = "Book A Room",font = "Georgia 20",padx = 8,pady = 8,command = bookARoom,relief=FLAT,bg = "Orange").place(x = 400,y =400)
    Button(gui,text = "Admin login ",fg  = "Green",bg = "Yellow",command = admin).place (x = 750,y=20)
    gui.mainloop()
    
    
