import random
from tkinter import *

root = Tk()

current_q = "Q257"
Q257_text = "Text transplant successful!"
Q257_hint = "Hint transplant successful!"
question_number = 25

def write_question(q):
    #adds components of question based on "Q42" input format held by a global variable "q"
    v=len(current_q)
    qnumber = (str(q))[1:v]
    #sliced the actual number out of the Q42 format
    print ("the question number: " + qnumber)
    qtext = eval("Q" + qnumber + str("_text"))
    #Get Q42_text and turn it into variable qtext
    print (qtext)
    qhint = eval("Q" + qnumber + str("_hint"))
    print (qhint)
    #find the hint for the Qcode


write_question(current_q)



