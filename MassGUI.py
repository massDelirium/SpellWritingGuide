# I Attempt to make a simple UI
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import writer

# Create root of tkinker container
root = tkinter.Tk()
root.geometry('800x450')
root.title('Spell Writing')


class GUI:
    def __init__(self, master):
        self.master = master
        self.gatherattrlist()
        self.filename = "Fireball"
        self.choice = ["3", "evocation", "fire", "sphere", "point (150 feet)", "Fireball"]
        self.givespell("3", "evocation", "fire", "sphere", "point (150 feet)", "Fireball")
        self.folder = "Spells"
        # create grid structure
        paddings = {'padx': 5, 'pady': 5}

        # create frame for Attribute Buttons
        buttonspot = {'column': 0, 'row': 0, 'columnspan': 1, 'rowspan': 5, 'sticky': NW}
        self.buttonFrame = Frame(self.master)
        self.buttonFrame.grid(**buttonspot, **paddings)

        # Create frame for Picture
        picturespot = {'column': 2, 'row': 0, 'columnspan': 2, 'rowspan': 5, 'sticky': NE}
        self.pictureframe = Frame(self.master)
        self.pictureframe.grid(**picturespot, **paddings)

        self.pLabel = ttk.Label(self.pictureframe)

        self.nameinput = ttk.Entry(self.buttonFrame)
        self.nameinput.grid(column=0, row=0, **paddings)
        self.nameinput.insert(0, "Fireball")
        # Put fireball up upon start
        self.ogImage = Image.open(self.folder+"/"+self.filename+".png")
        self.resize_image = self.ogImage.resize((600, 450))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.pLabel.config(image=self.image)
        self.pLabel.pack()

        class AttributeButton:
            def __init__(self, master, attribute, order, start):
                self.master = master
                self.order = order
                self.values = attribute
                self.var = StringVar(value=start)
                self.padxy = {'padx': 5, 'pady': 5}
                self.size = {'width': 15}
                self.position = {'row': (self.order+1), 'column': 0, 'rowspan': 1, 'columnspan': 1, 'sticky': NE}

                self.frame = Frame(self.master)
                self.frame.grid(**self.position, **self.padxy)

                self.optionMenu = OptionMenu(self.frame, self.var, *self.values)
                self.optionMenu.config(**self.padxy, **self.size)
                self.optionMenu.pack(side=LEFT)

            def givevar(self):
                return self.var.get()

        # Create buttons to put in the frame
        self.Levelbutton = AttributeButton(self.buttonFrame, self.levels, 0, self.choice[0])
        self.Schoolbutton = AttributeButton(self.buttonFrame, self.schools, 1, self.choice[1])
        self.Damagebutton = AttributeButton(self.buttonFrame, self.damages, 2, self.choice[2])
        self.Areabutton = AttributeButton(self.buttonFrame, self.areas, 3, self.choice[3])
        self.Rangebutton = AttributeButton(self.buttonFrame, self.ranges, 4, self.choice[4])

        # Create go button
        self.size = {'width': 15}
        self.go = Button(self.buttonFrame, text='Write!', command=self.update, **self.size)
        self.go.grid(sticky=NW, row=6, column=0, padx=10, pady=10)

    def gatherattrlist(self):
        # gather Attributes from file
        self.levels = writer.load_attribute("Attributes/levels.txt")
        self.schools = writer.load_attribute("Attributes/school.txt")
        self.damages = writer.load_attribute("Attributes/damage_types.txt")
        self.areas = writer.load_attribute("Attributes/area_types.txt")
        self.ranges = writer.load_attribute("Attributes/range.txt")

    def printchoice(self):
        print(self.choice)

    def update(self):
        self.filename = (self.nameinput.get())
        self.choice[0] = self.Levelbutton.givevar()
        self.choice[1] = self.Schoolbutton.givevar()
        self.choice[2] = self.Damagebutton.givevar()
        self.choice[3] = self.Areabutton.givevar()
        self.choice[4] = self.Rangebutton.givevar()
        writer.plt.clf()

        self.givespell(self.choice[0], self.choice[1], self.choice[2], self.choice[3], self.choice[4], self.filename)
        self.makeimage(self.folder+"/"+self.filename+".png")

    def givespell(self, level, school, damage, area, rangee, file):
        writer.draw_spell(level, rangee, area, damage, school,
                          title=file, legend=TRUE,
                          breakdown=TRUE, savename=("Spells/"+file+".png"))

    def makeimage(self, file):
        self.ogImage = Image.open(file)
        self.resize_image = self.ogImage.resize((600, 450))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.pLabel.config(image=self.image)
        self.pLabel.pack()


# Actually run the GUI Program
running = GUI(root)
root.mainloop()
