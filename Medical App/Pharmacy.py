from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import string
import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Hospital_db"
    )






def main():
    root =Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.master.config( bg='light blue')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.frame.config( bg='light blue')
        


        self.Username = StringVar()
        self.Password = StringVar()
        


        self.LabelTitle =Label(self.frame,text ='Pharmacy Management System',
                               font=('arial',50,'bold'),bd=20,bg = ("light blue"))
        self.LabelTitle.grid(row=0, column=0, columnspan=2,pady=20)
        
        self.Loginframe1 = Frame(self.frame , width=700,height=300,bd=4,padx =55,
                                relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame , width=890,height=100,bd=4
                                ,relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame , width=700,height=200,bd=4
                                ,relief='ridge')
        self.Loginframe3.grid(row=3, column=0,pady=1)

        #=====================================================================

        self.lblUsername =Label(self.Loginframe1,text ='Username',
                               font=('arial',20,'bold'),bd=4)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername =Entry(self.Loginframe1,
                               font=('arial',16,'bold'),bd=4,
                                textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1,padx =85,pady =8)


        self.lblPassword =Label(self.Loginframe1,text ='Password',
                               font=('arial',20,'bold'),bd=4)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword =Entry(self.Loginframe1,
                               font=('arial',20,'bold'),bd=4,show="*",
                                textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1,padx =85,pady =8)

        #=====================================================================
        

        self.btnLogin = Button(self.Loginframe2, text="Login",width=17,font=('arial',20,'bold'),
                                 command =self.Login_System)
        self.btnLogin.grid(row = 0 ,column =0)


        self.btnExit = Button(self.Loginframe2, text="Exit",width=17,font=('arial',20,'bold'),
                                 command =self.iExit)
        self.btnExit.grid(row = 0 ,column =2)

        

        self.btnPatient = Button(self.Loginframe3, text="Drugs Despenary",
                                 state = DISABLED, command =self.Patient_window,font=('arial',20,'bold'))
        self.btnPatient.grid(row = 0 ,column =0,pady =12,padx=15)

        #self.btnExiting = Button(self.Loginframe3, text="Inventory/Store",
                                # state = DISABLED, command =self.Exiting_window,font=('arial',20,'bold'))
       # self.btnExiting.grid(row = 0 ,column =1,pady =8,padx=15)

         #=====================================================================

    def Login_System(self):
            user = (self.Username.get())
            password = (self.Password.get())


            if ( user == str("Derek")) and (password == str(123456)):
                 self.btnPatient.config(state = NORMAL)
                 self.btnExiting.config(state = NORMAL)

            elif ( user == str("Boat")) and (password == str(789456)):
                 self.btnPatient.config(state = NORMAL)
                 self.btnExiting.config(state = NORMAL)

            elif ( user == str("Dee")) and (password == str(456123)):
                 self.btnPatient.config(state = NORMAL)
                 self.btnExiting.config(state = NORMAL)

                 
            else:
                 tkinter.messagebox.askyesno("Pharmacy Management System","You have entered an invalid login details")
                 self.btnPatient.config(state = DISABLED)
                 self.btnExiting.config(state = DISABLED)
                 self.Username.set("")
                 self.Password.set("")
                 self.txtUsername.focus()
                
                 
    def iExit(self):
         self.iExit =tkinter.messagebox.askyesno("Pharmacy System","Confirm if you want to exit")
         if self.iExit > 0:
             self.master.destroy()
             return
                 


         #=====================================================================

    def Patient_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)



    
        



class Window2:
        
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
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
        Medication_1=StringVar()
        Medication_2=StringVar()
        Medication_3=StringVar()
        Injection=StringVar()
        Expiring_Date=StringVar()
        Dosage=StringVar()
        Prescription=StringVar()
        Methodofpayment=StringVar()
        
        
        
        Amount=StringVar()

        Membership =StringVar()
        Membership.set("0")
            

        def save():
            mycursor = mydb.cursor()
            sql = "INSERT INTO pharmacy_data (date,Medication_1,Medication_2,Medication_3,Injection,Expiring_Date,Prescription,Dosage,Payment_Method) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(Dateoforder.get(),Medication_1.get(),Medication_2.get(),Medication_3.get(),Injection.get(),Expiring_Date.get(),Prescription.get(),Dosage.get(),Methodofpayment.get())
            mycursor.execute(sql,val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            



        def record():
            mycursor = mydb.cursor()
            sql = "SELECT * FROM patient_data WHERE card_number ="+ Cardnumber.get()+""
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            card_No()
            self.txtFrameDetails.insert(END,"\t" + myresult[1]+"\t\t"+myresult[3]+ "\t\t"+myresult[4]+
                                   "\t\t"+myresult[5]+"\t\t"+Medication_1.get()+"\t\t"+Medication_1.get()+"\t\t"+Medication_3.get()+"\t\t"+Injection.get()+"\t\t"+
                                        Prescription.get()+"\t\t"+Dosage.get()+"\t\t"+Dateoforder.get()+"\n")
            

            self.txtFirstname.insert(END,"\t" + myresult[3])
            self.txtMiddlename.insert(END,"\t" + myresult[4])
            self.txtSurname.insert(END,"\t" + myresult[5])
            self.txtDateofBirth.insert(END,"\t" + myresult[6])
            self.txtAge.insert(END,"\t" + myresult[7])
            self.txtTelephone.insert(END,"\t" + myresult[9])

            
            

    
        



        def card_No():
            Y = random.randint(1,900000)
            randomCardnumber = str(Y)
            
        def Delete():
                Firstname.set("")
                Surname.set("")
                Middlename.set("")
                DateofBirth.set("")
                Age.set("")
                Telephone.set("")
                Medication_1.set("")
                Medication_2.set("")
                Medication_3.set("")
                Injection.set("")
                Expiring_Date.set("")
                Dosage.set("")
                Prescription.set("")
                Methodofpayment.set("")

                var1.set("")
                var2.set("")
                var3.set("")
                var4.set("")
                var5.set("")
                

                
                self.cboMethodofpayment.current(0)
                
        

        
            
                
        


        
        Mainframe=Frame(self.frame)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe, bd=5, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',40,'bold'),text="Pharmacy Management System ",padx=4)
        self.lblTitle.grid()

#====================================================================================

        FrameDetails = LabelFrame(Mainframe, bd=5,width=1350,height=300, padx=20,relief=RIDGE)
        FrameDetails.pack(side=BOTTOM)

        MedicationDetails = LabelFrame(Mainframe, bd=5,width=1350,height=50, padx=20,relief=RIDGE)
        MedicationDetails.pack(side=BOTTOM)

        RecordDetails = LabelFrame(Mainframe, bd=5,width=1350,height=330, padx=20,relief=RIDGE)
        RecordDetails.pack(side=BOTTOM)

        RecordDetailsLEFT = LabelFrame(RecordDetails, bd=5,width=800,height=330, padx=20,relief=RIDGE,
                                       font=('arial',13,'bold'),text="Patient Details ")
        RecordDetailsLEFT.pack(side=LEFT)

        RecordDetailsRIGHT = LabelFrame(RecordDetails, bd=5,width=450,height=330, padx=20,relief=RIDGE,
                                        font=('arial',13,'bold'),text="Doctor's Report ")
        RecordDetailsRIGHT.pack(side=RIGHT)
        

#======================================================================================
        self.lblCardnumber=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Card Number ",padx=2,bd=3)
        self.lblCardnumber.grid(row=0, column=0, sticky=W)
        self.txtCardnumber=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Cardnumber,insertwidth=2)
        self.txtCardnumber.grid(row=0, column=1)

        self.lblDate=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Date ",bd=3)
        self.lblDate.grid(row=1, column=0, sticky=W)
        self.txtDate=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Dateoforder, insertwidth=2)
        self.txtDate.grid(row=1, column=1)

        self.lblFirstname=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="First Name ",bd=3)
        self.lblFirstname.grid(row=2, column=0, sticky=W)
        self.txtFirstname=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Firstname, insertwidth=2)
        self.txtFirstname.grid(row=2, column=1)

        self.lblMiddlename=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Middle name ",bd=3)
        self.lblMiddlename.grid(row=3, column=0, sticky=W)
        self.txtMiddlename=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Middlename, insertwidth=2)
        self.txtMiddlename.grid(row=3, column=1)

        self.lblSurname=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Surname ",bd=3)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateofBirth=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Date of Birth ",bd=3)
        self.lblDateofBirth.grid(row=5, column=0, sticky=W)
        self.txtDateofBirth=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=DateofBirth, insertwidth=2)
        self.txtDateofBirth.grid(row=5, column=1)

        self.lblAge=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Age ",bd=3)
        self.lblAge.grid(row=6, column=0, sticky=W)
        self.txtAge=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Age, insertwidth=2)
        self.txtAge.grid(row=6, column=1)

        self.lblTelephone=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Telephone ",bd=3)
        self.lblTelephone.grid(row=7, column=0, sticky=W)
        self.txtTelephone=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Telephone, insertwidth=2)
        self.txtTelephone.grid(row=7, column=1)

        self.lblMedication_1=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Medication ",bd=3)
        self.lblMedication_1.grid(row=0, column=2, sticky=W)
        self.txtMedication_1=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Medication_1, insertwidth=2)
        self.txtMedication_1.grid(row=0, column=3)

        self.lblMedication_2=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Medication ",bd=3)
        self.lblMedication_2.grid(row=1, column=2, sticky=W)
        self.txtMedication_2=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Medication_2, insertwidth=2)
        self.txtMedication_2.grid(row=1, column=3)

        self.lblMedication_3=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Medication ",bd=3)
        self.lblMedication_3.grid(row=2, column=2, sticky=W)
        self.txtMedication_3=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Medication_3, insertwidth=2)
        self.txtMedication_3.grid(row=2, column=3)

        self.lblInjection=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Injection ",bd=3)
        self.lblInjection.grid(row=3, column=2, sticky=W)
        self.txtInjection=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Injection, insertwidth=2)
        self.txtInjection.grid(row=3, column=3)

        self.lblExpiring_Date=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Expiring Date ",bd=3)
        self.lblExpiring_Date.grid(row=4, column=2, sticky=W)
        self.txtExpiring_Date=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Expiring_Date, insertwidth=2)
        self.txtExpiring_Date.grid(row=4, column=3)

        self.lblPrescription=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Prescription ",bd=3)
        self.lblPrescription.grid(row=5, column=2, sticky=W)
        self.txtPrescription=Entry(RecordDetailsLEFT,font=('arial',13,'bold'),bd=3,textvariable=Prescription, insertwidth=2)
        self.txtPrescription.grid(row=5, column=3)

        self.lblDosage=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Dosage ",bd=3)
        self.lblDosage.grid(row=6, column=2, sticky=W)
        self.cboDosage=ttk.Combobox(RecordDetailsLEFT,textvariable=var1,font=('arial',13,'bold'),width=18)
        self.cboDosage['value']=('','1','2','3')
        self.cboDosage.current(0)
        self.cboDosage.grid(row=6, column=3)

        self.lblMethodofpayment=Label(RecordDetailsLEFT,font=('arial',13,'bold'),text="Payment Method ",bd=3)
        self.lblMethodofpayment.grid(row=7, column=2, sticky=W)
        self.cboMethodofpayment=ttk.Combobox(RecordDetailsLEFT,textvariable=var2,font=('arial',13,'bold'),width=18)
        self.cboMethodofpayment['value']=('','Cash','Mobile money')
        self.cboMethodofpayment.current(0)
        self.cboMethodofpayment.grid(row=7, column=3)

#=====================================================================
        self.lblRecord=Label(FrameDetails,font=('arial',10,'bold'),pady=8
        ,text="Card Number\t Firstname\t Middlename\t Surname\t Medication_1\t\t Medication_2\t\t Medication_3\t Prescription\t Injection\t Dosage\t Date")
        self.lblRecord.grid(row=0, column=0, columnspan=4)

        

        self.txtPrescription=Text(RecordDetailsRIGHT,width=80, height =17,font=('arial',10,'bold'))
        self.txtPrescription.grid(row=0, column=0, columnspan=4)

        self.txtFrameDetails=Text(FrameDetails,width=185, height =18,font=('arial',10,'bold'))
        self.txtFrameDetails.grid(row=1, column=0, columnspan=4)

#=====================================================================

        self.btnRecord=Button(MedicationDetails, padx=10, bd=4, font=('arial',12,'bold'),width=10,
        text=("Record"), command= record)
        self.btnRecord.grid(row =0,column=0)   
           
        self.btnExit=Button(MedicationDetails, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Delete"), command= Delete)
        self.btnExit.grid(row =0,column=2)

        self.btnsave=Button(MedicationDetails, padx=15, bd=4, font=('arial',12,'bold'),width=10,
        text=("Save"), command= save)
        self.btnsave.grid(row =0,column=1)



        self.btnPrint = Button(MedicationDetails, padx=15, bd=4,font=('arial',12,'bold'),width=10,
        text=("Print"))
        self.btnPrint.grid(row =0,column=3)
        
#=====================================================================





        


        


#=====================================================================
        
        


if __name__=='__main__':
    main()
    



 
