from tkinter import *
import os
def on_selection(event):
    # here you can get selected element
    print('previous:', l1.get('active'))
    val1 = l1.curselection()
    l1int = int(val1[0])
    labelEdit1['text'] = l1int+1


def on_selection2(event):
    # here you can get selected element
    print('previous:', l2.get('active'))
    val2 = l2.curselection()
    l2int = int(val2[0])
    labelEdit2['text'] = l2int+1


def test():
    val1 = textBox1.get()
    val2 = textBox2.get()
    val3 = textBox3.get()
    val4 = textBox4.get()
    if(val1.isnumeric() and val2.isnumeric() and val3.isnumeric() and val4.isnumeric()):
        calculations(val1,val2,val3,labelEdit1['text'],labelEdit2['text'],val4)
    else:
        return
def calculations(text1,text2,text3,text4,text5,text6):
    global minion_upgrade
    diamond_spreading = False
    while True:
        try:
            action_time = float(text1)
            check = 1/action_time
            break
        except:
            pass


    while True:
        try:
            price_per = float(text2)
            check = 1 / price_per
            break
        except:
            pass

    while True:
        try:
            items_per_action = float(text3)
            check = 1 / items_per_action
            break
        except:
            pass


    while True:
        try:
            fuel_answer = int(text4)
            check = 1 / fuel_answer
            break
        except:
            pass


    while True:
        try:
            upgrade_answer = int(text5)
            check = 1 / upgrade_answer
            if upgrade_answer == 1:
                diamond_spreading = True
                minion_upgrade = 0
            elif upgrade_answer == 2:
                minion_upgrade = 0.20
            elif upgrade_answer == 3:
                minion_upgrade = 0.05
            elif upgrade_answer == 4:
                minion_upgrade = 0
            break
        except:
            pass

    while True:
        try:
            minion_amount = float(text6)
            check = 1 / minion_amount
            break
        except:
            pass

    calculations2(action_time, price_per, items_per_action, fuel_answer, upgrade_answer, minion_amount, diamond_spreading)
    return action_time, price_per, items_per_action, fuel_answer, upgrade_answer, minion_amount
def calculations2(action_time, price_per, items_per_action, fuel_answer, upgrade_answer, minion_amount, diamond_spreading):

    if fuel_answer == 1:
        minion_fuel = 1.05          #Coal
    elif fuel_answer == 2:
        minion_fuel = 1.05          #Block of coal
    elif fuel_answer == 3:
        minion_fuel = 1.05          #E bread
    elif fuel_answer == 4:
        minion_fuel = 1.10          #E coal
    elif fuel_answer == 5:
        minion_fuel = 1.25          #Solar Panel
    elif fuel_answer == 6:
        minion_fuel = 1.25          #E lava bucket
    elif fuel_answer == 7:
        minion_fuel = 1.50          #Hamster Wheel
    elif fuel_answer == 8:
        minion_fuel = 1.90          #Foul flesh
    elif fuel_answer == 9:
        minion_fuel = 1.20          #E charcoal
    elif fuel_answer == 10:
        minion_fuel = 1             #None
    else:
        minion_fuel = 1




    fuel_efficency = 1 / minion_fuel
    upgrade_efficiency = 1 / (minion_upgrade + 1)
    action_time = action_time * fuel_efficency * upgrade_efficiency
    actions_per_hour = hour / action_time
    items_per_hour = actions_per_hour * items_per_action
    profit_per_hour = items_per_hour * minion_amount * price_per

    if diamond_spreading == True:
        spreding_money = items_per_hour / 10 * 8 * minion_amount
        profit_per_hour = profit_per_hour + spreding_money





    profit_per_day = profit_per_hour * 24
    profit_per_week = profit_per_day * 7

    clear()
    labelEdit3['text'] = "     Profit Per Hour = $"+'{:20,.2f}'.format(profit_per_hour).replace(" ", '')
    labelEdit4['text'] = "     Profit Per Day = $"+'{:20,.2f}'.format(profit_per_day).replace(" ", '')
    labelEdit5['text'] = "     Profit Per Week = $"+'{:20,.2f}'.format(profit_per_week).replace(" ", '')







# หน้าจอ
gui = Tk()
gui.geometry("500x600")
gui.title("Minion Resource Calculator [Gui By ZahnEins] [Code By e56]")

clear = lambda: os.system('cls')
hour = 3600
# ข้อความ
mLabel1 = Label(text="ระยะเวลาของมินเนี่ยนระหว่างการกระทำ (วินาที) ").grid(row = 1)
mLabel2 = Label(text="ราคา ").grid(row = 2)
mLabel3 = Label(text="จำนวนไอเทมที่ได้รับต่อรอบของมินเนี่ยน ").grid(row = 3)
mLabel4 = Label(text="       ").grid(row = 4)
mLabel5 = Label(text="Fuel ของมินเนี่ยน (ไม่คำนวณเวลา) ").grid(row = 5)
mLabel6 = Label(text="      ").grid(row = 6)
mLabel7 = Label(text="มินเนี่ยนอัพเกรด ").grid(row = 7)
mLabel8 = Label(text=" ").grid(row = 8)
mLabel9 = Label(text="จำนวนมินเนี่ยนที่มี ").grid(row = 9)
mLabel10 = Label(text="      ").grid(row = 10)

labelEdit1 = Label(gui,text="เชื้อเพลิงที่เลือก")
labelEdit1.grid(row = 5,column=3)
labelEdit2 = Label(gui,text="มินเนี่ยนอัพเกรดที่เลือก")
labelEdit2.grid(row = 7,column=3)

labelEdit000 = Label(text=" ").grid(row=13,column=2)

labelEdit3 = Label(gui,text="ต่อชม.")
labelEdit3.grid(row = 14,column=1)
labelEdit4 = Label(gui,text="ต่อวัน")
labelEdit4.grid(row = 15,column=1)
labelEdit5 = Label(gui,text="ต่อสัปดาห์")
labelEdit5.grid(row = 16,column=1)
# กล่องรับข้อความ
textBox1=Entry(gui)
textBox1.grid(row=1,column=1)
textBox2=Entry(gui)
textBox2.grid(row=2,column=1)
textBox3=Entry(gui)
textBox3.grid(row=3,column=1)
textBox4=Entry(gui)
textBox4.grid(row=9,column=1)
# ตารางข้อความ
l1 = Listbox()
l1.insert(1,"Coal")
l1.insert(2,"Block of coal")
l1.insert(3,"E-bread")
l1.insert(4,"E-coal")
l1.insert(5,"Solar Panel")
l1.insert(6,"E-lava Bucket")
l1.insert(7,"Hamster wheel")
l1.insert(8,"CoaFoul fleshl")
l1.insert(9,"E-charcoal")
l1.insert(10,"None")
l1.grid(row=5,column = 1)
l1.bind('<<ListboxSelect>>', on_selection)

l2 = Listbox(widt=20,height=4)
l2.insert(1,"Diamond Spreading")
l2.insert(2,"Flycatcher")
l2.insert(3,"Minion expander")
l2.insert(4,"None")
l2.grid(row=7,column = 1)
l2.bind('<<ListboxSelect>>', on_selection2)

# ปุ่ม
mBottun = Button(gui,text="คำนวณ",command=test).grid(row = 11,column=1)

menubar = Menu(gui)
gui.mainloop()

