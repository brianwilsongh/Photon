from tkinter import *
import random

answer_list = []

A25_right = "the correct response"
A25_wrong = "wrong response 1"
A25_wrong2 = "wrong response 2"
A25_wrong3 = "wrong_response 3"

def write_answer(q):
    #retrieve the raw question number
    v = len(current_q)
    qnumber = (str(q))[1:v]
    print (qnumber)
    aprefix = "A" + qnumber + "_"
    print (aprefix)
    #retrieve answer list with code
    answer_list.append(aprefix + "right")
    answer_list.append(aprefix + "wrong")
    answer_list.append(aprefix + "wrong2")
    answer_list.append(aprefix + "wrong3")
    print (answer_list)
    random.shuffle(answer_list)
    print (answer_list)

write_answer(current_q)