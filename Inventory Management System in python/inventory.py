from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime


class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory System")
        self.root.geometry("1528x828+0+0")
        self.root.configure(background='powder blue')

        title = Label(self.root, text="Inventory Management System", bd=10, relief=GROOVE, font=(
            "times new roman", 40, "bold"), bg="#ffbf00", fg="#0000ff")
        title.pack(side=TOP, fill=X)
# ===========================frames==========================================
        mainFrame = Frame(self.root, bd=20, width=1535,
                          height=836, bg="cadet blue", relief=RIDGE)
        mainFrame.pack()

        leftFrame = Frame(mainFrame, bd=10, width=900,
                          height=798, padx=10, bg="powder blue", relief=RIDGE)
        leftFrame.pack(side=LEFT)

        rightFrame = Frame(mainFrame, bd=10, width=600,
                           height=798, padx=10, bg="powder blue", relief=RIDGE)
        rightFrame.pack(side=RIGHT)

# ===========================frames for the following widger, Text, labels entry widget=========================
        leftFrame0 = Frame(leftFrame, bd=5, width=790,
                           height=195, padx=5, bg="powder blue", relief=RIDGE)
        leftFrame0.grid(row=0, column=0)
        leftFrame1 = Frame(leftFrame, bd=5, width=790,
                           height=195, padx=5, bg="powder blue", relief=RIDGE)
        leftFrame1.grid(row=1, column=0)
        leftFrame2 = Frame(leftFrame, bd=5, width=790,
                           height=195, padx=5, bg="powder blue", relief=RIDGE)
        leftFrame2.grid(row=2, column=0)
        leftFrame3 = Frame(leftFrame, bd=5, width=790,
                           height=100, padx=5, bg="powder blue", relief=RIDGE)
        leftFrame3.grid(row=3, column=0)

        rightFrame0 = Frame(rightFrame, bd=5, width=620,
                            height=260, padx=5, bg="powder blue", relief=RIDGE)
        rightFrame0.grid(row=0, column=0)
        rightFrame1 = Frame(rightFrame, bd=5, width=620,
                            height=376, padx=5, bg="powder blue", relief=RIDGE)
        rightFrame1.grid(row=1, column=0)
        rightFrame2 = Frame(rightFrame, bd=5, width=620,
                            height=100, padx=5, bg="powder blue", relief=RIDGE)
        rightFrame2.grid(row=2, column=0)

        AcctOpen = StringVar()
        AppDate = StringVar()
        NextCreditReview = StringVar()
        LastCreditReview = StringVar()
        DateReview = StringVar()
        ProdCode = StringVar()
        ProdType = StringVar()
        NoDays = StringVar()
        CostPDay = StringVar()
        CreLimit = StringVar()
        CreCheck = StringVar()
        SettDueDay = StringVar()
        PaymentD = StringVar()
        Discount = StringVar()
        Deposit = StringVar()
        PayDueDay = StringVar()
        PaymentM = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()
        iExit = StringVar()
        Receipt_Ref = StringVar()

        def Product():
            values = str(self.lblProdType.get())
            pType = values
            if pType == "Lawnmower":
                ProdCode.set("LAM918")
                CostPDay.set("12")
                CreCheck.set("No")
                SettDueDay.set("12")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Cash")

                n = float(self.LastCreditReview.get())
                s = float(self.SettDueDay.get())
                price = (n * s)
                TC = "Tk", str('%.2f' % (price))
                PayDueDay.set(TC)

        def ChackCredit():
            if (var1.get() == 1):
                self.txtInfo.insert(END, "\tCheck Credit Approved\n")
            elif var1.get() == 0:
                self.txtInfo.delete("1.0", END)

        def TermAgreed():
            if (var2.get() == 1):
                self.txtInfo.insert(END, "\tTerm Agreed\n")
            elif var2.get() == 0:
                self.txtInfo.delete("1.0", END)

        def AcctOnHold():
            if (var3.get() == 1):
                self.txtInfo.insert(END, "\tAccount On Hold\n")
            elif var3.get() == 0:
                self.txtInfo.delete("1.0", END)

        def RestrictedMails():
            if (var4.get() == 1):
                self.txtInfo.insert(END, "\tTerm Agreed\n")
            elif var4.get() == 0:
                self.txtInfo.delete("1.0", END)

        def Reset():
            AcctOpen.set("")
            AppDate.set("")
            NextCreditReview.set("")
            LastCreditReview.set("")
            DateReview.set("")
            ProdCode.set("")
            ProdType.set("")
            NoDays.set("")
            CostPDay.set("")
            CreLimit.set("")
            CreCheck.set("")
            SettDueDay.set("")
            PaymentD.set("")
            Discount.set("")
            Deposit.set("")
            PayDueDay.set("")
            PaymentM.set("")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            Tax.set(0)
            SubTotal.set("")
            Total.set("")
            self.txtinfo.delete("1.0", END)
            self.txtReceipt.delete("1.0", END)
            return

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Inventory System", "Confirm if you want to exit")
            if iExit > 0:
                root.destory()
                return

        def iDates(evt):
            values = str(self.lblNoDays.get())
            NDays = values
            if NDays == "1-30":
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=30)
                d3 = (d1 + d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(30)
                DateReview.set(d3)

                CreLimit.set("150 Tk")
                Discount.set("5%")
                AcctOpen.set("Yes")
            elif (NDays == "31-90"):
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=90)
                d3 = (d1 + d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(90)
                DateReview.set(d3)

                CreLimit.set("200 Tk")
                Discount.set("10%")
                AcctOpen.set("Yes")

            elif (NDays == "91-270"):
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=270)
                d3 = (d1 + d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(270)
                DateReview.set(d3)

                CreLimit.set("250 Tk")
                Discount.set("15%")
                AcctOpen.set("Yes")

            elif (NDays == "270-365"):
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=365)
                d3 = (d1 + d2)
                AppDate.set(d1)
                NextCreditReview.set(d3)
                LastCreditReview.set(365)
                DateReview.set(d3)

                CreLimit.set("300 Tk")
                Discount.set("20%")
                AcctOpen.set("Yes")

            elif (NDays == "0"):
                messagebox.showinfo("Zero Selected", "you Choose Zero?")
                Reset()


# ===========================leftFrame0=======================================
        self.lblProdType = Label(leftFrame0, font=(
            'arial', 18, 'bold'), text="Prod Type:", padx=2, pady=2, bg="powder blue")
        self.lblProdType.grid(row=0, column=0, sticky=W)

        self.lblProdType = ttk.Combobox(
            leftFrame0, textvariable=ProdType, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.lblProdType.bind("<<ComboboxSelected>>", Product)
        self.lblProdType['value'] = (
            '', 'Lawnmower', 'Pickup Van', 'Cement Mixer', 'Elec. Generator')
        self.lblProdType.current(0)
        self.lblProdType.grid(row=0, column=1)
# ====
        self.lblNoDays = Label(leftFrame0, font=(
            'arial', 18, 'bold'), text="No of Days", padx=2, pady=2, bg="powder blue")
        self.lblNoDays.grid(row=0, column=2, sticky=W)

        self.lblNoDays = ttk.Combobox(
            leftFrame0, textvariable=NoDays, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.lblNoDays.bind("<<ComboboxSelected>>", iDates)
        self.lblNoDays['value'] = ('0', '1-30', '31-90', '91-270', '270-365')
        self.lblNoDays.current(0)
        self.lblNoDays.grid(row=0, column=3)


# ====
        self.lblProdCode = Label(leftFrame0, font=(
            'arial', 16, 'bold'), text="Product Code:", padx=1, pady=16, bg="powder blue")
        self.lblProdCode.grid(row=1, column=0, sticky=W)

        self.txtProdCode = Entry(
            leftFrame0, textvariable=ProdCode, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=RIGHT).grid(row=1, column=1)

# ====
        self.lblProdCode = Label(leftFrame0, font=(
            'arial', 16, 'bold'), text="Product Code:", padx=1, pady=2, bg="powder blue")
        self.lblProdCode.grid(row=1, column=2, sticky=W)

        self.txtProdCode = Entry(
            leftFrame0, textvariable=CostPDay, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=RIGHT).grid(row=1, column=3)


# ===========================leftFrame1=======================================
        self.lblCreLimit = Label(leftFrame1, font=(
            'arial', 18, 'bold'), text="Credit Limit:", padx=2, pady=2, bg="powder blue")
        self.lblCreLimit.grid(row=0, column=0, sticky=W)

        self.lblCreLimit = ttk.Combobox(
            leftFrame1, textvariable=CreLimit, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.lblCreLimit['value'] = (
            '', 'Select an option', '150 Tk', '200 Tk', '250 TK', '300 Tk')
        self.lblCreLimit.current(0)
        self.lblCreLimit.grid(row=0, column=1, pady=8)
# ===
        self.lblCreCheck = Label(leftFrame1, font=(
            'arial', 18, 'bold'), text="Credit Check:", padx=2, pady=2, bg="powder blue")
        self.lblCreCheck.grid(row=0, column=2, sticky=W)

        self.lblCreCheck = ttk.Combobox(
            leftFrame1, textvariable=CreCheck, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.lblCreCheck['value'] = ('', 'Select an option', 'Yes', 'No')
        self.lblCreCheck.current(0)
        self.lblCreCheck.grid(row=0, column=3, pady=8)
# ====
        self.lblSettDueDay = Label(leftFrame1, font=(
            'arial', 16, 'bold'), text="Sett.Due:", padx=2, pady=2, bg="powder blue")
        self.lblSettDueDay.grid(row=1, column=0, sticky=W)

        self.txtSettDueDay = Entry(
            leftFrame1, textvariable=SettDueDay, font=('arial', 16, 'bold'), bd=2, fg="black", width=14, justify=RIGHT).grid(row=1, column=1)

# ===
        self.lblPaymentD = Label(leftFrame1, font=(
            'arial', 18, 'bold'), text="Payment Due:", padx=2, pady=2, bg="powder blue")
        self.lblPaymentD.grid(row=1, column=2, sticky=W)

        self.lblPaymentD = ttk.Combobox(
            leftFrame1, textvariable=PaymentD, state='readonly', font=('arial', 18, 'bold'), width=10)
        self.lblPaymentD['value'] = ('', 'Select an option', 'Yes', 'No')
        self.lblPaymentD.current(0)
        self.lblPaymentD.grid(row=1, column=3, pady=8)

# ===
        self.lblDiscount = Label(leftFrame1, font=(
            'arial', 18, 'bold'), text="Discount:", padx=2, pady=2, bg="powder blue")
        self.lblDiscount.grid(row=2, column=0, sticky=W)

        self.lblDiscount = ttk.Combobox(
            leftFrame1, textvariable=Discount, state='readonly', font=('arial', 18, 'bold'), width=10)
        self.lblDiscount['value'] = ('0', '5', '10', '15', '20')
        self.lblDiscount.current(0)
        self.lblDiscount.grid(row=2, column=1, pady=8)

# ===
        self.lblDeposit = Label(leftFrame1, font=(
            'arial', 18, 'bold'), text="Deposit:", padx=2, pady=2, bg="powder blue")
        self.lblDeposit.grid(row=2, column=2, sticky=W)

        self.lblDeposit = ttk.Combobox(
            leftFrame1, textvariable=Deposit, state='readonly', font=('arial', 18, 'bold'), width=10)
        self.lblDeposit['value'] = ('', 'Select an option', 'Yes', 'No')
        self.lblDeposit.current(0)
        self.lblDeposit.grid(row=2, column=3, pady=8)
# ====
        self.lblPayDueDay = Label(leftFrame1, font=(
            'arial', 16, 'bold'), text="Pay Due Day:", padx=1, pady=2, bg="powder blue")
        self.lblPayDueDay.grid(row=3, column=0, sticky=W)

        self.txtPayDueDay = Entry(
            leftFrame1, textvariable=PayDueDay, font=('arial', 16, 'bold'), bd=2, fg="black", width=14, justify=RIGHT).grid(row=3, column=1)
# ===
        self.lblPaymentM = Label(leftFrame1, font=(
            'arial', 18, 'bold'), text="Payment Method:", padx=2, pady=2, bg="powder blue")
        self.lblPaymentM.grid(row=3, column=2, sticky=W)

        self.lblPaymentM = ttk.Combobox(
            leftFrame1, textvariable=PaymentM, state='readonly', font=('arial', 18, 'bold'), width=10)
        self.lblPaymentM['value'] = (
            '', 'Select an option', 'Cash', 'Visa Card', 'Master Card')
        self.lblPaymentM.current(0)
        self.lblPaymentM.grid(row=3, column=3, pady=8)


# ===========================leftFrame2=======================================
        leftFrame2LL = Frame(leftFrame2, bd=5, width=300,
                             height=160, padx=5, bg="powder blue", relief=RIDGE)
        leftFrame2LL.grid(row=0, column=0)
        leftFrame2LR = Frame(leftFrame2, bd=5, width=300,
                             height=160, padx=5, bg="cadet blue", relief=RIDGE)
        leftFrame2LR.grid(row=0, column=1)

        self.chkCheckCredir = Checkbutton(leftFrame2LL, text="Check Credit", variable=var1, onvalue=1, offvalue=0, font=(
            'arial', 16, 'bold'), bg="powder blue", command=ChackCredit).grid(row=0, sticky=W)
        self.chkTermAgreed = Checkbutton(leftFrame2LL, text="Term  Agreed", variable=var2, onvalue=1, offvalue=0, font=(
            'arial', 16, 'bold'), bg="powder blue", command=TermAgreed).grid(row=1, sticky=W)
        self.chkAccountOnHold = Checkbutton(leftFrame2LL, text="Account On Hold ", variable=var3, onvalue=1, offvalue=0, font=(
            'arial', 16, 'bold'), bg="powder blue", command=AcctOnHold).grid(row=2, sticky=W)
        self.chkRestrictMailing = Checkbutton(leftFrame2LL, text="Restrict Mailing ", variable=var4, onvalue=1, offvalue=0, font=(
            'arial', 16, 'bold'), bg="powder blue", command=RestrictedMails).grid(row=3, sticky=W)
        self.txtinfo = Text(leftFrame2LR, height=9,
                            width=63, font=('arial', 9, 'bold'))
        self.txtinfo.grid(row=0, column=0, pady=2)

# ===========================leftFrame3=======================================
        self.lblTax = Label(leftFrame3, font=(
            'arial', 18, 'bold'), text="Tax", padx=14, pady=4, bg="powder blue")
        self.lblTax.grid(row=0, column=0, sticky=W)
        self.txtTax = Entry(
            leftFrame3, textvariable=Tax, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=LEFT).grid(row=1, column=0, padx=23, pady=5)

        self.lblSubTotal = Label(leftFrame3, font=(
            'arial', 18, 'bold'), text="Sub Total", padx=14, pady=4, bg="powder blue")
        self.lblSubTotal.grid(row=0, column=1, sticky=W)
        self.lblSubTotal = Entry(
            leftFrame3, textvariable=SubTotal, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=LEFT).grid(row=1, column=1, padx=23, pady=5)

        self.lblTotal = Label(leftFrame3, font=(
            'arial', 18, 'bold'), text="Total", padx=14, pady=4, bg="powder blue")
        self.lblTotal.grid(row=0, column=2, sticky=W)
        self.lblTotal = Entry(
            leftFrame3, textvariable=Total, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=LEFT).grid(row=1, column=2, padx=23, pady=5)
# ===========================rightFrame0=======================================
        self.lblAcctOpen = Label(rightFrame0, font=(
            'arial', 18, 'bold'), text="Account Opended", padx=2, pady=2, bg="powder blue")
        self.lblAcctOpen.grid(row=0, column=0, sticky=W)

        self.lblAcctOpen = ttk.Combobox(
            rightFrame0, textvariable=AcctOpen, state='readonly', font=('arial', 18, 'bold'), width=19)
        self.lblAcctOpen['value'] = ('', 'Select an option', 'Yes', 'No')
        self.lblAcctOpen.current(0)
        self.lblAcctOpen.grid(row=0, column=1, pady=8)
# ====
        self.lblAppDate = Label(rightFrame0, font=(
            'arial', 18, 'bold'), text="Application Date", padx=2, pady=2, bg="powder blue")
        self.lblAppDate.grid(row=1, column=0, sticky=W)

        self.lblAppDate = ttk.Combobox(
            rightFrame0, textvariable=AppDate, state='readonly', font=('arial', 18, 'bold'), width=19)
        self.lblAppDate['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
        self.lblAppDate.current(0)
        self.lblAppDate.grid(row=1, column=1, pady=8)
# ====
        self.lblNCrer = Label(rightFrame0, font=(
            'arial', 18, 'bold'), text="Next Credit Review", padx=2, pady=2, bg="powder blue")
        self.lblNCrer.grid(row=2, column=0, sticky=W)

        self.lblNCrer = ttk.Combobox(
            rightFrame0, textvariable=NextCreditReview, state='readonly', font=('arial', 18, 'bold'), width=19)
        self.lblNCrer['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
        self.lblNCrer.current(0)
        self.lblNCrer.grid(row=2, column=1, pady=8)
# ====
        self.lblLCrer = Label(rightFrame0, font=(
            'arial', 18, 'bold'), text="Last Credit Review", padx=2, pady=2, bg="powder blue")
        self.lblLCrer.grid(row=3, column=0, sticky=W)

        self.lblLCrer = ttk.Combobox(
            rightFrame0, textvariable=LastCreditReview, state='readonly', font=('arial', 18, 'bold'), width=19)
        self.lblLCrer['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
        self.lblLCrer.current(0)
        self.lblLCrer.grid(row=3, column=1, pady=8)
# ====
        self.lblLDateRev = Label(rightFrame0, font=(
            'arial', 18, 'bold'), text="Date Review", padx=2, pady=2, bg="powder blue")
        self.lblLDateRev.grid(row=4, column=0, sticky=W)

        self.lblLDateRev = ttk.Combobox(
            rightFrame0, textvariable=DateReview, state='readonly', font=('arial', 18, 'bold'), width=19)
        self.lblLDateRev['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
        self.lblLDateRev.current(0)
        self.lblLDateRev.grid(row=4, column=1, pady=8)


# ===========================Text, labels entry widget=========================
        self.txtReceipt = Text(rightFrame1, height=24,
                               width=85, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)
# ===========================Button============================================
        self.btnTotal = Button(rightFrame2, padx=40, pady=3, bd=5, fg="black", font=(
            'arial', 9, 'bold'), width=15, bg="powder blue", text="Total", command=Product).grid(row=0, column=0)
        self.btnReset = Button(rightFrame2, padx=40, pady=3, bd=5, fg="black", font=(
            'arial', 9, 'bold'), width=15, bg="powder blue", text="Reset", command=Reset).grid(row=0, column=1)
        self.btnExit = Button(rightFrame2, padx=40, pady=3, bd=5, fg="black", font=(
            'arial', 9, 'bold'), width=15, bg="powder blue", text="Exit", command=iExit).grid(row=0, column=2)


if __name__ == '__main__':
    root = Tk()
    application = Inventory(root)
    root.mainloop()
