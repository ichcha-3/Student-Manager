import tkinter as tk
from tkinter import ttk

def main():
    app = application()
    app.mainloop()

class application(tk.Tk):
    def __init__(self,root):
        super().__init__()
        self.title("Simple App")  #tilte of window
        
if __name__ == "__main__":
main()

#root = tk.Tk()   #parent window

#root.title("Simple App")  #tilte of window
#root.mainloop()

#def add_to_list(event = None):#since the bind() passes the event object as a arugment automaticaly so the fuction we are calling need to have arugment for it to work 
    
    text = entry.get()   #here in his function we are getting the test entered throught get() function
    if text:             #her in the if block if the text is entered and not just a blank line we make use of special tkinter function insert() 

        text_list.insert(tk.END, text)#here the entered test is basically intsert at the end of the content of that widget and what we want to insert is the text

        entry.delete(0,tk.END)# here usually in this type of list the input is earased form the field once it is added in the list to allow user to add more 
                              # so here the delete fuction is used to earase the text from field once entered all the way from start i.e from 0 to the end    

#EXTRA : we can do this using other method i.e using lambda fuction :entry.bind("<Return>", lambda event: add_to_list) so here if we use this method even if the fuction we are working with does not have an argument it will still work perfectly fine


root.columnconfigure(0 , weight = 1)# having the first row and column weight configure to 1 it makes it take up all the available space when it is resized
root.rowconfigure(0 , weight = 3)
root.columnconfigure(1 , weight = 1)

frame = ttk.Frame(root)
frame.grid(row = 0, column = 0 , sticky = "nsew",padx = 5,pady=5) #since our root window is able to expant we use sticky to ensure that our frame window stick to all sides of that window

frame.columnconfigure(0, weight = 1)#here the first colum which contain entry and list is going to expand whicle the second column that contain button is not
frame.rowconfigure(1, weight = 1)

entry = ttk.Entry(frame) #sice it is a zero based indexing system column zero refers to first column
entry.grid(row= 0,column = 0,sticky = "ew")#so that the input button would stick to the sides i'e left and right when expanded

#here we write code for adding list without pressin the add button i.e by using several evernt handling 
entry.bind("<Return>",add_to_list) #here the entry is bind to return key i.e we want to handle when retun key is pressed 

entry_btn = ttk.Button(frame, text = "Add", command= add_to_list) #here frame is within the window and enrty button is within the frame
entry_btn.grid(row= 0,column = 1) 

text_list = tk.Listbox(frame)
text_list.grid(row= 1,column = 0,columnspan = 2,sticky = "nsew") #her ew stands for east and west since we wanted it to stick to the sides i.e left and the right side we're gonna use east and west here

#SECOND LIST

frame2 = tk.Frame(root)
frame2.grid(row = 0, column = 1 , sticky = "nsew",padx = 5,pady=5)

frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(1, weight = 1)

entry = tk.Entry(frame2)
entry.grid(row= 0,column = 0,sticky = "ew")

entry.bind("<Return>",add_to_list) 

entry_btn = tk.Button(frame2, text = "Add", command= add_to_list)
entry_btn.grid(row= 0,column = 1) 
 
text_list = tk.Listbox(frame2)
text_list.grid(row= 1,column = 0,columnspan = 2,sticky = "nsew") 

root.mainloop()