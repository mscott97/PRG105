import tkinter
import tkinter.messagebox
import pickle


class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('FINAL THE RolePlaying GAME')
        self.radio_var = 0

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.label4 = tkinter.Label(self.top_frame,
                                    text='So, you want a good grade in this class? No way! this is my class!')
        self.label5 = tkinter.Label(self.top_frame, text='You have to get though me frist!')

        self.fight = tkinter.Radiobutton(self.top_frame, text='fight', variable=self.radio_var, value=1)
        self.item = tkinter.Radiobutton(self.top_frame, text='item', variable=self.radio_var, value=2)
        self.Talk = tkinter.Radiobutton(self.top_frame, text='talk', variable=self.radio_var, value=3)

        self.quit_button = tkinter.Button(self.bottom_frame, text='RUN', command=self.master.destroy)
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        # pack the buttons
        self.fight.pack(side='left')
        self.item.pack(side='left')
        self.Talk.pack(side='left')
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

def open_menu(self):
        if self.radio_var.get() == 1-3:
            search = FightGUI(self.master)
        elif self.radio_var.get() == 2:
            search = ItemGUI(self.master)
        elif self.radio_var.get() == 3:
            search = TalkGUI(self.master)

class FightGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('fight')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='time to fight!: ')
        self.goodlooking = tkinter.Radiobutton(self.top_frame, text='paper cut!', variable=self.radio_var, value=1)
        self.please = tkinter.Radiobutton(self.top_frame, text='water bottle throw', variable=self.radio_var, value=2)
        self.comeon = tkinter.Radiobutton(self.top_frame, text='Pin Push!', variable=self.radio_var, value=3)
        # pack top frame
        self.search_label.pack(side='left')
        self.goodlooking.pack(side='left')
        self.please.pack(side='left')
        self.comeon.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='fight!', command=self.open_menu2)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

def open_menu5(self):
    if self.radio_var.get() == 1:
        search = goodlookingGUI(self.master)
    elif self.radio_var.get() == 2:
        search = pleaseGUI(self.master)
    elif self.radio_var.get() == 3:
        search = Comeon(self.master)


def open_menu2(self):
        if self.radio_var.get() == 1:
            search = HitGUI(self.master)


class TalkGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('talk')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Time to talk!: ')
        self.paper = tkinter.Radiobutton(self.top_frame, text='', variable=self.radio_var, value=1)
        self.water = tkinter.Radiobutton(self.top_frame, text='water bottle throw', variable=self.radio_var, value=2)
        self.pin = tkinter.Radiobutton(self.top_frame, text='pin stab', variable=self.radio_var, value=3)
        # pack top frame
        self.search_label.pack(side='left')
        self.paper.pack(side='left')
        self.water.pack(side='left')
        self.pin.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.open_menu2)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

class ItemGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('item')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='time to heal!!: ')
        self.goodlooking = tkinter.Radiobutton(self.top_frame, text='coffee drink!', variable=self.radio_var, value=1)
        # pack top frame
        self.search_label.pack(side='left')
        self.goodlooking.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.open_menu7)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

class HitGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Get out of the way!')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.label = tkinter.Label(self.top_frame, text='Damage 30! Hit Points left 50! ')
        self.label2 = tkinter.Label(self.top_frame, text='I am not done yet! Take this! paper cut!')
        self.paper = tkinter.Radiobutton(self.top_frame, text='paper doge', variable=self.radio_var, value=1)
        self.water = tkinter.Radiobutton(self.top_frame, text='water bottle throw dodge', variable=self.radio_var, value=2)
        self.pin = tkinter.Radiobutton(self.top_frame, text='pin stab dodge', variable=self.radio_var, value=3)
        # pack top frame
        self.label.pack(side='left')
        self.label2.pack(side='left')
        self.paper.pack(side='left')
        self.water.pack(side='left')
        self.pin.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.open_menu3)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

class BaddogdeGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Wrong action!')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.label = tkinter.Label(self.top_frame, text='Damage taken 30! Hit Points left 50! ')
        self.label2 = tkinter.Label(self.top_frame, text='Wrong action! Choose Again! Quick!')
        self.paper = tkinter.Radiobutton(self.top_frame, text='paper doge', variable=self.radio_var, value=1)
        self.water = tkinter.Radiobutton(self.top_frame, text='water bottle throw dodge', variable=self.radio_var, value=2)
        self.pin = tkinter.Radiobutton(self.top_frame, text='pin stab dodge', variable=self.radio_var, value=3)
        # pack top frame
        self.label.pack(side='left')
        self.label2.pack(side='left')
        self.paper.pack(side='left')
        self.water.pack(side='left')
        self.pin.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.open_menu4)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

def open_menu6(self):
    if self.radio_var.get() == 1:
        search = doingwellGUI(self.master)
    elif self.radio_var.get() == 2-3:
        search = Badtalkself(self.master)

def open_menu7(self):
    if self.radio_var.get() == 1:
        search = Coffe(self.master)

class PleaseGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Bad talk!!')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.label = tkinter.Label(self.top_frame, text='Damage 10! Hit Points left 80! ')
        self.label2 = tkinter.Label(self.top_frame, text='Agh...I guess so...whatever!')
        self.paper = tkinter.Radiobutton(self.top_frame, text='Come on! You know I been Doing well in here!', variable=self.radio_var, value=2)
        self.water = tkinter.Radiobutton(self.top_frame, text='Thank you! Your great you know that?', variable=self.radio_var, value=1)
        self.pin = tkinter.Radiobutton(self.top_frame, text='Stop it!! I just wnt this!!', variable=self.radio_var, value=3)
        # pack top frame
        self.label.pack(side='left')
        self.label2.pack(side='left')
        self.paper.pack(side='left')
        self.water.pack(side='left')
        self.pin.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.open_menu6)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

class NicedogeGUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Good Action!')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.label = tkinter.Label(self.top_frame, text='Nice dodge! ')
        self.label2 = tkinter.Label2(self.top_frame, text='Agh! Your up I guess! I do not understand why we need to do this way! Stupid rules')
        self.Goback = tkinter.Radiobutton(self.top_frame, text='time to choose again!', variable=self.radio_var, value=1)

        # pack top frame
        self.label.pack(side='left')
        self.label2.pack(side='left')
        self.Goback.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='return', command=self.open_menu)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()



def open_menu4(self):
        if self.radio_var.get() == 1:
            search = Gooddodge1(self.master)
        elif self.radio_var.get() == 2-3:
            search = BaddogdeGUI2(self.master)

class Baddogde2GUI:
    def __init__(self, master):

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Good Action!')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.label = tkinter.Label(self.top_frame, text='Nice dodge! ')
        self.label2 = tkinter.Label2(self.top_frame, text='Agh! Your up I guess! I do not understand why we need to do this way! Stupid rules')
        self.Goback = tkinter.Radiobutton(self.top_frame, text='time to choose again!', variable=self.radio_var, value=1)

        # pack top frame
        self.label.pack(side='left')
        self.label2.pack(side='left')
        self.Goback.pack(side='left')
        # middle frame
        self.value = tkinter.StringVar()

        # pack Middle frame

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='return', command=self.open_menu)

        # pack bottom frame
        self.search_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()


def back(self):
        self.look.destroy()

def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    menu_gui = MainGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
