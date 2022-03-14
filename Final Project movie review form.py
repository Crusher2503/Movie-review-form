"""  Movie review form final project
This code allows you to input a movie title your rating for a movie
Tim Powers 3/1/2022
"""


 
 
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

root=tk.Tk()
 
# setting the windows size
root.geometry("1000x1000")


                        
# declaring string variable
# for storing name, score, and review
mame_var=tk.StringVar()
score_var=tk.StringVar()
rview_var=tk.StringVar()
 

# defining a function that will
# get the name,score, and review
# print them on the screen
def submit():
 
    Movie=mame_var.get()
    Score=score_var.get()
    Review=rview_var.get()
     
    print(" Movie: " + Movie)
    print(Score + "/10")
     
    mame_var.set("")
    score_var.set("")
    rview_var.set("")
     
    
# creating a label for
# name using widget Label
mame_label = tk.Label(root, text = 'Movie Name', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
mame_entry = tk.Entry(root,textvariable = mame_var, font=('calibre',10,'normal'))
  
# creating a label for score
score_label = tk.Label(root, text = 'Score out of 10', font = ('calibre',10,'bold'))
  
# creating a entry for score
score_entry=tk.Entry(root, textvariable = score_var, font = ('calibre',10,'normal'))

rview_label = tk.Label(root, text = 'Review', font=('calibre',10, 'bold'))

rview_entry=tk.Entry(root,textvariable = rview_var, font=('calibre',10,'bold'))
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
exit_btn=tk.Button(root,text = 'Exit', command = root.destroy)
info_btn=tk.Button(root,text = 'Info',)
# placing the label and entry in
# the required position using grid
# method
mame_label.grid(row=0,column=0)
mame_entry.grid(row=0,column=1)
score_label.grid(row=1,column=0)
score_entry.grid(row=1,column=1)
rview_label.grid(row=2,column=0)
rview_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=0)
exit_btn.grid(row=3,column=1)
info_btn.grid(row=3,column=2)
# performing an infinite loop
# for the window to display






root.mainloop()
