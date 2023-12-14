# Hello!
You have found MassDelirium's fork of Gorrilla_of_Destiny's Spell Writing Code!
This code requires a couple more python packages due to it having a GUI and all. 

# Mass's GUI for SpellWritingGuide

This is a simple GUI version of the code used in the [Spell Writing Guide](https://www.drivethrurpg.com/product/429711/The-Spell-Writing-Guide?manufacturers_id=22808) which aims to provide a simple method by which we can draw spells in D&D 5e. 

## Setup

You can clone the repo for use simply by typing:

```git clone https://github.com/massDelirium/SpellWritingGuide.git```

When initially running the code a folder called "Uniques" with files such as "11.npy" being created within. These contain the rotationally unique binary numbers the method relies on. They will only be created when such a file does not already exist in a directory called "Uniques".

This code automatically saves spells in the folder "Spells" and will overwrite images when saving if they don't have unique names!
### Dependencies

Python vesion used in development: Python 3.10.4

The required python modules are:
  - numpy
  - matplotlib
  - argparse
  - math
  - os
  - tqdm
  - tkinter
  - PIL (Pillow)
 
## Running the file

to run you type the command: ```py MassGUI.py```

  
## Modifying
  
Not Modifyable yet, but it works!
  
  

