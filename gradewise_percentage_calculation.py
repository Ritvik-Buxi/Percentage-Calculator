from tkinter import *
root = Tk()
root.title("Gradewise Percentage Calculation")
root.geometry("400x300")
percentageGrade3Label = Label(root)
percentageGrade3Label.place(relx=0.5,rely=0.1,anchor=CENTER)
percentageGrade5Label = Label(root)
percentageGrade5Label.place(relx=0.5,rely=0.3,anchor=CENTER)
percentageGrade10Label = Label(root)
percentageGrade10Label.place(relx=0.5,rely=0.5,anchor=CENTER)
percentageGrade3Label.configure(font=("Helvetica",16,"bold"))
percentageGrade5Label.configure(font=("Helvetica",16,"bold"))
percentageGrade10Label.configure(font=("Helvetica",16,"bold"))

class grade3:
    def __init__(self,language_arts,mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
    def percentage(self):
        total_marks = self.mathematics + self.language_arts
        total_marks_with_100 = total_marks*100
        grade3percentage = total_marks_with_100/200
        percentageGrade3Label["text"] = grade3percentage
class grade5:
    def __init__(self,language_arts,mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    def percentage(self):
        total_marks = self.mathematics + self.language_arts + self.social_studies
        total_marks_with_100 = total_marks*100
        grade5percentage = total_marks_with_100/300
        percentageGrade5Label["text"] = grade5percentage
class grade10:
    def __init__(self,language_arts,mathematics,social_studies,foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language
    def percentage(self):
        total_marks = self.mathematics + self.language_arts + self.social_studies + self.foreign_language
        total_marks_with_100 = total_marks*100
        grade10percentage = total_marks_with_100/400
        percentageGrade10Label["text"] = grade10percentage
objgra3 = grade3(88,77)
objgra5 = grade5(100,97,98)
objgra10 = grade10(100,97,98,99)
btngra3 = Button(master=root,text="Grade 3",command = objgra3.percentage )
btngra3.place(relx=0.5,rely=0.2,anchor=CENTER)
btngra5 = Button(master=root,text="Grade 5",command = objgra5.percentage )
btngra5.place(relx=0.5,rely=0.4,anchor=CENTER)
btngra10 = Button(master=root,text="Grade 10",command = objgra10.percentage )
btngra10.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()