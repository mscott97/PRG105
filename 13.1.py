import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.name_value = tkinter.label(self.info_frame, textvarable=self.name_value)

        self.street_label = tkinter.label(self.info_frame, textvarable=self.street_value)

        self.csz_label = tkinter.label(self.info_frame, textvarable=self.csz_value)

        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        self.show_info_button = tkinter.Button(self.button_frame, text='show info', command = self.show)
        self.quit_button = tkinter.Button(self.button_frame, text = 'quit', command = self.main_window.destory)

        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

def show(self):
        self.name_value.set('Mariya Scott')
        self.street_value.set('123 Glenn Ridge')
        self.csz_value.set('Crystal lake, IL, 60015')

my_gui = MyGUI()
