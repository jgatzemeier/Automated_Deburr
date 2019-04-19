import tkinter as tk
import ConfigWriter


import os

PRESET = None
BORE_SIZE = None
SLEEVE_LENGTH = None
CYCLE_ENTRY = None


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
        for F in (ConfigPage, Confirmation, TimeRemaining):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        # displays page
        self.show_frame(ConfigPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def startListener(text, controller):
    print(text)
    controller.show_frame(Confirmation)
    print(PRESET.get())
    ConfigWriter.PRESET = PRESET.get()
    print(BORE_SIZE.get())
    ConfigWriter.BORE_SIZE = BORE_SIZE.get()
    print(SLEEVE_LENGTH.get())
    ConfigWriter.SLEEVE_LENGTH = SLEEVE_LENGTH.get()
    print(CYCLE_ENTRY.get())
    ConfigWriter.NUM_CYCLES = CYCLE_ENTRY.get()


class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self,
                 text="Automated Deburr",
                 fg="Dark Blue",
                 font="Times 24 bold").pack()

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
        BORE_SIZE.set("Bore Size")
        boreOptionMenu = tk.OptionMenu(boreModule, BORE_SIZE, *BORE_OPTIONS)
        boreOptionMenu.pack(side=tk.LEFT)

        ################################################################
        # Sleeve Length Menu
        ################################################################

        SLEEVE_OPTIONS = [
            "3-7/8",
            "4", # rep part
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
        SLEEVE_LENGTH.set("Sleeve Length")
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
        CYCLE_ENTRY = tk.Entry(cycleModule)
        CYCLE_ENTRY.pack(side=tk.LEFT)

        # start button
        start = tk.Button(self,
                          text="Start",
                          command=lambda: startListener("test", controller))
        start.pack()


class Confirmation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ensure all necessary parts are the \n right size and sleeve is "
                                    "secured in \n housing with door closed.", fg="Dark Blue", font="Times 24")
        label.pack(pady=10, padx=10)


        confirm = tk.Button(self, text="Confirm",
                            command=lambda: ConfigWriter.ConfigWriteMain())#controller.show_frame(TimeRemaining))
        confirm.pack()


class TimeRemaining(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(75)	# Pass in a time for the countdown function.

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Timer is up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    # Id you wish for this format: mm:ss (i.e. 12:45), utilize this function
    # below as a helper function for countdown()...

    '''
    def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))
    '''


app = top()
app.mainloop()
