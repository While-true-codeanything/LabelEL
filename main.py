import os
import re

import pygame
from pygame_widgets.button import Button
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import ButtonArray
import pandas as pd
from tkinter import Tk

data = None
if 'base.csv' in os.listdir():
    data = pd.read_csv("base.csv", sep=';')
data = pd.read_csv("date169.csv", sep=';')

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


From = 175


def react_ide(n):
    global ide_set
    global buttons4
    if n in ide_set:
        ide_set.remove(n)
        buttons4[n].inactiveColour = (140, 140, 140)
        buttons4[n].pressedColour = (140, 140, 140)
        buttons4[n].hoverColour = (140, 140, 140)
    else:
        ide_set.add(n)
        buttons4[n].inactiveColour = (37, 200, 20)
        buttons4[n].pressedColour = (37, 200, 20)
        buttons4[n].hoverColour = (37, 200, 20)


def react_typ(n):
    global id_typ
    global buttons2
    if n in id_typ:
        id_typ.remove(n)
        buttons2[n].inactiveColour = (140, 140, 140)
        buttons2[n].pressedColour = (140, 140, 140)
        buttons2[n].hoverColour = (140, 140, 140)
    else:
        id_typ.add(n)
        buttons2[n].inactiveColour = (37, 200, 20)
        buttons2[n].pressedColour = (37, 200, 20)
        buttons2[n].hoverColour = (37, 200, 20)


def react_click(n):
    global cur_set
    global buttons
    if n in cur_set:
        cur_set.remove(n)
        buttons[n].inactiveColour = (140, 140, 140)
        buttons[n].pressedColour = (140, 140, 140)
        buttons[n].hoverColour = (140, 140, 140)
    else:
        cur_set.add(n)
        buttons[n].inactiveColour = (37, 200, 20)
        buttons[n].pressedColour = (37, 200, 20)
        buttons[n].hoverColour = (37, 200, 20)


def react_obr(n):
    if len("".join(textbox.text)) > 1:
        global cur_set
        global ide_set
        global id_typ
        global From
        global data
        if n:
            card = [[("".join(textbox.text)).replace(';', ''), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            for i in cur_set:
                card[0][i + 1] = 1
            for i in ide_set:
                card[0][8 + i + 1] = 1
            for i in id_typ:
                card[0][11 + i + 1] = 1
            if data is None:
                data = pd.DataFrame(card,
                                    columns=['text', 'WEB', 'Mobile', 'Engineering', 'Metverse', 'Data Science',
                                             'Desktop',
                                             'Chat/Bot', 'Management', 'B2B', 'B2C', 'B2G',
                                             'Социальные', 'Наукоемкие', 'Инженерные', 'Прикладные'])
            else:
                data = pd.concat([data, pd.DataFrame(card,
                                                     columns=['text', 'WEB', 'Mobile', 'Engineering', 'Metverse',
                                                              'Data Science', 'Desktop', 'Chat/Bot', 'Management',
                                                              'B2B', 'B2C', 'B2G', 'Социальные',
                                                              'Наукоемкие', 'Инженерные', 'Прикладные'])])
            cur_set = set()
            ide_set = set()
            id_typ = set()
            # print(data.tail(1))
            data.to_csv('date' + str(From) + '.csv', sep=';')
        else:
            cur_set = set()
            ide_set = set()
            id_typ = set()
        From += 1
        textbox.setText('')
        for i in range(len(buttons)):
            buttons[i].inactiveColour = (140, 140, 140)
            buttons[i].pressedColour = (140, 140, 140)
            buttons[i].hoverColour = (140, 140, 140)
        for i in range(len(buttons2)):
            buttons2[i].inactiveColour = (140, 140, 140)
            buttons2[i].pressedColour = (140, 140, 140)
            buttons2[i].hoverColour = (140, 140, 140)
        for i in range(len(buttons4)):
            buttons4[i].inactiveColour = (140, 140, 140)
            buttons4[i].pressedColour = (140, 140, 140)
            buttons4[i].hoverColour = (140, 140, 140)


pygame.init()
window = pygame.display.set_mode((640, 480))
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)
cur_set = set()
ide_set = set()
bis_set = set()
id_typ = set()
buttonArray = ButtonArray(
    # Mandatory Parameters
    window,  # Surface to place button array on
    0,  # X-coordinate
    350,  # Y-coordinate
    640,  # Width
    50,  # Height
    (8, 1),  # Shape: 2 buttons wide, 2 buttons tall
    border=10,  # Distance between buttons and edge of array
    texts=('WEB', 'Mobile', 'Engineer', 'Metverse', 'Data Science', 'Desktop', 'Chat/Bot', 'Mangmnt'),
    inactiveColour=(200, 50, 0),
    onClicks=(lambda: react_click(0), lambda: react_click(1), lambda: react_click(2), lambda: react_click(3),
              lambda: react_click(4), lambda: react_click(5), lambda: react_click(6), lambda: react_click(7))
)
buttonArray2 = ButtonArray(
    # Mandatory Parameters
    window,  # Surface to place button array on
    0,  # X-coordinate
    250,  # Y-coordinate
    640,  # Width
    50,  # Height
    (4, 1),  # Shape: 2 buttons wide, 2 buttons tall
    border=10,  # Distance between buttons and edge of array
    texts=('Социальные', 'Наукоемкие', 'Инженерные', 'Прикладные'),
    inactiveColour=(200, 50, 0),
    onClicks=(lambda: react_typ(0), lambda: react_typ(1), lambda: react_typ(2), lambda: react_typ(3))
)

buttonArray4 = ButtonArray(
    # Mandatory Parameters
    window,  # Surface to place button array on
    0,  # X-coordinate
    300,  # Y-coordinate
    640,  # Width
    50,  # Height
    (3, 1),  # Shape: 2 buttons wide, 2 buttons tall
    border=10,  # Distance between buttons and edge of array
    texts=('B2B', 'B2C', 'B2G'),
    inactiveColour=(200, 50, 0),
    onClicks=(lambda: react_ide(0), lambda: react_ide(1), lambda: react_ide(2))
)
accept_dec = ButtonArray(
    # Mandatory Parameters
    window,  # Surface to place button array on
    0,  # X-coordinate
    420,  # Y-coordinate
    640,  # Width
    50,  # Height
    (2, 1),  # Shape: 2 buttons wide, 2 buttons tall
    border=10,  # Distance between buttons and edge of array
    texts=('Accept', 'Decline'),
    colour=WHITE,
    onClicks=(lambda: react_obr(True), lambda: react_obr(False))
)
textbox = TextBox(window, 0, 100, 640, 50, fontSize=20,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0), radius=10, borderThickness=5)
accept_dec.buttons[1].inactiveColour = (255, 114, 118)
accept_dec.buttons[0].inactiveColour = (0, 168, 107)
accept_dec.buttons[1].pressedColour = (255, 114, 118)
accept_dec.buttons[0].pressedColour = (0, 168, 107)
accept_dec.buttons[1].hoverColour = (255, 114, 118)
accept_dec.buttons[0].hoverColour = (0, 168, 107)
buttonArray.colour = pygame.Color('lightskyblue3')
buttonArray2.colour = pygame.Color('lightskyblue3')
buttonArray4.colour = pygame.Color('lightskyblue3')
buttons = buttonArray.buttons
buttons2 = buttonArray2.buttons
buttons4 = buttonArray4.buttons
font = pygame.font.SysFont(None, 50)
text = ""
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            data.to_csv('base.csv', sep=';')
            run = False
            quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                textbox.setText(Tk().clipboard_get())
    window.fill((255, 255, 255))
    pygame_widgets.update(events)
    pygame.display.update()

pygame.quit()
exit()
