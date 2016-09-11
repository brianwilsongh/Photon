from tkinter import *
import time
import random

root = Tk()
root.minsize(900, 600)
Q25_text = (u"What is the atomic weight of HCO2? What would 1 mol of HCO2 weigh in kg?")

#define all the varaibles, placeholder
number_correct=0
answer_record = []
font_adjust=13
font_size="-size %s" % (font_adjust)
larger_font_size ="-size %s" % (int(font_adjust) + 1)
current_q = "Q12"
qnumber = (str(current_q))[1:]
print ("qnumber is %s by the way" % (qnumber))
question_ID = "Question %s" % (qnumber)
exam_content = "General Chemistry Cumulative Exam - 100 Questions"
oj = "#FAA551"
coal = "#474441"

#Hold page loops


#Menu fucntions

def increase_fontsize():
    global font_adjust
    if font_adjust <= 25:
        font_adjust += 1
        print ("the font is now" + str(font_adjust))
    else:
        pass

def decrease_fontsize():
    global font_adjust
    if font_adjust >= 6:
        font_adjust -= 1

#Create the menu
menu = Menu(root)
root.config(menu=menu)
menu1 = Menu(menu, tearoff=0)
menu.add_cascade(menu=menu1, label="Actions")
menu1.add_command(label="Increase font", command=increase_fontsize)
menu1.add_command(label="Decrease font", command=decrease_fontsize)

#Timer function
timer = [0, 0, 0]
pattern = '{0:02d}:{1:02d}:{2:02d}'
timeText = Label(root, text=("Elapsed Time: " + "00:00:00"), anchor=E, fg="#8d8d8c")
timer_on = True
def update_timeText():
    if timer_on == True:
        global timer
        # Every time this function is called,
        # we will increment 1 second (1/60 of a minute)
        timer[2] += 1

        # Every 60 second is equal to 1 minute
        if (timer[2] >= 60):
            timer[2] = 0
            timer[1] += 1
        # Every 60 minutes is equal to 1 hr
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1], timer[2])
        # Update the timeText Label box with the current time
        timeText.configure(text="Elapsed Time: " + timeString)
        # Call the update_timeText() function after 1 centisecond
    root.after(1000, update_timeText)
timeText.pack(side=BOTTOM, fill=X)

#writequestion function defined and create the list

answer_list = []

A25_right = "the correct response"
A25_wrong = "wrong response 1"
A25_wrong2 = "wrong response 2"
A25_wrong3 = "wrong_response 3"

def write_answer(q):
    global randomized_answer_list
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
    print ("original answer list: " + str(answer_list))
    random.shuffle(answer_list)
    print ("randomized answer list: " + str(answer_list))

write_answer(current_q)

#IT BEGINS HERE ~~~~~ ~~~~~ ~~~~~ topframe for question number and name of exam
topframe = Frame(root)
topframe.pack(side=TOP, fill=X)
#display question number in label
qnumberlabel = Label(topframe, text=question_ID, font=larger_font_size, bg=coal, fg="white", padx=25, pady=2)
qnumberlabel.pack(side=LEFT)
#display exam content
qexamcontentlabel = Label(topframe, text=(exam_content), anchor=E, padx=50, bg = oj, fg="white")
qexamcontentlabel.pack(fill=X, side=TOP)

#middle frame for displaying the question
midframe = Frame(root)
midframe.pack_propagate(0)
midframe.pack(side=TOP)
qbox = Label(midframe, text=Q25_text, font=font_size, pady=40, padx=25)
qbox.grid(row=0, column=2)

#bottomframes for displaying answers
botframe1 = Frame(root)
botframe1.pack(fill=X, pady=3, padx=50)
botframe2 = Frame(root)
botframe2.pack(fill=X, pady=3, padx=50)
botframe3 = Frame(root)
botframe3.pack(fill=X, pady=3, padx=50)
botframe4 = Frame(root)
botframe4.pack(fill=X, pady=3, padx=50)



#functions to ACCEPT and EVALUATE the answer
def eval_input(answer):
    global number_correct
    if answer[(len(qnumber)+2):] == "right":
        print ("point added successfully for right answer")
        number_correct += 1
    else:
        print ("WRONG!")
    answer_record.append(answer)
    print("current answer record: " + str(answer_record))
    print ("current number correct count: " + str(number_correct))

def receive_answerA():
    #take choice A for button A(1)
    the_choice = answer_list[0]
    print ("The choice was: " + the_choice)
    eval_input(the_choice)

def receive_answerB():
    #take choice B for button B(2)
    the_choice = answer_list[1]
    print ("The choice was: " + the_choice)
    eval_input(the_choice)

def receive_answerC():
    #take choice C for button C(3)
    the_choice = answer_list[2]
    print ("The choice was: " + the_choice)
    eval_input(the_choice)

def receive_answerD():
    #take choice C for button D(4)
    the_choice = answer_list[3]
    print ("The choice was: " + the_choice)
    eval_input(the_choice)

#answer buttons
answer1 = Button(botframe1, text="A", font=larger_font_size, bg=coal, fg="white", width=5, command=receive_answerA)
answer1.pack(side=LEFT, padx=10)
display_answer1 = Label(botframe1, text=answer_list[0], font=font_size)
display_answer1.pack(side=LEFT, fill=X)

answer2 = Button(botframe2, text="B", font=larger_font_size, bg=coal, fg="white", width=5, command=receive_answerB)
answer2.pack(side=LEFT, padx=10, anchor=W)
display_answer2 = Label(botframe2, text=answer_list[1], font=font_size)
display_answer2.pack(side=LEFT, fill=X)

answer3 = Button(botframe3, text="C", font=larger_font_size, bg=coal, fg="white", width=5, command=receive_answerC)
answer3.pack(side=LEFT, padx=10)
display_answer3 = Label(botframe3, text=answer_list[2], font=font_size)
display_answer3.pack(side=LEFT, fill=X)

answer4 = Button(botframe4, text="D", font=larger_font_size, bg=coal, fg="white", width=5, command=receive_answerD)
answer4.pack(side=LEFT, padx=10)
display_answer4 = Label(botframe4, text=answer_list[3], font=font_size)
display_answer4.pack(side=LEFT, fill=X)







#run mainloop and timer
update_timeText()
root.mainloop()

