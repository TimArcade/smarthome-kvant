import pygame

from tkinter import *
from tkinter import ttk

from pygameWindow import *
from settings import *
from pygame.locals import *
import sys

def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)

def delete():
    print("p")

root = Tk()
root.title("METANIT.COM")
root.geometry("450x720")
 
Label = Label(Text="Время")