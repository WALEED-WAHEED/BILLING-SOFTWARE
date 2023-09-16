from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Billing_App:

    # This makes the interface which is opened when we open any application
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")
        self.root.state("zoomed")
        # self.root.attributes('-fullscreen',True)

        # Decalering the variables as a database
        self.C_Name = StringVar()
        self.C_Phone = StringVar()
        self.C_Email = StringVar()
        self.C_Product = StringVar()
        self.C_Price = IntVar()
        self.C_Qty = IntVar()
        self.C_Bill_No = StringVar()
        rand = random.randint(1000,9999)
        self.C_Bill_No.set(rand)
        self.C_Search_Bill = StringVar()
        self.C_Sub_Total = StringVar()
        self.C_Tax = StringVar()
        self.C_Total = StringVar()



        # Back End of Product Frame

        # Categories
        self.Category = ["Select Option","Mobiles","Laptops","Spare Parts"]

        # Sub-Categories

        # For Select Option
        # self.Sub_Cat_SelectOption = False

        # Sub-Categories of Mobiles
        self.Sub_Cat_Mobiles = ["Oppo","Huawie","Samsung","Apple","Vivo","Infinix","Xiaomi"]

        # Sub-Categories of Laptops
        self.Sub_Cat_Laptops = ["Mac Book","HP","Dell","Lenovo"]

        # Sub-Categories of Spare-Parts
        self.Sub_Cat_SpareParts = ["RAM","Hard Disk","SSD","Windows DVD","USB"]

        # Products Name of Mobiles

        # Products Name Oppo
        self.Prod_Names_Oppo = ["OPPO A78 5G","Oppo K10 5G","Oppo F21 Pro 5G","Oppo Reno8 5G","Oppo Reno8 Pro 5G"]
        self.Price_1 = 45999
        self.Price_2 = 55999
        self.Price_3 = 60999
        self.Price_4 = 75999
        self.Price_5 = 89999

        # Products Name Huawie
        self.Prod_Names_Huawie = ["Huawei Mate 50 Pro","Huawei P50","Huawei P30 Pro","Huawei P50 Pro","Huawei Mate X2","Huawei P40 Pro","Huawei P40","Huawei P40 Pro+"]
        self.Price_6 = 33999
        self.Price_7 = 45999
        self.Price_8 = 65999
        self.Price_9 = 70999
        self.Price_10 = 94999
        self.Price_11 = 86999
        self.Price_12 = 29999
        self.Price_13 = 32999


        # Products Name Samsung
        self.Prod_Names_Samsung = ["Samsung Galaxy S23 Ultra","Samsung Galaxy A21s","Samsung Galaxy Z","Samsung Galaxy S21","Samsung Galaxy A54 5G"]
        self.Price_14 = 85999
        self.Price_15 = 96999
        self.Price_16 = 14999
        self.Price_17 = 59999
        self.Price_18 = 56999

        # Products Name Apple
        self.Prod_Names_Apple = ["iPhone 12 Pro Max","iPhone 13 Pro Max","iPhone 14 Pro Max","iPhone 11 Pro Max","iPhone XS Max"]
        self.Price_19 = 100000
        self.Price_20 = 200000
        self.Price_21 = 250000
        self.Price_22 = 300000
        self.Price_23 = 350000

        # Products Name Vivo
        self.Prod_Names_Vivo = ["Vivo T1 5G","Vivo T1 Pro 5G","Vivo T1 44W","Vivo X80","Vivo X80 Pro","Vivo X90"]
        self.Price_24 = 54999
        self.Price_25 = 45999
        self.Price_26 = 69999
        self.Price_27 = 78999
        self.Price_28 = 36999
        self.Price_29 = 79999

        # Products Name Infinix
        self.Prod_Names_Infinix = ["Smart 6 Plus","Hot 12 Play","Note 12","Note 12 5G","Note 12 Pro 5G","Smart 7","Hot 30i"]
        self.Price_30 = 65999
        self.Price_31 = 33999
        self.Price_32 = 45999
        self.Price_33 = 55999
        self.Price_34 = 36999
        self.Price_35 = 36999
        self.Price_36 = 14999

        # Products Name Xiaomi
        self.Prod_Names_Xiaomi = ["Xiaomi 12 Pro 5G","Xiaomi 11T Pro 5G","Xiaomi Mi 11X","Xiaomi 11 Lite NE 5G","Redmi Note 11"]
        self.Price_37 = 65999
        self.Price_38 = 47999
        self.Price_39 = 87999
        self.Price_40 = 78999
        self.Price_41 = 32999

        # Products Name of Laptops

        # Products Name Dell
        self.Prod_Names_Dell = ["Dell XPS 17","Dell XPS 13","Dell XPS 15","Alienware x15","Dell Inspiron","Dell Inspiron 15 3000","Alienware m17 R4","Dell G15"]
        self.Price_42 = 489999
        self.Price_43 = 369999
        self.Price_44 = 479999
        self.Price_45 = 249999
        self.Price_46 = 359999
        self.Price_47 = 149999
        self.Price_48 = 699999
        self.Price_49 = 989999

        # Products Name Hp
        self.Prod_Names_Hp = ["HP ZBook Firefly G9","HP EliteBook 840 G9","HP ZBook Studio G8","HP Chromebook x2 11","HP ZBook Fury 17 G8","HP Omen 17","HP Pavilion Aero 13","HP Elite Dragonfly G3"]
        self.Price_50 = 248999
        self.Price_51 = 456999
        self.Price_52 = 145999
        self.Price_53 = 698999
        self.Price_54 = 324999
        self.Price_55 = 486999
        self.Price_56 = 699999
        self.Price_57 = 324999

        # Products Name Mac_Book
        self.Prod_Names_Mac_Book = ["MacBook Air M2","MacBook Air M1","MacBook Pro 16-inch","MacBook Pro 14-inch","MacBook Pro 13-inch"]
        self.Price_58 = 369999
        self.Price_59 = 449999
        self.Price_60 = 899999
        self.Price_61 = 979999
        self.Price_62 = 789999

        # Products Name Lenovo
        self.Prod_Names_Lenovo = ["IdeaPad","ThinkPad","Lenovo Yoga 9 (14)","ThinkBook","Lenovo Legion Y7000"]
        self.Price_63 = 879999
        self.Price_64 = 369999
        self.Price_65 = 479999
        self.Price_66 = 789999
        self.Price_67 = 979999

        # Product Name Spare Parts

        # Products Name RAM
        self.Prod_Names_RAM = ["2 GB","4 GB","6 GB","8 GB","16 GB","32 GB"]
        self.Price_68 = 600
        self.Price_69 = 1200
        self.Price_70 = 1800
        self.Price_71 = 2400
        self.Price_72 = 3000
        self.Price_73 = 3600

        # Products Name SSD
        self.Prod_Names_SSD = ["120 GB","240 GB","360 GB","480 GB","1 TB"]
        self.Price_74 = 2800
        self.Price_75 = 5000
        self.Price_76 = 7600
        self.Price_77 = 10000
        self.Price_78 = 13000

        # Products Name HardDisk
        self.Prod_Names_Hard_Disk = ["80 GB","160 GB","240 GB","320 GB","400","1.0 TB"]
        self.Price_79 = 2000
        self.Price_80 = 3200
        self.Price_81 = 4200
        self.Price_82 = 4800
        self.Price_83 = 5600
        self.Price_84 = 7400

        # Products Name WindowsDVD
        self.Prod_Names_Windows_DVD = ["Windows 11","Windows 10","Windows 8.1","Windows 8","Windows 7","Windows Vista","Windows XP"]
        self.Price_85 = 350
        self.Price_86 = 300
        self.Price_87 = 250
        self.Price_88 = 200
        self.Price_89 = 150
        self.Price_90 = 100
        self.Price_91 = 50

        # Products Name USB
        self.Prod_Names_USB = ["2.0 GB","4.0 GB","8.0 GB","16.0 GB","32.0 GB","64.0 GB","128.0 GB"]
        self.Price_92 = 400
        self.Price_93 = 800
        self.Price_94 = 1200
        self.Price_95 = 1800
        self.Price_96 = 2300
        self.Price_97 = 2800
        self.Price_98 = 3200

        # For First Image
        img = Image.open("Images/i2.jpg")
        img = img.resize((650, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl_img = Label(self.root, image = self.photoimg)
        lbl_img.place(x = 0, y = 0, width = 650, height = 200)

        # For Second Image
        img_1 = Image.open("Images/i3.jpeg")
        img_1 = img_1.resize((650, 200), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        lbl_img_1 = Label(self.root, image = self.photoimg_1)
        lbl_img_1.place(x = 650, y = 0, width = 650, height = 200)

        # For Third Image
        img_2 = Image.open("Images/i6.jpg")
        img_2 = img_2.resize((650, 200), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        lbl_img_2 = Label(self.root, image = self.photoimg_2)
        lbl_img_2.place(x = 1300, y = 0, width = 650, height = 200)

        # Making the title of our software
        lbl_title = Label(self.root, text = "BILLING  SOFTWARE  BY WALEED WAHEED", font = ("Georgia", 40, "bold"), bg = "White", fg = "red")
        lbl_title.place(x = 0, y = 200, width = 1920, height = 70)

        # Here we use the date and time domain
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font = ("times new roman", 15, "bold"), bg = "White", fg = "blue")
        lbl.place(x = 0, y = 0, width = 200, height = 70)
        time()

        # Now we make a container or a box called Main Frame
        Main_Frame = Frame(self.root, bd = 3, relief = GROOVE, bg = "white")
        Main_Frame.place(x = 10, y = 275, width = 1905, height = 730)

        # Create a sub frame for customer
        Cust_Frame = LabelFrame(Main_Frame, text = "Customer", font = ("times new roman", 15, "bold"), bg = "white", fg = "red")
        Cust_Frame.place(x = 10, y = 5, width = 400, height = 157)

        # Sub portion of customer for customer details

        # Label and Entry of Customer's Name
        self.lbl_name = Label(Cust_Frame, text = "Name", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_name.grid(row = 0, column = 0, sticky = W, padx = 32, pady = 6)
         
        self.entry_name = ttk.Entry(Cust_Frame, textvariable = self.C_Name, font = ("times new roman", 13, "bold"), width = 25)
        self.entry_name.grid(row = 0, column = 1)

        # Label and Entry of Customer's Mobile Number
        self.lbl_mob = Label(Cust_Frame, text = "Mobile", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_mob.grid(row = 1, column = 0, sticky = W, padx = 32, pady = 6)
         
        self.entry_mob = ttk.Entry(Cust_Frame, textvariable = self.C_Phone, font = ("times new roman", 13, "bold"), width = 25)
        self.entry_mob.grid(row = 1, column = 1)

        # Label and Entry of Customer's Email
        self.lbl_email = Label(Cust_Frame, text = "Email", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_email.grid(row = 2, column = 0, sticky = W, padx = 32, pady = 6)

        self.entry_email = ttk.Entry(Cust_Frame, textvariable = self.C_Email, font = ("times new roman", 13, "bold"), width = 25)
        self.entry_email.grid(row = 2, column = 1)

        # Create a sub frame for Product
        Prod_Frame = LabelFrame(Main_Frame, text = "Product", font = ("times new roman", 15, "bold"), bg = "white", fg = "red")
        Prod_Frame.place(x = 435, y = 5, width = 943, height = 157)


        # bd = 4 nahi likha hy so error aay to remember

        # Sub portion of Product for Product details

        # Label and Entry of Category
        self.lbl_category = Label(Prod_Frame, text = "Select Category", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_category.grid(row = 0, column = 0, sticky = W, padx = 32, pady = 6)

        self.Combo_Category = ttk.Combobox(Prod_Frame, value = self.Category, font = ("times new roman", 13, "bold"), width = 25, state = "readonly")
        # =====================================
        # Showing of 0th index value on combo box
        self.Combo_Category.current(0)
        # ======================================
        self.Combo_Category.grid(row = 0, column = 1, sticky = W, padx = 32, pady = 6)
        # =====================================
        # Bind Sub Category with Category
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)
        # ======================================

        # Label and Entry of Sub_Category
        self.lbl_SubCategory = Label(Prod_Frame, text = "Sub-Category", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_SubCategory.grid(row = 1, column = 0, sticky = W, padx = 32, pady = 6)

        self.Combo_SubCategory = ttk.Combobox(Prod_Frame, value = [""], font = ("times new roman", 13, "bold"), width = 25, state = "readonly")
        self.Combo_SubCategory.grid(row = 1, column = 1, sticky = W, padx = 32, pady = 6)
        self.Combo_SubCategory.bind('<<ComboboxSelected>>', self.Product_Add)

        # Label and Entry of Products
        self.lbl_Product = Label(Prod_Frame, text = "Products Name", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_Product.grid(row = 2, column = 0, sticky = W, padx = 32, pady = 6)

        self.Combo_Product = ttk.Combobox(Prod_Frame, textvariable = self.C_Product, font = ("times new roman", 13, "bold"), width = 25, state = "readonly")
        self.Combo_Product.grid(row = 2, column = 1, sticky = W, padx = 32, pady = 6)
        self.Combo_Product.bind("<<ComboboxSelected>>", self.Price)

        # Label and Entry of Price
        self.lbl_Price = Label(Prod_Frame, text = "Price", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_Price.grid(row = 0, column = 3, sticky = W, padx = 32, pady = 6)

        self.Combo_Price = ttk.Combobox(Prod_Frame, textvariable = self.C_Price, font = ("times new roman", 13, "bold"), width = 25, state = "readonly")
        self.Combo_Price.grid(row = 0, column = 4, sticky = W, padx = 32, pady = 6)

        # Label and Entry of Quantity of the Product
        self.lbl_Quantity = Label(Prod_Frame, text = "Qty", font = ("times new roman", 15, "bold"), bg = "white")
        self.lbl_Quantity.grid(row = 1, column = 3, sticky = W, padx = 32, pady = 6)

        self.Entry_Quantity = ttk.Entry(Prod_Frame, textvariable = self.C_Qty, font = ("times new roman", 13, "bold"), width = 27)
        self.Entry_Quantity.grid(row = 1, column = 4, sticky = W, padx = 32, pady = 6)

        # Middle Frame for Middle Images
        Middle_Frame = Frame(Main_Frame, bd = 10, bg = "white")
        Middle_Frame.place(x = 0, y = 170., width = 1400, height = 400)

        # For Fourht Image
        img_4 = Image.open("Images/i1.jpg")
        img_4 = img_4.resize((700, 370), Image.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        lbl_img_4 = Label(Middle_Frame, image = self.photoimg_4)
        lbl_img_4.place(x = 0, y = 0, width = 700, height = 370)

        # For Fifth Image
        img_5 = Image.open("Images/i4.jpg")
        img_5 = img_5.resize((700, 370), Image.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        lbl_img_5 = Label(Middle_Frame, image = self.photoimg_5)
        lbl_img_5.place(x = 650, y = 0, width = 740, height = 370)

        # Bill Area on Right Frame
        Bill_Area_Frame = LabelFrame(Main_Frame, text = "Bill Area", font = ("times new roman", 15, "bold"), bg = "white", fg = "red")
        Bill_Area_Frame.place(x = 1405, y = 60, width = 485, height = 495)

        # Scroll Bar on Bill Area
        Scroll_Y = Scrollbar(Bill_Area_Frame, orient = VERTICAL)
        Scroll_Y.pack(side = RIGHT, fill = Y)

        # Making the text Area
        self.Text_Area = Text(Bill_Area_Frame, yscrollcommand = Scroll_Y.set, font = ("times new roman", 15, "bold"), bg = "white", fg = "blue")
        self.Text_Area.pack(fill = BOTH, expand = 1)

        # Now we join the both text and scroll bar with each other
        Scroll_Y.config(command = self.Text_Area.yview)

        # Make a search bar which is used to search any bill by it's number

        # Firstly make a search frame
        Search_Frame = Frame(Main_Frame, bd = 2, bg = "white")
        Search_Frame.place(x = 1400, y = 13, width = 490, height = 50)

        # Secondly make the label 'Bill Number'
        self.Bill_Number = Label(Search_Frame, text = "Bill Number", font = ("times new roman", 14, "bold"), bg = "red", fg = "white")
        self.Bill_Number.grid(row = 0, column = 0, sticky = W, padx = 4)

        #Thirdly make it's Entity
        self.Bill_Number_Entity = ttk.Entry(Search_Frame, textvariable = self.C_Search_Bill, font = ("arial", 14, "bold"), width = 20)
        self.Bill_Number_Entity.grid(row = 0, column = 1, sticky = W, padx = 4)

        # Forthly make a search button for the label of 'Bill Number'
        self.Btn_Bill_Number = Button(Search_Frame, command = self.Find_Bill, text = "Search", font = ("arial", 11, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Bill_Number.grid(row = 0, column = 2, sticky = W, padx = 4)

        # Now we make Total Bill Counter
        Bill_Counter_Frame = LabelFrame(Main_Frame, text = "Bill Counter", font = ("times new roman", 15, "bold"), bg = "white", fg = "red")
        Bill_Counter_Frame.place(x = 10, y = 565, width = 1880, height = 150)

        # Putting Options in the Bill Counter Frame

        # Sub Total bill in BIll Counter Frame
        self.Sub_Total = Label(Bill_Counter_Frame, text = "Sub Total", font = ("times new roman", 13, "bold"), bg = "white")
        self.Sub_Total.grid(row = 0, column = 0, sticky = W, padx = 12, pady = 7)

        self.Sub_Total_Entry = ttk.Entry(Bill_Counter_Frame, textvariable = self.C_Sub_Total, font = ("times new roman", 11, "bold"), width = 25)
        self.Sub_Total_Entry.grid(row = 0, column = 1, sticky = W, padx = 12, pady = 7)

        # Government Tax in BIll Counter Frame
        self.Gov_tax = Label(Bill_Counter_Frame, text = "Gov Tax", font = ("times new roman", 13, "bold"), bg = "white")
        self.Gov_tax.grid(row = 1, column = 0, sticky = W, padx = 12, pady = 7)

        self.Sub_Total_Entry = ttk.Entry(Bill_Counter_Frame, textvariable = self.C_Tax, font = ("times new roman", 11, "bold"), width = 25)
        self.Sub_Total_Entry.grid(row = 1, column = 1, sticky = W, padx = 12, pady = 7)

        # Total bill in BIll Counter Frame
        self.Sub_Total = Label(Bill_Counter_Frame, text = "Total", font = ("times new roman", 13, "bold"), bg = "white")
        self.Sub_Total.grid(row = 2, column = 0, sticky = W, padx = 12, pady = 7)

        self.Sub_Total_Entry = ttk.Entry(Bill_Counter_Frame, textvariable = self.C_Total, font = ("times new roman", 11, "bold"), width = 25)
        self.Sub_Total_Entry.grid(row = 2, column = 1, sticky = W, padx = 12, pady = 7)

        # Button Sub Frame in Billing Counter
        Button_Frame = Frame(Bill_Counter_Frame, bd = 2, bg = "white")
        Button_Frame.place(x = 480, y = 30)

        # Add to Cart Button
        self.Btn_Add_To_Cart = Button(Button_Frame, command = self.AddItem, text = "Add To Cart", font = ("times new roman", 15, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Add_To_Cart.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 7)

        # Generate Bill Button
        self.Btn_Generate_Bill = Button(Button_Frame, command = self.Gen_Bill, text = "Generate Bill", font = ("times new roman", 15, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Generate_Bill.grid(row = 0, column = 1, sticky = W, padx = 20, pady = 7)

        # Save Bill Button
        self.Btn_Save_Bill = Button(Button_Frame, command = self.Save, text = "Save Bill", font = ("times new roman", 15, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Save_Bill.grid(row = 0, column = 2, sticky = W, padx = 20, pady = 7)

        # Print Button
        self.Btn_Print = Button(Button_Frame, command = self.iprint, text = "Print", font = ("times new roman", 15, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Print.grid(row = 0, column = 3, sticky = W, padx = 20, pady = 7)

        # Clear Button
        self.Btn_Clear = Button(Button_Frame, command = self.Clear, text = "Clear", font = ("times new roman", 15, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Clear.grid(row = 0, column = 4, sticky = W, padx = 20, pady = 7)

        # Exit Button
        self.Btn_Exit = Button(Button_Frame,command = self.root.destroy, text = "Exit", font = ("times new roman", 15, "bold"), bg = "orangered", fg = "white", height = 1, width = 13, cursor = "hand2")
        self.Btn_Exit.grid(row = 0, column = 5, sticky = W, padx = 20, pady = 7)

        # Calling the welcome Function
        self.Welcome()

        # List that get all the Customer Added Items
        self.Items_List = []

    # Add to Cart Button Backend is within a function
    def AddItem(self):
        self.p = self.C_Price.get()
        self.q = self.C_Qty.get()
        self.multi = self.p * self.q
        self.Items_List.append(self.multi)
        if self.C_Product.get() == "":
            messagebox.showerror("Error", "Please Select the Product !!!")
        else:   # Work on it and simplify it
            Tax = 100
            self.Text_Area.insert(END, f"\n   {self.C_Product.get()} \t\t\t {self.C_Qty.get()} \t       {self.multi}")
            self.C_Sub_Total.set(str('Rs.%.2f'%(sum(self.Items_List))))
            self.C_Tax.set(str('Rs.%.2f'%((((sum(self.Items_List)) - (self.C_Price.get())) * Tax) / 100 )))
            self.C_Total.set(str('Rs.%.2f'%(((sum(self.Items_List)) + ((((sum(self.Items_List)) - (self.C_Price.get())) * Tax) / 100 )))))
    
    # Generate Bill Backend Coding
    def Gen_Bill(self):
        if self.C_Product.get() == "":
            messagebox.showerror("Error", "Please Add To Cart Product !!!")
        else:
            text = self.Text_Area.get(10.0,(10.0 + float(len(self.Items_List))))
            self.Welcome()
            self.Text_Area.insert(END, text)
            self.Text_Area.insert(END, "\n =========================================")
            self.Text_Area.insert(END, f"\n Sub Aomunt : \t\t {self.C_Sub_Total.get()}")
            self.Text_Area.insert(END, f"\n Tax Aomunt : \t\t {self.C_Tax.get()}")
            self.Text_Area.insert(END, f"\n Total Aomunt : \t\t {self.C_Total.get()}")
            self.Text_Area.insert(END, "\n =========================================")

    # Back end to save bill button
    def Save(self):
        message = messagebox.askyesno("Save Bill", "Do you want to save the Bill")
        if message > 0:
            self.Bill_Data = self.Text_Area.get(1.0, END)
            file = open("Bills/"+str(self.C_Bill_No.get())+".txt","w")
            file.write(self.Bill_Data)
            message = messagebox.showinfo("Save", f"Bill Number : {self.C_Bill_No.get()} Saved Successfully")
            file.close()

    # Backend of print button
    def iprint(self):
        data = self.Text_Area.get(1.0, "end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename, 'w').write(data)
        os.startfile(filename, "print")

    def Find_Bill(self):
        found = "File Not Found"
        for i in os.listdir("Bills/"):
            if i.split(".")[0] == self.C_Search_Bill.get():
                f1 = open(f'Bills/{i}','r')
                self.Text_Area.delete(1.0, END)
                for d in f1:
                    self.Text_Area.insert(END, d)
                    f1.close
                    found = "File Found"
        if found == "File Not Found":
            messagebox.showerror("Error", "Invalid Bill Not Found")

    # Backend of Clear Button
    def Clear(self):
        self.Text_Area.delete(1.0, END)
        self.C_Name.set("")
        self.C_Phone.set("")
        self.C_Email.set("")
        self.C_Product.set("")
        self.C_Price.set(0)
        self.C_Qty.set(0)
        self.C_Bill_No.set(str(X))
        self.C_Search_Bill.set("")
        self.C_Sub_Total.set("")
        self.C_Tax.set("") # Either in a single quotation
        self.C_Total.set("")
        self.Items_List = [0]

    # Make the Auto Intro of the Billing Area
    def Welcome(self):
        self.Text_Area.delete(1.0, END)
        self.Text_Area.insert(END, "\t              Welcome To My Mart")
        self.Text_Area.insert(END, f"\n Bill Number : {self.C_Bill_No.get()}")
        self.Text_Area.insert(END, f"\n Customer Name : {self.C_Name.get()}")
        self.Text_Area.insert(END, f"\n Phone Number : {self.C_Phone.get()}")
        self.Text_Area.insert(END, f"\n Customer Email : {self.C_Email.get()}")

        self.Text_Area.insert(END, "\n =========================================")
        self.Text_Area.insert(END, "\n Product \t\t\t Qty \t      Price")
        self.Text_Area.insert(END, "\n =========================================\n")

    # Back End of Binding or combining of Catagory,  Sub-Catagory, Products and Price

    # Combine Catagory with Sub-Catogory
    def Categories(self, event = ""):
        if self.Combo_Category.get() == "Mobiles":
            self.Combo_SubCategory.config(values = self.Sub_Cat_Mobiles)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Laptops":
            self.Combo_SubCategory.config(values = self.Sub_Cat_Laptops)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Spare Parts":
            self.Combo_SubCategory.config(values = self.Sub_Cat_SpareParts)
            self.Combo_SubCategory.current(0)

        # if self.Combo_Category.get() == "Select Option":
        #     self.Combo_SubCategory.config(values = self.Sub_Cat_SelectOption)
        #     self.Combo_SubCategory.current(0)
    
    def Product_Add(self, event = ""):

        # Combining Sub_Category of Mobiles with it's Products
        if self.Combo_SubCategory.get() == "Oppo":
            self.Combo_Product.config(values = self.Prod_Names_Oppo)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Huawie":
            self.Combo_Product.config(values = self.Prod_Names_Huawie)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Samsung":
            self.Combo_Product.config(values = self.Prod_Names_Samsung)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Apple":
            self.Combo_Product.config(values = self.Prod_Names_Apple)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Vivo":
            self.Combo_Product.config(values = self.Prod_Names_Vivo)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Infinix":
            self.Combo_Product.config(values = self.Prod_Names_Infinix)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Xiaomi":
            self.Combo_Product.config(values = self.Prod_Names_Xiaomi)
            self.Combo_Product.current(0)
    
        # Combine Sub_Category of Laptops with it's Products
        if self.Combo_SubCategory.get() == "Lenovo":
            self.Combo_Product.config(values = self.Prod_Names_Lenovo)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Dell":
            self.Combo_Product.config(values = self.Prod_Names_Dell)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "HP":
            self.Combo_Product.config(values = self.Prod_Names_Hp)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Mac Book":
            self.Combo_Product.config(values = self.Prod_Names_Mac_Book)
            self.Combo_Product.current(0)

        # Combine Sub_Categories of Spare Parts with it's Products
        if self.Combo_SubCategory.get() == "USB":
            self.Combo_Product.config(values = self.Prod_Names_USB)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "RAM":
            self.Combo_Product.config(values = self.Prod_Names_RAM)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Hard Disk":
            self.Combo_Product.config(values = self.Prod_Names_Hard_Disk)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "SSD":
            self.Combo_Product.config(values = self.Prod_Names_SSD)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get() == "Windows DVD":
            self.Combo_Product.config(values = self.Prod_Names_Windows_DVD)
            self.Combo_Product.current(0)

    def Price(self, event = ""):

        # Add prices of Mobile elements to it's prices

        # Add prices of Oppo Mobile elements to it's prices
        if self.Combo_Product.get() == "OPPO A78 5G":
            self.Combo_Price.config(value = self.Price_1)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Oppo K10 5G":
            self.Combo_Price.config(value = self.Price_2)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Oppo F21 Pro 5G":
            self.Combo_Price.config(value = self.Price_3)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Oppo Reno8 5G":
            self.Combo_Price.config(value = self.Price_4)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Oppo Reno8 Pro 5G":
            self.Combo_Price.config(value = self.Price_5)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)
        
        # Add prices of Huawie Mobile elements to it's prices
        if self.Combo_Product.get() == "Huawei Mate 50 Pro":
            self.Combo_Price.config(value = self.Price_6)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei P50":
            self.Combo_Price.config(value = self.Price_7)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei P30 Pro":
            self.Combo_Price.config(value = self.Price_8)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei P50 Pro":
            self.Combo_Price.config(value = self.Price_9)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei Mate X2":
            self.Combo_Price.config(value = self.Price_10)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei P40 Pro":
            self.Combo_Price.config(value = self.Price_11)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei P40":
            self.Combo_Price.config(value = self.Price_12)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Huawei P40 Pro+":
            self.Combo_Price.config(value = self.Price_13)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Samsung Mobile elements to it's prices
        if self.Combo_Product.get() == "Samsung Galaxy S23 Ultra":
            self.Combo_Price.config(value = self.Price_14)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Samsung Galaxy A21s":
            self.Combo_Price.config(value = self.Price_15)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Samsung Galaxy Z":
            self.Combo_Price.config(value = self.Price_16)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Samsung Galaxy S21":
            self.Combo_Price.config(value = self.Price_17)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Samsung Galaxy A54 5G":
            self.Combo_Price.config(value = self.Price_18)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)
        
        # Add prices of I-Phone Mobile elements to it's prices
        if self.Combo_Product.get() == "iPhone 12 Pro Max":
            self.Combo_Price.config(value = self.Price_19)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "iPhone 13 Pro Max":
            self.Combo_Price.config(value = self.Price_20)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "iPhone 14 Pro Max":
            self.Combo_Price.config(value = self.Price_21)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "iPhone 11 Pro Max":
            self.Combo_Price.config(value = self.Price_22)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "iPhone XS Max":
            self.Combo_Price.config(value = self.Price_23)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Vivo Mobile elements to it's prices
        if self.Combo_Product.get() == "Vivo T1 5G":
            self.Combo_Price.config(value = self.Price_24)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Vivo T1 Pro 5G":
            self.Combo_Price.config(value = self.Price_25)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Vivo T1 44W":
            self.Combo_Price.config(value = self.Price_26)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)
        
        if self.Combo_Product.get() == "Vivo X80":
            self.Combo_Price.config(value = self.Price_27)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Vivo X80 Pro":
            self.Combo_Price.config(value = self.Price_28)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Vivo X90":
            self.Combo_Price.config(value = self.Price_29)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Infinix Mobile elements to it's prices
        if self.Combo_Product.get() == "Smart 6 Plus":
            self.Combo_Price.config(value = self.Price_30)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Hot 12 Play":
            self.Combo_Price.config(value = self.Price_31)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Note 12":
            self.Combo_Price.config(value = self.Price_32)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)
        
        if self.Combo_Product.get() == "Note 12 5G":
            self.Combo_Price.config(value = self.Price_33)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Note 12 Pro 5G":
            self.Combo_Price.config(value = self.Price_34)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Smart 7":
            self.Combo_Price.config(value = self.Price_35)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Hot 30i":
            self.Combo_Price.config(value = self.Price_36)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Xiaomi Mobile elements to it's prices
        if self.Combo_Product.get() == "Xiaomi 12 Pro 5G":
            self.Combo_Price.config(value = self.Price_37)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Xiaomi 11T Pro 5G":
            self.Combo_Price.config(value = self.Price_38)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Xiaomi Mi 11X":
            self.Combo_Price.config(value = self.Price_39)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)
        
        if self.Combo_Product.get() == "Xiaomi 11 Lite NE 5G":
            self.Combo_Price.config(value = self.Price_40)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Redmi Note 11":
            self.Combo_Price.config(value = self.Price_41)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Laptop elements to it's prices

        # Add prices of Dell Laptop elements to it's prices
        if self.Combo_Product.get() == "Dell XPS 17":
            self.Combo_Price.config(value = self.Price_42)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Dell XPS 13":
            self.Combo_Price.config(value = self.Price_43)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Dell XPS 15":
            self.Combo_Price.config(value = self.Price_44)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Alienware x15":
            self.Combo_Price.config(value = self.Price_45)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Dell Inspiron":
            self.Combo_Price.config(value = self.Price_46)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Dell Inspiron 15 3000":
            self.Combo_Price.config(value = self.Price_47)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Alienware m17 R4":
            self.Combo_Price.config(value = self.Price_48)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Dell G15":
            self.Combo_Price.config(value = self.Price_49)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Hp Laptop elements to it's prices
        if self.Combo_Product.get() == "HP ZBook Firefly G9":
            self.Combo_Price.config(value = self.Price_50)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP EliteBook 840 G9":
            self.Combo_Price.config(value = self.Price_51)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP ZBook Studio G8":
            self.Combo_Price.config(value = self.Price_52)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP Chromebook x2 11":
            self.Combo_Price.config(value = self.Price_53)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP ZBook Fury 17 G8":
            self.Combo_Price.config(value = self.Price_54)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP Omen 17":
            self.Combo_Price.config(value = self.Price_55)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP Pavilion Aero 13":
            self.Combo_Price.config(value = self.Price_56)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "HP Elite Dragonfly G3":
            self.Combo_Price.config(value = self.Price_57)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Mac Book Laptop elements to it's prices
        if self.Combo_Product.get() == "MacBook Air M2":
            self.Combo_Price.config(value = self.Price_58)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "MacBook Air M1":
            self.Combo_Price.config(value = self.Price_59)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "MacBook Pro 16-inch":
            self.Combo_Price.config(value = self.Price_60)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "MacBook Pro 14-inch":
            self.Combo_Price.config(value = self.Price_61)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "MacBook Pro 13-inch":
            self.Combo_Price.config(value = self.Price_62)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Lenovo Laptop elements to it's prices
        if self.Combo_Product.get() == "IdeaPad":
            self.Combo_Price.config(value = self.Price_63)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "ThinkPad":
            self.Combo_Price.config(value = self.Price_64)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Lenovo Yoga 9 (14)":
            self.Combo_Price.config(value = self.Price_65)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "ThinkBook":
            self.Combo_Price.config(value = self.Price_66)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Lenovo Legion Y7000":
            self.Combo_Price.config(value = self.Price_67)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Spare Parts elements to it's prices

        # Add prices of RAM elements to it's prices
        if self.Combo_Product.get() == "2 GB":
            self.Combo_Price.config(value = self.Price_68)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "4 GB":
            self.Combo_Price.config(value = self.Price_69)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "6 GB":
            self.Combo_Price.config(value = self.Price_70)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "8 GB":
            self.Combo_Price.config(value = self.Price_71)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "16 GB":
            self.Combo_Price.config(value = self.Price_72)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "32 GB":
            self.Combo_Price.config(value = self.Price_73)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of SSD elements to it's prices
        if self.Combo_Product.get() == "120 GB":
            self.Combo_Price.config(value = self.Price_74)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "240 GB":
            self.Combo_Price.config(value = self.Price_75)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "360 GB":
            self.Combo_Price.config(value = self.Price_76)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "480 GB":
            self.Combo_Price.config(value = self.Price_77)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "1 TB":
            self.Combo_Price.config(value = self.Price_78)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Hard Disk elements to it's prices
        if self.Combo_Product.get() == "80 GB":
            self.Combo_Price.config(value = self.Price_79)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "160 GB":
            self.Combo_Price.config(value = self.Price_80)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "240 GB":
            self.Combo_Price.config(value = self.Price_81)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "320 GB":
            self.Combo_Price.config(value = self.Price_82)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "400":
            self.Combo_Price.config(value = self.Price_83)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "1.0 TB":
            self.Combo_Price.config(value = self.Price_84)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of Windows DVD elements to it's prices
        if self.Combo_Product.get() == "Windows 11":
            self.Combo_Price.config(value = self.Price_85)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Windows 10":
            self.Combo_Price.config(value = self.Price_86)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Windows 8.1":
            self.Combo_Price.config(value = self.Price_87)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Windows 8":
            self.Combo_Price.config(value = self.Price_88)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Windows 7":
            self.Combo_Price.config(value = self.Price_89)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Windows Vista":
            self.Combo_Price.config(value = self.Price_90)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "Windows XP":
            self.Combo_Price.config(value = self.Price_91)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        # Add prices of USB elements to it's prices
        if self.Combo_Product.get() == "2.0 GB":
            self.Combo_Price.config(value = self.Price_92)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "4.0 GB":
            self.Combo_Price.config(value = self.Price_93)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "8.0 GB":
            self.Combo_Price.config(value = self.Price_94)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "16.0 GB":
            self.Combo_Price.config(value = self.Price_95)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "32.0 GB":
            self.Combo_Price.config(value = self.Price_96)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "64.0 GB":
            self.Combo_Price.config(value = self.Price_97)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        if self.Combo_Product.get() == "128.0 GB":
            self.Combo_Price.config(value = self.Price_98)
            self.Combo_Price.current(0)
            self.C_Qty.set(1)

        






       




        





if __name__ == '__main__':
    root = Tk()
    obj = Billing_App(root)
    root.mainloop()