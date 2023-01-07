from WLhelper import WLHelper
from customtkinter import *


class Window:
    set_appearance_mode("System")
    set_default_color_theme("dark-blue")
    temp = ''
    wlhelper = WLHelper()
    app = CTk()
    app.geometry("1000x700")
    app.title('WL Helper')
    app.resizable(width=False, height=False)

    def generate_window(self):
        self.generate_fields()
        self.app.mainloop()

    def out_writen(self):
        print(self.temp)

    def solo_mode_active(self):
        for checkbox in [self.checkbox_double, self.checkbox_ai]:
            checkbox.deselect()
        for field in [self.field_token2, self.field_uid1, self.field_uid2]:
            field.configure(state='disabled')
        for field in [self.field_time_min, self.field_time_max]:
            field.configure(state='normal')
        self.start_btn.configure(command=self.wlhelper.solo_bot)

    def double_mode_active(self):
        for checkbox in [self.checkbox_solo, self.checkbox_ai]:
            checkbox.deselect()
        for field in [self.field_time_min, self.field_time_max, self.field_token2, self.field_uid1, self.field_uid2]:
            field.configure(state='normal')
        self.start_btn.configure(command=self.wlhelper.double_bot)

    def ai_mode_active(self):
        for checkbox in [self.checkbox_double, self.checkbox_solo]:
            checkbox.deselect()
        for field in [self.field_time_min, self.field_time_max, self.field_token2, self.field_uid1, self.field_uid2]:
            field.configure(state='disabled')
        self.start_btn.configure(command=self.wlhelper.ai_bot)

    def write_values(self):
        self.wlhelper.token1 = self.field_token1.get()
        self.wlhelper.id_channel = self.field_id_channel.get()
        self.wlhelper.time_min = self.field_time_min.get()
        self.wlhelper.time_max = self.field_time_max.get()
        self.wlhelper.token2 = self.field_token2.get()
        self.wlhelper.id_bot1 = self.field_uid1.get()
        self.wlhelper.id_bot2 = self.field_uid2.get()

    field_token1 = CTkEntry(master=app)
    field_id_channel = CTkEntry(master=app)
    field_time_min = CTkEntry(master=app)
    field_time_max = CTkEntry(master=app)
    field_token2 = CTkEntry(master=app)
    field_uid1 = CTkEntry(master=app)
    field_uid2 = CTkEntry(master=app)
    checkbox_solo = CTkCheckBox(master=app)
    checkbox_double = CTkCheckBox(master=app)
    checkbox_ai = CTkCheckBox(master=app)
    start_btn = CTkButton(master=app)

    def generate_fields(self):
        choose_mode = CTkLabel(master=self.app, text='Choose Mode', font=('Segoe UI', 30), text_color="#1F538D")
        choose_mode.place(x=60, y=10)
        checkbox_solo = CTkCheckBox(master=self.app, text='Solo Mode', command=self.solo_mode_active, font=('Segoe UI', 20))
        checkbox_double = CTkCheckBox(master=self.app, text='Double Mode', command=self.double_mode_active, font=('Segoe UI', 20))
        checkbox_ai = CTkCheckBox(master=self.app, text='AI Mode', command=self.ai_mode_active, font=('Segoe UI', 20))
        checkbox_solo.place(x=50, y=60)
        checkbox_double.place(x=50, y=100)
        checkbox_ai.place(x=50, y=140)
        field_token1 = CTkEntry(master=self.app, width=400, height=30, placeholder_text='Token', fg_color="#1F538D", font=('Segoe UI', 16))
        field_id_channel = CTkEntry(master=self.app, width=400, height=30, placeholder_text='Channel ID', fg_color="#1F538D", font=('Segoe UI', 16))
        field_time_min = CTkEntry(master=self.app, width=400, height=30, placeholder_text='Minimum time in secs', fg_color="#1F538D", font=('Segoe UI', 16))
        field_time_max = CTkEntry(master=self.app, width=400, height=30, placeholder_text='Max time in secs', fg_color="#1F538D", font=('Segoe UI', 16))
        field_token2 = CTkEntry(master=self.app, width=400, height=30, placeholder_text='Token additional', fg_color="#1F538D", font=('Segoe UI', 16))
        field_uid1 = CTkEntry(master=self.app, width=400, height=30, placeholder_text='ID user 1(above)', fg_color="#1F538D", font=('Segoe UI', 16))
        field_uid2 = CTkEntry(master=self.app, width=400, height=30, placeholder_text='ID user 2(below)', fg_color="#1F538D", font=('Segoe UI', 16))
        field_token1.place(x=500, y=35)
        field_id_channel.place(x=500, y=75)
        field_time_min.place(x=500, y=115)
        field_time_max.place(x=500, y=155)
        field_token2.place(x=500, y=195)
        field_uid1.place(x=500, y=235)
        field_uid2.place(x=500, y=275)
        button_confirm = CTkButton(master=self.app, text='ENTER', width=200, height=70, font=('Segoe UI', 30), command=self.write_values)
        button_confirm.place(x=220, y=235)
        start_btn = CTkButton(master=self.app, text='START', width=200, height=50, font=('Segoe UI', 40))
        start_btn.place(x=400, y=600)
        self.checkbox_solo = checkbox_solo
        self.checkbox_double = checkbox_double
        self.checkbox_ai = checkbox_ai
        self.field_token1 = field_token1
        self.field_id_channel = field_id_channel
        self.field_time_min = field_time_min
        self.field_time_max = field_time_max
        self.field_token2 = field_token2
        self.field_uid1 = field_uid1
        self.field_uid2 = field_uid2
        self.start_btn = start_btn


if __name__ == '__main__':
    window = Window()
    window.generate_window()
    sys.exit()