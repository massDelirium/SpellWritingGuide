#I Attempt to make a simple UI
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import writer

#create root of tkinker container
root = tkinter.Tk()
root.geometry('800x450')
root.title('Spell Writing')

class GUI:
    def __init__(self, master):
        self.master = master
        self.gatherAtList()
        self.filename = "Spell.png"
        self.choice = ["3", "evocation", "fire","sphere","point (150 feet)","Fireball"]
        self.giveSpell("3", "evocation", "fire","sphere","point (150 feet)","Fireball")

        # create frame for Attribute Buttons
        self.frame = Frame(root)
        self.frame.pack(side=LEFT)
        self.pictureframe = Frame(root)
        self.pictureframe.pack(side=RIGHT)

        self.frame6 = Frame(root)
        self.frame6.pack(side=TOP)
        self.plabel = ttk.Label(self.pictureframe)
        self.makeImage("Fireball.png")
        class AttributeButton:
            def __init__(self, master, attribute, id,start):
                self.master = master
                self.id = id

                self.frame = Frame(self.master)
                self.values = attribute
                self.var = StringVar(value=start)

                self.optionMenu = OptionMenu(self.frame, self.var, *self.values)
                self.optionMenu.pack(padx=50, pady=20)

                self.frame.pack(expand=True, fill=BOTH)

            def giveVar(self):
                return self.var.get()

        #Create buttons to put in the frame
        self.Levelbutton = AttributeButton(self.frame, self.levels, 0, self.choice[0])
        self.Schoolbutton = AttributeButton(self.frame, self.schools, 1, self.choice[1])
        self.Damagebutton = AttributeButton(self.frame, self.damages, 2, self.choice[2])
        self.Areabutton = AttributeButton(self.frame, self.areas, 3, self.choice[3])
        self.Rangebutton = AttributeButton(self.frame, self.ranges, 4, self.choice[4])

        self.go = Button(self.frame, text='Write!', command=self.update)
        self.go.pack(side=LEFT, padx= 50, pady = 20)

    def gatherAtList(self):
        # gather Attributes from file
        self.levels = writer.load_attribute("Attributes/levels.txt")
        self.schools = writer.load_attribute("Attributes/school.txt")
        self.damages = writer.load_attribute("Attributes/damage_types.txt")
        self.areas = writer.load_attribute("Attributes/area_types.txt")
        self.ranges = writer.load_attribute("Attributes/range.txt")
    def printchoice(self):
        print(self.choice)
    def update(self):
        self.choice[0] = self.Levelbutton.giveVar()
        self.choice[1] = self.Schoolbutton.giveVar()
        self.choice[2] = self.Damagebutton.giveVar()
        self.choice[3] = self.Areabutton.giveVar()
        self.choice[4] = self.Rangebutton.giveVar()
        writer.plt.clf()
        #self.printchoice()
        self.giveSpell(self.choice[0], self.choice[1], self.choice[2], self.choice[3], self.choice[4],self.filename)
        self.makeImage(self.filename)
    def giveSpell(self,level,school,damage,area,range,file):
        writer.draw_spell(level, range, area, damage, school,
                          title=file, legend=TRUE,
                          breakdown=TRUE, savename=file)


    def makeImage(self,file):
        self.ogImage = Image.open(file)
        self.resize_image = self.ogImage.resize((600, 450))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.plabel.config(image=self.image)
        self.plabel.pack()


if __name__ == "__main__":
    #actually run the GUI Program
    running = GUI(root)
    root.mainloop()


