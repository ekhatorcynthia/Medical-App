from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
from newspaper import article
#from Doctor import chat
import string
import nltk
import numpy as np
import json
import pickle
import warnings
warnings.filterwarnings("ignore")
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk import punkt 
from nltk import wordnet
import threading



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="hospital_db"
    )






def main():
    root =Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1350x750+0+0")
        self.master.config( bg='powder blue')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.frame.config( bg='powder blue')
        


        self.Username = StringVar()
        self.Password = StringVar()
        


        self.LabelTitle =Label(self.frame,text ='Hospital Management System',
                               font=('arial',50,'bold'),bd=20,bg = ("powder blue"))
        self.LabelTitle.grid(row=0, column=0, columnspan=2,pady=20)
        
        self.Loginframe1 = Frame(self.frame , width=1010,height=300,bd=5,
                                relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame , width=1000,height=100,bd=5
                                ,relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame , width=1010,height=200,bd=5
                                ,relief='ridge')
        self.Loginframe3.grid(row=3, column=0,pady=2)

        #=====================================================================

        self.lblUsername =Label(self.Loginframe1,text ='Username',
                               font=('arial',20,'bold'),bd=5)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername =Entry(self.Loginframe1,
                               font=('arial',16,'bold'),bd=5,
                                textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1,padx =85,pady =8)


        self.lblPassword =Label(self.Loginframe1,text ='Password',
                               font=('arial',20,'bold'),bd=5)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword =Entry(self.Loginframe1,
                               font=('arial',20,'bold'),bd=5,show="*",
                                textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1,padx =85,pady =8)

        #=====================================================================
        

        self.btnLogin = Button(self.Loginframe2, text="Login",width=17,font=('arial',20,'bold'),
                                 command =self.Login_System)
        self.btnLogin.grid(row = 0 ,column =0)


        self.btnExit = Button(self.Loginframe2, text="Exit",width=17,font=('arial',20,'bold'),
                                 command =self.iExit)
        self.btnExit.grid(row = 0 ,column =2)

        

        self.btnPatient = Button(self.Loginframe3, text="New Patient Registration",
                                 state = DISABLED, command =self.Patient_window,font=('arial',20,'bold'))
        self.btnPatient.grid(row = 0 ,column =0,pady =12,padx=15)

        self.btnExiting = Button(self.Loginframe3, text="Exiting Patient Registration",
                                 state = DISABLED, command =self.Exiting_window,font=('arial',20,'bold'))
        self.btnExiting.grid(row = 0 ,column =1,pady =8,padx=15)

         #=====================================================================

    def Login_System(self):
            user = (self.Username.get())
            password = (self.Password.get())


            if ( user == str("Maa")) and (password == str(123456)):
                 self.btnPatient.config(state = NORMAL)
                 self.btnExiting.config(state = NORMAL)

            elif ( user == str("Ben")) and (password == str(789456)):
                 self.btnPatient.config(state = NORMAL)
                 self.btnExiting.config(state = NORMAL)

            elif ( user == str("Yaa")) and (password == str(456123)):
                 self.btnPatient.config(state = NORMAL)
                 self.btnExiting.config(state = NORMAL)

                 
            else:
                 tkinter.messagebox.askyesno("Hospital Management System","You have entered an invalid login details")
                 self.btnPatient.config(state = DISABLED)
                 self.btnExiting.config(state = DISABLED)
                 self.Username.set("")
                 self.Password.set("")
                 self.txtUsername.focus()
                
                 
    def iExit(self):
         self.iExit =tkinter.messagebox.askyesno("Medical Diagnosis System","Confirm if you want to exit")
         if self.iExit > 0:
             self.master.destroy()
             return
                 


         #=====================================================================

    def Patient_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)



    def Exiting_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
        



class Window2:
    
    def Doctor_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)

        
    def __init__(self, master):
        self.master = master
        self.master.title("New Patient Registration")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.config( bg='powder blue')

    

        #=====================================================================

        


        Dateoforder=StringVar()
        Dateoforder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=IntVar()


        Cardnumber=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Middlename=StringVar()
        DateofBirth=StringVar()
        Age=StringVar()
        Telephone=StringVar()
        Residenceaddress=StringVar()
        NextofKin=StringVar()
        Nationality=StringVar()
        MaritalStatus=StringVar()
        Gender=StringVar()
        Occupation=StringVar()
        Email=StringVar()
        Address=StringVar()
        Amount=StringVar()

        Membership =StringVar()
        Membership.set("0")


        def save():
            
            card_No()
            self.txtReceipt.insert(END,"\t" + Cardnumber.get()+"\t\t"+Firstname.get()+ "\t\t"+Surname.get()+
                                   "\t\t"+Middlename.get()+ "\t\t"+Address.get()+"\t\t"+Telephone.get()+"\t\t"
                                   +Amount.get()+"\t\t"+ Dateoforder.get()+"\n")

            mycursor = mydb.cursor()
            sql = "INSERT INTO patient_data (card_number,date,first_name,middle_name,surname,date_of_birth,age,gender,telephone,residence_address,next_of_kin,nationality,marital_status,occupation,email,payment_method,membership_fee) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(Cardnumber.get(),Dateoforder.get(),Firstname.get(),Middlename.get(),Surname.get(),DateofBirth.get(),Age.get(),var1.get(),Telephone.get(),
                  Address.get(),NextofKin.get(),var4.get(),var2.get(),var5.get(),Email.get(),var3.get(),Amount.get())
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

    
        



        def card_No():
            Y = random.randint(1,900000)
            randomCardnumber = str(Y)
            Cardnumber.set(randomCardnumber)
            
        def Delete():
                Firstname.set("")
                Surname.set("")
                Middlename.set("")
                DateofBirth.set("")
                Age.set("")
                Telephone.set("")
                Residenceaddress.set("")
                NextofKin.set("")
                Nationality.set("")
                MaritalStatus.set("")
                Gender.set("")
                Occupation.set("")
                Email.set("")
                Address.set("")
                Amount.set("")

                var1.set("")
                var2.set("")
                var3.set("")
                var4.set("")
                var5.set("")
                

                self.cboGender.current(0)
                self.cboNationality.current(0)
                self.cboMaritalstatus.current(0)
                self.cboMethodofpayment.current(0)
                
        

        
            
                
        


        
        Mainframe=Frame(self.frame)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe, bd=5, width=1350, padx=35, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',50,'bold'),text="New Patient Registration ",padx=4)
        self.lblTitle.grid()

#=====================================================================
        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500, bd=5,pady=5, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=5,width=800,height=1000,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10,width=350,height=400,
        font=('arial',12,'bold'),text = 'Patient Details',relief=RIDGE)
        
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame= LabelFrame(MemberDetailsFrame, bd=5,width=1000,height=500,relief=RIDGE)

        Receipt_ButtonFrame.pack(side=RIGHT)
#=====================================================================
        self.lblCardnumber=Label(MembersName_F,font=('arial',13,'bold'),text="Card Number ",bd=3)
        self.lblCardnumber.grid(row=0, column=0, sticky=W)
        self.txtCardnumber=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Cardnumber, state =DISABLED, insertwidth=2)
        self.txtCardnumber.grid(row=0, column=1)

        self.lblDate=Label(MembersName_F,font=('arial',13,'bold'),text="Date ",bd=3)
        self.lblDate.grid(row=1, column=0, sticky=W)
        self.txtDate=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Dateoforder, insertwidth=2)
        self.txtDate.grid(row=1, column=1)

        self.lblFirstname=Label(MembersName_F,font=('arial',13,'bold'),text="First Name ",bd=3)
        self.lblFirstname.grid(row=2, column=0, sticky=W)
        self.txtFirstname=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Firstname, insertwidth=2)
        self.txtFirstname.grid(row=2, column=1)

        self.lblMiddlename=Label(MembersName_F,font=('arial',13,'bold'),text="Middle name ",bd=3)
        self.lblMiddlename.grid(row=3, column=0, sticky=W)
        self.txtMiddlename=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Middlename, insertwidth=2)
        self.txtMiddlename.grid(row=3, column=1)

        self.lblSurname=Label(MembersName_F,font=('arial',13,'bold'),text="Surname ",bd=3)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateofBirth=Label(MembersName_F,font=('arial',13,'bold'),text="Date of Birth ",bd=3)
        self.lblDateofBirth.grid(row=5, column=0, sticky=W)
        self.txtDateofBirth=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=DateofBirth, insertwidth=2)
        self.txtDateofBirth.grid(row=5, column=1)

        self.lblAge=Label(MembersName_F,font=('arial',13,'bold'),text="Age ",bd=3)
        self.lblAge.grid(row=6, column=0, sticky=W)
        self.txtAge=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Age, insertwidth=2)
        self.txtAge.grid(row=6, column=1)

        self.lblTelephone=Label(MembersName_F,font=('arial',13,'bold'),text="Telephone Number ",bd=3)
        self.lblTelephone.grid(row=7, column=0, sticky=W)
        self.txtTelephone=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Telephone, insertwidth=2)
        self.txtTelephone.grid(row=7, column=1)

        self.lblAddress=Label(MembersName_F,font=('arial',13,'bold'),text="Residence Address ",bd=3)
        self.lblAddress.grid(row=8, column=0, sticky=W)
        self.txtAddress=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Address, insertwidth=2)
        self.txtAddress.grid(row=8, column=1)

        self.lblNextofkin=Label(MembersName_F,font=('arial',13,'bold'),text="Next of kin ",bd=3)
        self.lblNextofkin.grid(row=9, column=0, sticky=W)
        self.txtNextofkin=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=NextofKin, insertwidth=2)
        self.txtNextofkin.grid(row=9, column=1)

        self.lblEmail=Label(MembersName_F,font=('arial',13,'bold'),text="Email ",bd=3)
        self.lblEmail.grid(row=10, column=0, sticky=W)
        self.txtEmail=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Email, insertwidth=2)
        self.txtEmail.grid(row=10, column=1)

        self.lblGender=Label(MembersName_F,font=('arial',13,'bold'),text="Gender ",bd=3)
        self.lblGender.grid(row=11, column=0, sticky=W)
        self.cboGender=ttk.Combobox(MembersName_F,textvariable=var1,state= 'readonly',font=('arial',13,'bold'),width=18)
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=11, column=1)

        self.lblNationality=Label(MembersName_F,font=('arial',13,'bold'),text="Nationality ",bd=3)
        self.lblNationality.grid(row=12, column=0, sticky=W)
        self.cboNationality=ttk.Combobox(MembersName_F,textvariable=var4,state= 'readonly',font=('arial',13,'bold'),width=18)
        self.cboNationality['value']=('','Ghanaian','Other')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=12, column=1)

        self.lblMaritalstatus=Label(MembersName_F,font=('arial',13,'bold'),text="Marital Status ",bd=3)
        self.lblMaritalstatus.grid(row=13, column=0, sticky=W)
        self.cboMaritalstatus=ttk.Combobox(MembersName_F,textvariable=var2,state= 'readonly',font=('arial',13,'bold'),width=18)
        self.cboMaritalstatus['value']=('','Single','Married','Divorced')
        self.cboMaritalstatus.current(0)
        self.cboMaritalstatus.grid(row=13, column=1)

        self.lblOccupation=Label(MembersName_F,font=('arial',13,'bold'),text="Occupation ",bd=3)
        self.lblOccupation.grid(row=14, column=0, sticky=W)
        self.cboOccupation=ttk.Combobox(MembersName_F,textvariable=var5,state= 'readonly',font=('arial',13,'bold'),width=18)
        self.cboOccupation['value']=('','Working','Non Working','Student')
        self.cboOccupation.current(0)
        self.cboOccupation.grid(row=14, column=1)

        self.lblMethodofpayment=Label(MembersName_F,font=('arial',13,'bold'),text="Payment Method ",bd=3)
        self.lblMethodofpayment.grid(row=15, column=0, sticky=W)
        self.cboMethodofpayment=ttk.Combobox(MembersName_F,textvariable=var3,font=('arial',13,'bold'),width=18)
        self.cboMethodofpayment['value']=('','Cash','Mobile money')
        self.cboMethodofpayment.current(0)
        self.cboMethodofpayment.grid(row=15, column=1)

        self.lblAmount=Label(MembersName_F,font=('arial',13,'bold'),text="Membership Fee ",bd=3)
        self.lblAmount.grid(row=16, column=0, sticky=W)
        self.txtAmount=Entry(MembersName_F,font=('arial',13,'bold'),bd=3,textvariable=Amount, insertwidth=2)
        self.txtAmount.grid(row=16, column=1)
#=====================================================================
        self.lblheader=Label(Receipt_ButtonFrame,font=('arial',10,'bold'),pady=10
        ,text="Card Number\t Firstname\t Middlename\t Surname\t Address\t\t Telephone\t Registration Fee\t\t Date\t")
        self.lblheader.grid(row=0, column=0, columnspan=4)

        self.txtReceipt=Text(Receipt_ButtonFrame,width=137, height =22,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

#=====================================================================

        self.btnReceipt=Button(Receipt_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Save"), command= save)
        self.btnReceipt.grid(row =2,column=0)

    
            
           

        self.btnExit=Button(Receipt_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Delete"), command= Delete)
        self.btnExit.grid(row =2,column=1)

        self.btnPrint=Button(Receipt_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Print"))
        self.btnPrint.grid(row =2,column=2)

#=================================Doctor====================================

        self.btnDoctor = Button(Receipt_ButtonFrame, padx=15, bd=4,font=('arial',12,'bold'),width=10,
        text=("Doctor"), command =self.Doctor_window)
        self.btnDoctor.grid(row =2,column=3)
        
#=====================================================================



#=====================================================================



class Window3:
    
    def Doctor_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)
        
    def __init__(self, master):
        self.master = master
        self.master.title("Exiting Patient Registration")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.config( bg='powder blue')
        
#=====================================================================

        Dateoforder=StringVar()
        Dateoforder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=IntVar()


        Cardnumber=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Middlename=StringVar()
        DateofBirth=StringVar()
        Amount=StringVar()
        Telephone=StringVar()


        def save():
            mycursor = mydb.cursor()
            sql = "SELECT * FROM patient_data WHERE card_number ="+ Cardnumber.get()+""
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            record()
            card_No()
            self.txtReceipt.insert(END,"\t" + myresult[1]+"\t\t\t"+myresult[3]+ "\t\t\t"+myresult[4]+
                                   "\t\t\t"+myresult[5]+"\t\t"+ Dateoforder.get()+"\t\t\t"+Amount.get()+"\n")

            self.txtFirstname.insert(END,"\t" + myresult[3])
            self.txtMiddlename.insert(END,"\t" + myresult[4])
            self.txtSurname.insert(END,"\t" + myresult[5])
            self.txtDateofBirth.insert(END,"\t" + myresult[6])
           
            
            

        def record():
            mycursor = mydb.cursor()
            sql = "INSERT INTO exiting_data (Card_number,Date,Membership_fee) VALUE (%s,%s,%s)"
            val = (Cardnumber.get(),Dateoforder.get(),Amount.get())
            mycursor.execute(sql,val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            

    
        



        def card_No():
            Y = random.randint(0,0)
            randomCardnumber = str(Y)
            Cardnumber.set(randomCardnumber)
        


        Exiting =StringVar()
        Exiting.set("0")

        Subframe=Frame(self.frame)
        Subframe.grid()

        TitleFrame=Frame(Subframe, bd=5, width=1450, padx=35, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',48,'bold'),text="Exiting Patient ",padx=4)
        self.lblTitle.grid()

#=====================================================================
        ExitingDetailsFrame = LabelFrame(Subframe,width=1350,height=700, bd=5,pady=5, relief=RIDGE)
        ExitingDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(ExitingDetailsFrame, bd=3,width=1400,height=950,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        ExitingName_F = LabelFrame(FrameDetails, bd=7,width=350,height=400,
        font=('arial',12,'bold'),text = 'Patient Details',relief=RIDGE)
        
        ExitingName_F.grid(row=0,column=0)

        Exiting_ButtonFrame= LabelFrame(ExitingDetailsFrame, bd=5,width=1400,height=530,relief=RIDGE)

        Exiting_ButtonFrame.pack(side=RIGHT)
        
#=====================================================================

        self.lblCardnumber=Label(ExitingName_F,font=('arial',13,'bold'),text="Card Number ",bd=3)
        self.lblCardnumber.grid(row=0, column=0, sticky=W)
        self.txtCardnumber=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=Cardnumber, insertwidth=2)
        self.txtCardnumber.grid(row=0, column=1)

        self.lblDate=Label(ExitingName_F,font=('arial',13,'bold'),text="Date ",bd=3)
        self.lblDate.grid(row=1, column=0, sticky=W)
        self.txtDate=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=Dateoforder, insertwidth=2)
        self.txtDate.grid(row=1, column=1)

        self.lblFirstname=Label(ExitingName_F,font=('arial',13,'bold'),text="First Name ",bd=3)
        self.lblFirstname.grid(row=2, column=0, sticky=W)
        self.txtFirstname=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=Firstname, insertwidth=2)
        self.txtFirstname.grid(row=2, column=1)

        self.lblMiddlename=Label(ExitingName_F,font=('arial',13,'bold'),text="Middle name ",bd=3)
        self.lblMiddlename.grid(row=3, column=0, sticky=W)
        self.txtMiddlename=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=Middlename, insertwidth=2)
        self.txtMiddlename.grid(row=3, column=1)

        self.lblSurname=Label(ExitingName_F,font=('arial',13,'bold'),text="Surname ",bd=3)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateofBirth=Label(ExitingName_F,font=('arial',13,'bold'),text="Date of Birth ",bd=3)
        self.lblDateofBirth.grid(row=5, column=0, sticky=W)
        self.txtDateofBirth=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=DateofBirth, insertwidth=2)
        self.txtDateofBirth.grid(row=5, column=1)

        self.lblPayment=Label(ExitingName_F,font=('arial',13,'bold'),text="Payment Method ",bd=3)
        self.lblPayment.grid(row=6, column=0, sticky=W)
        self.cboPayment=ttk.Combobox(ExitingName_F,textvariable=var1,font=('arial',13,'bold'),width=18)
        self.cboPayment['value']=('','Cash','Mobile money')
        self.cboPayment.current(0)
        self.cboPayment.grid(row=6, column=1)

        self.lblAmount=Label(ExitingName_F,font=('arial',13,'bold'),text="Membership Fee ",bd=3)
        self.lblAmount.grid(row=7, column=0, sticky=W)
        self.txtAmount=Entry(ExitingName_F,font=('arial',13,'bold'),bd=3,textvariable=Amount, insertwidth=2)
        self.txtAmount.grid(row=7, column=1)

#=====================================================================

        self.lblheader=Label(Exiting_ButtonFrame,font=('arial',10,'bold'),pady=10
        ,text="Card Number\t\t Firstname\t\t Middlename\t\t Surname\t\t Date\t\t Membership Fee\t")
        self.lblheader.grid(row=0, column=0, columnspan=4)

        self.txtReceipt=Text(Exiting_ButtonFrame,width=140, height =25,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        self.btnPrint=Button(Exiting_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Retrive"), command= save)
        self.btnPrint.grid(row =2,column=0)

        

        self.btnPrint=Button(Exiting_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Print"))
        self.btnPrint.grid(row =2,column=1)

        self.btnPrint=Button(Exiting_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Delete"))
        self.btnPrint.grid(row =2,column=2)

        self.btnPrint=Button(Exiting_ButtonFrame, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Doctor"), command =self.Doctor_window)
        self.btnPrint.grid(row =2,column=3)
       

        


        


#=====================================================================

class Window4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Boateng")
        self.master.geometry("700x500")
        self.frame = Frame(self.master)

        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)


   

#=====================================================================
         
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)


        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Arial", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

#=====================================================================
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

#=====================================================================

        self.entry_field = Entry(self.entry_frame, bd=1,font= 10, justify=LEFT)
        self.entry_field.pack(fill=X, padx=8, pady=8, ipady=15)
        # self.users_message = self.entry_field.get()

#=====================================================================

        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        self.save_button_frame = Frame(self.master, bd=0)
        self.save_button_frame.pack(fill=BOTH)

#=====================================================================

        self.send_button = Button(self.send_button_frame,font=("Verdana",8,'bold'), text="Send", width=8, relief=GROOVE, bg="powder blue",
                                  bd=1,command=(lambda: self.send_message_insert(None)),activebackground="powder blue",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT,fill=X, padx=8, pady=8, ipady=15)
        self.master.bind("<Return>", self.send_message_insert)


        




    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        pr1 = "Patient : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        ob=chat(user_input)
        pr="Doctor Boateng : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.entry_field.delete(0,END)
        time.sleep(0)
        
        

#=====================================================================



f=open('try.txt' ,'r' ,errors ='ignore')
m=open('modules.txt' ,'r' ,errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"

raw=f.read()
rawone=m.read()
raw=raw.lower()
rawone=rawone.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
sent_tokensone = nltk.sent_tokenize(rawone) 
word_tokensone = nltk.word_tokenize(rawone)

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="hospital_db"
    )

mycursor = mydb.cursor()
sql = "SELECT * FROM patient_data"
mycursor.execute(sql)
myresult = mycursor.fetchone()

def save():
            mycursor = mydb.cursor()
            sql = "INSERT INTO patient_data (Report) VALUES (%s)"
            val =(chat.get())
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            


GREETING_INPUTS = ("hello", "hi","hii","greetings", "sup","hey","sap")
GREETING_RESPONSES = ["hi " +myresult[3] + ", checking of Vitals please( Weight(kg) )", "hey " +myresult[3] + ", checking of Vitals please( Weight(kg) )","hi there " +myresult[3] + ", checking of Vitals please( Weight(kg) )", "hello " +myresult[3] + ", checking of Vitals please( Weight(kg) )"]
NURSE_W =["25kg","26kg","27kg","28kg","29kg","30kg","31kg","32kg","33kg","34kg","35kg","36kg","37kg","38kg","39kg","40kg","41kg","42kg","43kg","43kg","44kg","45kg","46kg","47kg","48kg","49kg","50kg","51kg","52kg","53kg","54kg","55kg","56kg","57kg","58kg","59kg","60kg","61kg","62kg","63kg","64kg","65kg","66kg","67kg","68kg","69kg","70kg","71kg","72kg","73kg","74kg","75kg","76kg","77kg","78kg","79kg","80kg"]
NURSE_K = ["Please input your Temperature ºC"]
NURSE_T =["36c","37c"]
NURSE_R = ["Your Temperature is normal, Please input Blood Pressure (bp)"]
NURSE_TH = ["38c","39c","40c","41c","42c"]
NURSE_RH = ["Your Temperature is High (Patient need infusion), Please input Blood Pressure (bp)"]
NURSE_TL = ["28c","29c","30c","31c","32c","33c","34c","35c",]
NURSE_RL = ["Your Temperature is Low (Patient need Tsiponshi), Please input Blood Pressure (bp)"]
NURSE_BN =["70bp","71bp","72bp","73bp","74bp","75bp","76bp","77bp","78bp","79bp","80bp","81bp","82bp","83bp","84bp","85bp","86bp","87bp","88bp","89bp","90bp"]
NURSE_BNR = ["Your Blood Pressure is Normal.  " + myresult[3] + ", What wrong with you?"]
LAB_T = ["p","P","positive","POSITIVE"]
LAB_R =["POSITIVE, Please input the test result"]
LAB_TN = ["n","N","negative","NEGATIVE"]
LAB_RN = ["NEGATIVE, Please input the test result"]






def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def NURSE(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_W:
            return random.choice(NURSE_K)

def Temp(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_T:
            return random.choice(NURSE_R)

def TempHigh(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_TH:
            return random.choice(NURSE_RH)

def TempLow(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_TL:
            return random.choice(NURSE_RL)

def BloodP(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_BN:
            return random.choice(NURSE_BNR)

def LabT(sentence):
    for word in sentence.split():
        if word.lower() in LAB_T:
            return random.choice(LAB_R)

def Lab2(sentence):
    for word in sentence.split():
        if word.lower() in LAB_TN:
            return random.choice(LAB_RN)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response



def responseone(user_response):
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response



def chat(user_response):
    user_response=user_response.lower()
    keyword = " Malaria "
    keywordone = " Cholera "


    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            return "You are welcome.."
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1):
                return responseone(user_response)
                sent_tokensone.remove(user_response)

            elif(greeting(user_response)!=None):
                return greeting(user_response)
            elif(NURSE(user_response)!=None):
                return NURSE(user_response)
            elif(Temp(user_response)!=None):
                return Temp(user_response)
            elif(TempHigh(user_response)!=None):
                return TempHigh(user_response)
            elif(TempLow(user_response)!=None):
                return TempLow(user_response)
            elif(BloodP(user_response)!=None):
                return BloodP(user_response)
            elif(LabT(user_response)!=None):
                return LabT(user_response)
            elif(Lab2(user_response)!=None):
                return Lab2(user_response)
            else:
                return response(user_response)
                sent_tokens.remove(user_response)
    


    else:
        flag=False
        return "Bye! take care.."
    save()

    
        
        
        

            



        
    
        

#=====================================================================
        
        


if __name__=='__main__':
    main()
    



 
