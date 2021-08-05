import tkinter
from tkinter import *

root = Tk()
root.geometry('600x400')

root.title("Mad Libs Game Generator")
lbl1 = Label(root, text="Mad Libs Generator\nHave Fun!", font="arial 20")
lbl2 = Label(root, text="Select the game language:", font="arial 15")
btn_language1 = Button(root,
                       text="Portuguese",
                       font="arial 12",
                       background="white",
                       width=20,
                       height=2,
                       compound="c",
                       command=lambda: languageSelection("portuguese"))
btn_language2 = Button(root,
                       text="English",
                       font="arial 12",
                       background="white",
                       width=20,
                       height=2,
                       compound="c",
                       command=lambda: languageSelection("english"))


def homePage():
    lbl1.pack()
    lbl2.pack()
    btn_language1.place(x=200, y=150)
    btn_language2.place(x=200, y=250)
    hoverAnimation(btn_language1, 150)
    hoverAnimation(btn_language2, 250)


def hoverAnimation(button, positionY):
    button.bind("<Enter>", func=lambda e: button.configure(background="blue", width=25, height=3), add="+")
    button.bind("<Enter>", func=lambda p: button.place(x=180, y=positionY), add="+")

    button.bind("<Leave>", func=lambda e: button.configure(background="white", width=20, height=2), add="+")
    button.bind("<Leave>", func=lambda p: button.place(x=200, y=positionY), add="+")


def languageSelection(language):
    btn_language1.destroy()
    btn_language2.destroy()
    lbl2.destroy()

    if language == "portuguese":
        lbl3 = Label(root, text="Escolha uma história", font="arial 12")
    else:
        lbl3 = Label(root, text="Choose a story", font="arial 12")
    root.children.clear()
    lbl3.pack()
    stories()


def stories():
    btn_madLib1 = Button(root,
                         text="The Photographer",
                         font="arial 12",
                         background="white",
                         width=20,
                         height=2,
                         compound="c",
                         command=lambda: madLibs("photographer"))
    btn_madLib2 = Button(root,
                         text="Apple and Apple",
                         font="arial 12",
                         background="white",
                         width=20,
                         height=2,
                         compound="c",
                         command=lambda: madLibs("appleApple"))
    btn_madLib3 = Button(root,
                         text="The butterfly",
                         font="arial 12",
                         background="white",
                         width=20,
                         height=2,
                         compound="c",
                         command=lambda: madLibs("butterfly"))
    hoverAnimation(btn_madLib1, 100)
    hoverAnimation(btn_madLib2, 200)
    hoverAnimation(btn_madLib3, 300)

    btn_madLib1.place(x=200, y=100)
    btn_madLib2.place(x=200, y=200)
    btn_madLib3.place(x=200, y=300)


def madLibs(story):
    if story == "photographer":
        animals = input('enter a animal name : ')
        profession = input('enter a profession name: ')
        cloth = input('enter a piece of cloth name: ')
        things = input('enter a thing name: ')
        name = input('enter a name: ')
        place = input('enter a place name: ')
        verb = input('enter a verb in ing form: ')
        food = input('food name: ')
        print(
            'say ' + food + ', the photographer said as the camera flashed! ' + name + ' '
            'and I had gone to ' + place + ' to get our photos taken on my birthday. The first photo we '
            'really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession +
            '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing '
            + cloth + ' and ' + verb + ' --exactly what I had in mind')
    elif story == "appleApple":
        adjective = input('enter adjective : ')
        color = input('enter a color name : ')
        thing = input('enter a thing name :')
        place = input('enter a place name : ')
        person = input('enter a person name : ')
        adjective1 = input('enter a adjactive : ')
        insect = input('enter a insect name : ')
        food = input('enter a food name : ')
        verb = input('enter a verb name : ')
        print(
            'Last night I dreamed I was a ' + adjective + ' butterfly with ' + color + ' splocthes that looked like '
            + thing + ' .I flew to ' + place + ' with my bestfriend and ' + person + ' who was a ' + adjective1 + ' '
            + insect + ' .We ate some ' + food + ' when we got there and then decided to ' + verb + ' and the dream ended '
            'when I said-- lets ' + verb + '.')
    else:
        person = input('enter person name: ')
        color = input('enter color : ')
        foods = input('enter food name : ')
        adjective = input('enter aa adjective name: ')
        thing = input('enter a thing name : ')
        place = input('enter place : ')
        verb = input('enter verb : ')
        adverb = input('enter adverb : ')
        food = input('enter food name: ')
        things = input('enter a thing name : ')
        print(
            'Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many different varieties "
            "of apples. I ate " + color + ' apples straight off the tree that tested like ' + foods +
            '. Then there was a ' + adjective + ' apple that looked like a ' + thing + '.When our bag were '
            'full, we went on a free hay ride to ' + place + ' and back. It ended at a hay pile where we got to '
            + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make appple '
            + food + ' and ' + things + ' pies!.')


homePage()

root.mainloop()
