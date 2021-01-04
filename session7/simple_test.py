#!/usr/bin/python
#-- coding: UTF-8 --
from __future__ import unicode_literals, print_function

from psychopy import visual, event, core, monitors
from random import choice

win = visual.Window(allowGUI=False, #monitor=m,
                    fullscr=False, winType='pyglet', rgb=-.5,
                    )

clock = core.Clock()

def get_response():
    '''Collect key press and rt and return them'''
    clock.reset()
    return event.waitKeys(timeStamped=clock)[0]  # waitKeys returned eine Liste von Tupeln: [('taste', RT)] wenn timeStamped definiert ist, sonst [('taste')]

def show_word(word='Default'):
    '''show a word and return a response'''
    visual.TextStim(win, text=word).draw()
    win.flip()
    return get_response()  # show_word ruft get_response auf!

def show_feedback(trial, correct_key, response):
    '''show feedback'''
    button, rt = response  # multiple assignment
    template = "Trial {}.\n\nresponse was: " + "{}, RT: {}. {}\n\nAny key to continue ..."
    feedback = "Correct!" if button == correct_key else "Incorrect!"
    feedback_text = template.format(trial, button, round(rt, 3), feedback)
    show_word(feedback_text)  # show_feedback benutzt show_word und damit intern get_response


# actual experiment
stims = list("abcdef")

for trial in range(10):  # 10 trials
    letter = choice(stims)  # draw a random letter
    response = show_word(letter)
    show_feedback(trial + 1, letter, response)



