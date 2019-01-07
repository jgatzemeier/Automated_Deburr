import tkinter as tk
import functools as ft


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


def startListener(text, controller, preset, bore, sleeve, cycles):
    print(text)
    controller.show_frame(Confirmation)
    print(preset.get())
    print(bore.get())
    print(sleeve.get())
    print(cycles.get())


class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self,
                 text="Automated Deburr",
                 fg="Dark Blue",
                 font="Times 24 bold").pack()

        # Preset menu
        OPTIONS = [
            "one",
            "two",
            "three"
        ]

        presetModule = tk.Frame(self)
        presetModule.pack()

        pre = tk.Label(presetModule,
                       text="Presets: ",
                       fg="Dark Blue",
                       font="Times 16")
        pre.pack(side=tk.LEFT)

        preset = tk.StringVar(presetModule)
        preset.set("Preset")
        presetOptionMenu = tk.OptionMenu(presetModule, preset, *OPTIONS)
        presetOptionMenu.pack(side=tk.LEFT)

        # Bore size menu
        OPTIONS = [
            "one",
            "two",
            "three"
        ]

        boreModule = tk.Frame(self)
        boreModule.pack()

        bore = tk.Label(boreModule,
                        text="Bore Size: ",
                        fg="Dark Blue",
                        font="Times 16")
        bore.pack(side=tk.LEFT)

        boreSize = tk.StringVar(boreModule)
        boreSize.set("Bore Size")

        boreOptionMenu = tk.OptionMenu(boreModule, boreSize, *OPTIONS)
        boreOptionMenu.pack(side=tk.LEFT)

        # Sleeve Length Menu
        OPTIONS = [
            "one",
            "two",
            "three"
        ]

        lengthModule = tk.Frame(self)
        lengthModule.pack()

        length = tk.Label(lengthModule,
                          text="Sleeve Length: ",
                          fg="Dark Blue",
                          font="Times 16")
        length.pack(side=tk.LEFT)

        sleeveLen = tk.StringVar(lengthModule)
        sleeveLen.set("Sleeve Length")

        lengthOptionMenu = tk.OptionMenu(lengthModule, sleeveLen, *OPTIONS)
        lengthOptionMenu.pack(side=tk.LEFT)

        # Number of Cycles menu
        cycleModule = tk.Frame(self)
        cycleModule.pack()

        cycle = tk.Label(cycleModule,
                         text="Number of Cycles: ",
                         fg="Dark Blue",
                         font="Times 16")
        cycle.pack(side=tk.LEFT)
        cycles = tk.StringVar()

        cycleEntry = tk.Entry(cycleModule)
        cycleEntry.pack(side=tk.LEFT)

        # start button
        start = tk.Button(self,
                          text="Start",
                          command=lambda: startListener("test", controller, preset, boreSize, sleeveLen, cycleEntry))
        start.pack()


class Confirmation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ensure all necessary parts are the \n right size and sleeve is "
                                    "secured in \n housing with door closed.", fg="Dark Blue", font="Times 24")
        label.pack(pady=10, padx=10)


        confirm = tk.Button(self, text="Confirm",
                            command=lambda: controller.show_frame(TimeRemaining))
        confirm.pack()


class TimeRemaining(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(ConfigPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(Confirmation))


app = top()
app.mainloop()
