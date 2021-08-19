
#
# Canvas.py
#

# Import CMU Graphics
from cmu_graphics import *

# Defining variables + defaults
colour = 'black'
transparency = 100
size = 15
cursor=Circle(200, 200, size, opacity=transparency, fill=colour)

# Array of all 10 colour rectangles
array = [
    Rect(0, 0, 50, 40, fill='blue', border='dimGray'),
    Rect(0, 40, 50, 40, fill='red', border='dimGray'),
    Rect(0, 80, 50, 40, fill='lawnGreen', border='dimGray'),
    Rect(0, 120, 50, 40, fill='yellow', border='dimGray'),
    Rect(0, 160, 50, 40, fill='orange', border='dimGray'),
    Rect(0, 200, 50, 40, fill='hotPink', border='dimGray'),
    Rect(0, 240, 50, 40, fill='saddleBrown', border='dimGray'),
    Rect(0, 280, 50, 40, fill='black', border='dimGray'),
    Rect(0, 320, 50, 40, fill='darkViolet', border='dimGray'),
    Rect(0, 360, 50, 40, fill='white', border='dimGray')
    ];

# Sliders to indicate what setting you have selected
sizeSlider = Rect(220, 380, 5, 20, fill='black')
transparencySlider = Rect(395, 360, 5, 20, fill='black')

# Group of UI shapes
interface = Group(
Rect(50, 360, 350, 20, fill='lightGray', border='dimGray'),
transparencySlider,
Label("Opacity", 75, 370, bold=True),
Rect(50, 380, 350, 20, fill='lightGray', border='dimGray'),
sizeSlider,
Label("Size", 70, 390, bold=True)
);

# Add everything in array into interface group
for x in array:
    interface.add(x)

    # Helper Function to draw circle with all variables
def drawCircle(colour, size, transparency, x, y):
    Circle(x, y, size, fill=colour, opacity=transparency)

def onMousePress(mouseX, mouseY):
    # Colour Picker
    if(mouseX <= 50):
        for x in array:
            if(x.hits(mouseX, mouseY)):
                global colour
                colour=x.fill

                global cursor
                cursor.fill=x.fill

                print('Current Colour Changed to ' + x.fill)

    # Transparency Picker
    elif mouseY >=360 and mouseY <=380 and mouseX >= 50:
        transparencySlider.left=mouseX

        global transparency
        transparency=pythonRound(mouseX/4)
        cursor.opacity=transparency
        print("Current Opacity Changed to " + str(transparency))

    # Size Picker
    elif mouseY >=380 and mouseX >= 50:
        sizeSlider.left=mouseX

        global size
        size=pythonRound((mouseX-40)/12)
        cursor.radius=size
        print("Current Size Changed to " + str(size))

    # Draws Single Circle On Click
    else:
        drawCircle(colour, size, transparency, mouseX, mouseY)

        # Ensures the UI always stays on top
        interface.toFront()

# Draws on drag
def onMouseDrag(mouseX, mouseY):
    if mouseX >= 50 and mouseY <= 350:
        drawCircle(colour, size, transparency, mouseX, mouseY)

        # Ensures the UI always stays on top
        interface.toFront()

# Update Cursor Position on mouseMove
def onMouseMove(mouseX, mouseY):
    cursor.centerX=mouseX
    cursor.centerY=mouseY
    cursor.toFront()
