import  time
import random as rd
from tkinter import Tk,Button,DISABLED

def show_card(x,y):
      global card_1
      global card1_x,card1_y
      cards[x,y]['text']=card_symbols[x,y]

      cards[x,y].update_idletasks()

      if card_1:
          card1_x=x
          card1_y=y
          card_1=False
      elif card1_x!=x or card1_y!=y:
          if cards[card1_x,card1_y]['text']!=cards[x,y]['text']:
             time.sleep(1)
             cards[x,y]['text']=' '
             cards[card1_x,card1_y]['text']=' '
          else:
              cards[card1_x,card1_y]['command']=DISABLED
              cards[x,y]['command']=DISABLED
          card_1=True

win=Tk()
win.title('MATCHMAKER')
win.resizable(width=False,height=False)



card_1=True
card1_x=0
card1_y=0
cards={}
card_symbols={}
symbols=[u'\u2705',u'\u2702',u'\u270B',u'\u2708',u'\u2706',u'\u2764',
         u'\u263A', u'\u2604', u'\u2744', u'\u269B', u'\u231A', u'\u260E',
         u'\u2705', u'\u2702', u'\u270B', u'\u2708', u'\u2706', u'\u2764',
         u'\u263A', u'\u2604', u'\u2744', u'\u269B', u'\u231A', u'\u260E']
# print(symbols)
rd.shuffle(symbols)

for i in range(4):
     for j in range(6):
          b=Button(width=13,height=6,command=lambda i=i,j=j:show_card(i,j),font='helvetica 16')
          b.grid(row=i,column=j)
          cards[i,j]=b
          card_symbols[i,j]=symbols.pop()

win.mainloop()
