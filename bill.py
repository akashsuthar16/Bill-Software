from tkinter import *
import math,random
from tkinter import messagebox
class Bil_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Billing Software")
        bg_color="#2B547E" 
        title=Label(self.root,text="Billing Softwer",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("time new roman",30,"bold"),pady=2).pack(fill=X)
        #-------------------Variables-------------------
        #--------cosmetic-------------------------------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #--------grocery-------------------------------
        self.tea=IntVar()
        self.oil=IntVar()
        self.oreo=IntVar()
        self.salt=IntVar()
        self.rice=IntVar()
        self.atta=IntVar()
        #--------cold_drink------------------------------
        self.fizz=IntVar()
        self.cool=IntVar()
        self.froti=IntVar()
        self.limca=IntVar()
        self.maza=IntVar()
        self.sprite=IntVar()

        #--------customer-------------------------------
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill_name=StringVar()

        #--------Total Product Price & Tax Variable-------------------------------
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #------------Customber Detail Frame-----------
        F1 = LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_labl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=0,padx=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_labl=Label(F1,text="Customer Phone",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=2,padx=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_labl=Label(F1,text="Customer Billnumber",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=4,padx=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #-------Cosmetics Frame--------------------
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=350,height=380)

        bath_lbl=Label(F2,text="Bath soap",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        face_w_lbl=Label(F2,text="Face Wash",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        hair_s_lbl=Label(F2,text="Hair Spray",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        hair_g_lbl=Label(F2,text="Hair Gell",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        body_lbl=Label(F2,text="Body Loshan",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        #-------Grocery Frame--------------------
        F3 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=370,y=180,width=355,height=380)

        gro1_lbl=Label(F3,text="Tea Pati",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        gro1_txt=Entry(F3,width=10,textvariable=self.tea,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        gro2_lbl=Label(F3,text="Cooking oil",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        gro2_txt=Entry(F3,width=10,textvariable=self.oil,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        gro3_lbl=Label(F3,text="OREO",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        gro3_txt=Entry(F3,width=10,textvariable=self.oreo,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        gro4_lbl=Label(F3,text="Tata Salt",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        gro4_txt=Entry(F3,width=10,textvariable=self.salt,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        gro5_lbl=Label(F3,text="Rice",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        gro5_txt=Entry(F3,width=10,textvariable=self.rice,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        gro6_lbl=Label(F3,text="Atta",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        gro6_txt=Entry(F3,width=10,textvariable=self.atta,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        #-------Coldrink Frame--------------------
        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=740,y=180,width=360,height=380)

        cold1_lbl=Label(F4,text="Fizz App",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        cold1_txt=Entry(F4,width=10,textvariable=self.fizz,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        cold2_lbl=Label(F4,text="Amul Cool",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        cold2_txt=Entry(F4,width=10,textvariable=self.cool,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        cold3_lbl=Label(F4,text="Froti",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        cold3_txt=Entry(F4,width=10,textvariable=self.froti,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        cold4_lbl=Label(F4,text="Limca",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        cold4_txt=Entry(F4,width=10,textvariable=self.limca,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        cold5_lbl=Label(F4,text="Maza",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        cold5_txt=Entry(F4,width=10,textvariable=self.maza,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        cold6_lbl=Label(F4,text="Sprite",font=("time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        cold6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #---------------------Bill Area-----------------------------
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1118,y=180,width=400,height=380)
        bill_title=Label(F5,text="Order Bill",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #----------------ButtonFrame-----------------------
        F6 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=570,relwidth=1,height=220)
        m1_lbl=Label(F6,text="Total Consmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w") 
        m1_txt= Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        m2_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w") 
        m2_txt= Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        m3_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w") 
        m3_txt= Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)


        a1_lbl=Label(F6,text="Consmetic tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w") 
        a1_txt= Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=10,padx=10)

        a2_lbl=Label(F6,text="Cold Drink tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w") 
        a2_txt= Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,pady=10,padx=10)

        a3_lbl=Label(F6,text="Grocery tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky="w") 
        a3_txt= Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=3,pady=10,padx=10)

        #---------------btn box------------------

        btn_b=Frame(F6,bd=7,relief=GROOVE)
        btn_b.place(x=780,y=30,width=690,height=110)

        Total_btn=Button(btn_b,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,bd=5,width=11,font="arail 15 bold").grid(row=0,column=0,padx=7,pady=6)
        
        Genrate_Bill_btn=Button(btn_b,command=self.bill_area,text="Genrate Bill",bg="cadetblue",fg="white",pady=15,bd=5,width=11,font="arail 15 bold").grid(row=0,column=1,padx=7,pady=6)
        
        Clear_btn=Button(btn_b,text="Clear",bg="cadetblue",fg="white",pady=15,bd=5,width=11,font="arail 15 bold").grid(row=0,column=2,padx=7,pady=6)
        
        Exit_btn=Button(btn_b,text="Exit",bg="cadetblue",fg="white",pady=15,bd=5,width=11,font="arail 15 bold").grid(row=0,column=3,padx=7,pady=6)
        self.welcom_bill

    #----------Total Price Sum-----------------------
    def total(self):
        self.cprice_s=self.soap.get()*55
        self.cprice_fc=self.face_cream.get()*1005
        self.cprice_fw=self.face_wash.get()*123
        self.cprice_sp=self.spray.get()*82
        self.cprice_g=self.gell.get()*105
        self.cprice_l=self.loshan.get()*220
        self.total_cosmetic_price=float(
                                        self.cprice_s+
                                        self.cprice_fc+
                                        self.cprice_fw+
                                        self.cprice_sp+
                                        self.cprice_g+
                                        self.cprice_l
                                        )

        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        #-----------------Cosmetic Tax-------------------------
        self.c_tax=round((self.total_cosmetic_price*0.18),2)
        self.cosmetic_tax.set("Tax. "+str(self.c_tax))
        
        #-----------------------grocery Price------------------
        self.g_t_p=self.tea.get()*55
        self.g_o_p=self.oil.get()*1005
        self.g_or_p=self.oreo.get()*123
        self.g_s_p=self.salt.get()*82
        self.g_r_p=self.rice.get()*105
        self.g_a_p=self.atta.get()*220
        self.total_grocery_price=float(
                                        self.g_t_p+
                                        self.g_o_p+
                                        self.g_or_p+
                                        self.g_s_p+
                                        self.g_r_p+
                                        self.g_a_p
                                        )

        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        #-----------------grocery Tax-------------------------
        self.g_tax=round((self.total_grocery_price*0.07),2)
        self.grocery_tax.set("Tax. "+str(self.g_tax))

        #-----------------------cold_drink Price------------------
        self.cd_f_p=self.fizz.get()*55
        self.cd_c_p=self.cool.get()*105
        self.cd_fr_p=self.froti.get()*123
        self.cd_l_p=self.limca.get()*82
        self.cd_m_p=self.maza.get()*105
        self.cd_s_p=self.sprite.get()*220
        self.total_cold_drink_price=float(
                                        self.cd_f_p+
                                        self.cd_c_p+
                                        self.cd_fr_p+
                                        self.cd_l_p+
                                        self.cd_m_p+
                                        self.cd_s_p
                                        )

        self.cold_drink_price.set("Rs."+str(self.total_cold_drink_price))
        #-----------------cold_drink Tax-------------------------
        self.cd_tax=round((self.total_cold_drink_price*0.20),2)
        self.cold_drink_tax.set("Tax. "+str(self.cd_tax))
    
        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax
                                )

    def welcom_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcom Webcode Reatil")
        self.txtarea.insert(END,f"\n Bill No.:-{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:-{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone No.:-{self.c_phon.get()}")
        self.txtarea.insert(END,"\n============================================")
        self.txtarea.insert(END,"\n Product  \t\t   Qut    \t\t   Price")
        self.txtarea.insert(END,"\n============================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.cold_drink_price.get()=="Rs.0.0":
            messagebox.showerror("Error","No Product Puchased")
        else:
            self.welcom_bill()
            #-----------------Cosmetic-------------------------
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap  \t\t   {self.soap.get()}    \t\t   {self.cprice_s}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream  \t\t   {self.face_cream.get()}    \t\t   {self.cprice_fc}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash  \t\t   {self.face_wash.get()}    \t\t   {self.cprice_fw}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray  \t\t   {self.spray.get()}    \t\t   {self.cprice_sp}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell  \t\t   {self.gell.get()}    \t\t   {self.cprice_g}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan  \t\t   {self.loshan.get()}    \t\t   {self.cprice_l}")
            #-----------------grocery -------------------------
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea Pati \t\t   {self.tea.get()}    \t\t   {self.g_t_p}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Cooking oil  \t\t   {self.oil.get()}    \t\t   {self.g_o_p}")
            if self.oreo.get()!=0:
                self.txtarea.insert(END,f"\n OREO  \t\t   {self.oreo.get()}    \t\t   {self.g_or_p}")
            if self.salt.get()!=0:
                self.txtarea.insert(END,f"\n Tata Salt  \t\t   {self.salt.get()}    \t\t   {self.g_s_p}")
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice   \t\t   {self.rice.get()}    \t\t   {self.g_r_p}")
            if self.atta.get()!=0:
                self.txtarea.insert(END,f"\n Atta  \t\t   {self.atta.get()}    \t\t   {self.g_a_p}")
            #-----------------------cold drink------------------
            if self.fizz.get()!=0:
                self.txtarea.insert(END,f"\n Fizz App  \t\t   {self.fizz.get()}    \t\t   {self.cd_f_p}")
            if self.cool.get()!=0:
                self.txtarea.insert(END,f"\n Amul Cool  \t\t   {self.cool.get()}    \t\t   {self.cd_c_p}")
            if self.froti.get()!=0:
                self.txtarea.insert(END,f"\n Froti  \t\t   {self.froti.get()}    \t\t   {self.cd_fr_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca  \t\t   {self.limca.get()}    \t\t   {self.cd_l_p}")
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza  \t\t   {self.maza.get()}    \t\t   {self.cd_m_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite  \t\t   {self.sprite.get()}    \t\t   {self.cd_s_p}")

            self.txtarea.insert(END,"\n--------------------------------------------")
            if self.cosmetic_tax.get()!="Tax. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax  \t\t       \t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Tax. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax  \t\t       \t\t{self.grocery_tax.get()}")
            
            if self.cold_drink_tax.get()!="Tax. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax  \t\t       \t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END,"\n--------------------------------------------")
            self.txtarea.insert(END,f"\n Totale Bill  \t\t       \t\tRS.{self.Total_bill}")
            self.txtarea.insert(END,"\n--------------------------------------------")



root=Tk()
obj = Bil_App(root)
root.mainloop() 