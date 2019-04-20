#!/usr/bin/env python3
import tkinter as tk
from ConfigWriter import ConfigWriter
import threading


import os

PRESET = None
BORE_SIZE = None
SLEEVE_LENGTH = None
CYCLE_ENTRY = None

TIME_REMAINING_PAGE = None

class top(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Deburr")
        # Sets container for application
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Adds page to application
        self.frames = {}
        for F in (ConfigPage, Confirmation, Error):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        global TIME_REMAINING_PAGE
        TIME_REMAINING_PAGE = TimeRemaining(container, self)
        self.frames[TimeRemaining] = TIME_REMAINING_PAGE
        TIME_REMAINING_PAGE.grid(row=0, column=0, sticky="nsew")


        # displays page
        self.show_frame(ConfigPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def startListener(text, controller):
    print(text)
    controller.show_frame(Confirmation)
    print(PRESET.get())
    print(BORE_SIZE.get())
    print(SLEEVE_LENGTH.get())
    print(CYCLE_ENTRY.get())


class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self,
                 text="Automated Deburr",
                 fg="Dark Blue",
                 font="Times 24 bold").pack()

        # Reading the current Config
        config = ConfigWriter()
        items = config.readJSON('current.json')

        ################################################################
        # Preset menu
        ################################################################

        PRESET_OPTIONS = []

        directory = 'preset'

        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                PRESET_OPTIONS.append("" + filename)

        presetModule = tk.Frame(self)
        presetModule.pack()

        pre = tk.Label(presetModule,
                       text="Presets: ",
                       fg="Dark Blue",
                       font="Times 16")
        pre.pack(side=tk.LEFT)

        global PRESET
        PRESET = tk.StringVar(presetModule)
        PRESET.set("Preset")
        presetOptionMenu = tk.OptionMenu(presetModule, PRESET, *PRESET_OPTIONS)
        presetOptionMenu.pack(side=tk.LEFT)

        ################################################################
        # Bore size menu
        ################################################################

        BORE_OPTIONS = [
            "Bore Size",
            "0.500",
            "0.750",
            "1.375",
            "2.250"
        ]

        boreModule = tk.Frame(self)
        boreModule.pack()

        bore = tk.Label(boreModule,
                        text="Bore Size: ",
                        fg="Dark Blue",
                        font="Times 16")
        bore.pack(side=tk.LEFT)

        global BORE_SIZE
        BORE_SIZE = tk.StringVar(boreModule)
        if items[0] == 0.0:
            BORE_SIZE.set("Bore Size")
        else:
            BORE_SIZE.set(items[0])  # The bore size from the last run
        boreOptionMenu = tk.OptionMenu(boreModule, BORE_SIZE, *BORE_OPTIONS)
        boreOptionMenu.pack(side=tk.LEFT)

        ################################################################
        # Sleeve Length Menu
        ################################################################

        SLEEVE_OPTIONS = [
            "Sleeve Length",
            "3-7/8",
            "4",  # rep part
            "4-7/8",
            "5",
            "7",
            "9",
            "10-3/4",
            "11-3/4"
        ]

        lengthModule = tk.Frame(self)
        lengthModule.pack()

        length = tk.Label(lengthModule,
                          text="Sleeve Length: ",
                          fg="Dark Blue",
                          font="Times 16")
        length.pack(side=tk.LEFT)

        global SLEEVE_LENGTH
        SLEEVE_LENGTH = tk.StringVar(lengthModule)
        if items[1] == 0.0:
            SLEEVE_LENGTH.set("Sleeve Length")
        elif items[1] == 3.875:
            SLEEVE_LENGTH.set("3-7/8")  # The sleeve length from the last run
        elif items[1] == 4.0:
            SLEEVE_LENGTH.set("4")
        elif items[1] == 4.875:
            SLEEVE_LENGTH.set("4-7/8")
        elif items[1] == 5.0:
            SLEEVE_LENGTH.set("5")
        elif items[1] == 7.0:
            SLEEVE_LENGTH.set("7")
        elif items[1] == 9.0:
            SLEEVE_LENGTH.set("9")
        elif items[1] == 10.75:
            SLEEVE_LENGTH.set("10-3/4")
        elif items[1] == 11.75:
            SLEEVE_LENGTH.set("11-3/4")
        lengthOptionMenu = tk.OptionMenu(lengthModule, SLEEVE_LENGTH, *SLEEVE_OPTIONS)
        lengthOptionMenu.pack(side=tk.LEFT)

        ################################################################
        # Number of Cycles menu
        ################################################################

        cycleModule = tk.Frame(self)
        cycleModule.pack()

        cycle = tk.Label(cycleModule,
                         text="Number of Cycles: ",
                         fg="Dark Blue",
                         font="Times 16")
        cycle.pack(side=tk.LEFT)

        global CYCLE_ENTRY
        v = tk.StringVar(cycleModule, value=items[2])
        CYCLE_ENTRY = tk.Entry(cycleModule, textvariable=v)
        CYCLE_ENTRY.pack(side=tk.LEFT)

        # start button
        start = tk.Button(self,
                          text="Start",
                          command=lambda: startListener("test", controller))
        start.pack()


def confirmListener(controller):

    if CYCLE_ENTRY.get() == '' and PRESET.get() == 'Preset':
        controller.show_frame(Error)
    else:
        TIME_REMAINING_PAGE.countdown(int(CYCLE_ENTRY.get()) * 32 * 60)  # calculates the total run time
        configWrite = ConfigWriter()
        x = threading.Thread(target=configWrite.ConfigWriteMain, args=(PRESET, BORE_SIZE, SLEEVE_LENGTH, CYCLE_ENTRY), daemon=True)
        print('Thread created')
        x.start()
        controller.show_frame(TimeRemaining)
        print('Thread Started')
        # x.join()


class Confirmation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ensure all necessary parts are the \n right size and sleeve is "
                                    "secured in \n housing with door closed.", fg="Dark Blue", font="Times 24")
        label.pack(pady=10, padx=10)

        confirm = tk.Button(self, text="Confirm",
                            command=lambda: confirmListener(controller))
        confirm.pack()


class Error(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Make sure you input a number of cycles", fg="Dark Blue", font="Times 24")
        label.pack(pady=10, padx=10)

        confirm = tk.Button(self, text="Okay",
                            command=lambda: controller.show_frame(ConfigPage))
        confirm.pack()


class TimeRemaining(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Time Remaining",
                            fg="Dark Blue",
                            font="Times 24 bold").pack()
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10, padx=10)
        self.remaining = 0
        # self.countdown(75)	 # Pass in a time for the countdown function.

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Deburr completed")
        else:
            x = formatTime(self.remaining)
            self.label.configure(text=x,
                                 fg="Dark Blue",
                                 font="Times 16")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    # Id you wish for this format: mm:ss (i.e. 12:45), utilize this function
    # below as a helper function for countdown()...


def formatTime(x):
    minutes = int(x / 60)
    hours = int(minutes / 60)
    minutes = int(minutes % 60)
    seconds_rem = int(x % 60)
    if seconds_rem < 10 and minutes > 10:
        return str(hours) + ":" + str(minutes) + ":0" + str(seconds_rem)
    elif seconds_rem > 10 and minutes < 10:
        return str(hours) + ":0" + str(minutes) + ":" + str(seconds_rem)
    elif seconds_rem < 10 and minutes < 10:
        return str(hours) + ":0" + str(minutes) + ":0" + str(seconds_rem)
    else:
        return str(hours) + ":" + str(minutes) + ":" + str(seconds_rem)



app = top()
app.mainloop()
