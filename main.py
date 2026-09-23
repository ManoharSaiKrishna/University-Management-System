# Python + Streamlit project
# Motive of this project is to revise the important python concepts
# University Management System

import streamlit as st

# configuring the main app page
st.set_page_config(
    page_title="University Management System", 
    page_icon=":mortar_board:", 
    layout="wide"
    )

st.title("University Management System")


# create a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

menu_choice = st.sidebar.radio(
    "SELECT OPTION",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teacher",
        "List of Colleges"
    )
)

class College:
    def __init__(self,cname):
        self.cname=cname
        self.students=[]
        self.teachers=[]
    def add_student(self,s):
        self.students.append(s)
    def add_teacher(self,t):
        self.teachers.append(t)

class Person:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

class Student(Person):  # Inheritance
    def __init__(self, sname, sage, srollno, branch):
        super().__init__(sname, branch)
        self.sage = sage
        self.srollno = srollno

class Teacher(Person):
    def __init__(self, tname, tage, tsubject, branch):
        super().__init__(tname, branch)
        self.tage = tage
        self.tsubject = tsubject

if menu_choice == "Create College":
    cname = st.text_input("Enter new college name")
    if st.button("CREATE"):
        clg_obj=College(cname) # creating an object of college class
        st.session_state.colleges.append(clg_obj)
        st.success(f"College created successfully : {cname}")
elif menu_choice == "Add Student":
    if len(st.session_state.colleges) == 0:
        st.warning("No college found. Please create a college first.")
    if not st.session_state.colleges:
        st.warning("No colleges available. Please create a college first.") # Both are same, just different ways to check the length of the list
    else:
        clg_name = st.selectbox("Select College", [clg.cname for clg in st.session_state.colleges])
        sname = st.text_input("Enter Student Name")
        sage = st.number_input("Enter Student Age", min_value=1, max_value=100)
        srollno = st.text_input("Enter Student Roll Number")
        branch = st.text_input("Enter Student Branch")
        if st.button("ADD STUDENT"):
            if not(sname and sage and srollno and branch):
                st.warning("Please fill all the fields.")
            else:
                for clg in st.session_state.colleges:
                    if clg.cname == clg_name:
                        student_obj=Student(sname, sage, srollno, branch)
                        clg.add_student(student_obj)
                        st.success(f"Student {sname} added to {clg_name}")
                        break
elif menu_choice == "Add Teacher":
    if len(st.session_state.colleges) == 0:
        st.info("No college found. Please create a college first.")
    else:
        clg_name = st.selectbox("Select College", [clg.cname for clg in st.session_state.colleges])
        tname = st.text_input("Enter Teacher Name")
        tage = st.number_input("Enter Teacher Age", min_value=1, max_value=100)
        tsubject = st.text_input("Enter Teacher Subject")
        tbranch = st.text_input("Enter Teacher Branch")
        if st.button("ADD TEACHER"):
            if not(tname and tage and tsubject and tbranch):
                st.warning("Please fill all the fields.")
            else:
                for clg in st.session_state.colleges:  # loop to find the college object from the list of colleges
                    if clg.cname == clg_name:
                        teacher_obj=Teacher(tname, tage, tsubject, tbranch)
                        clg.add_teacher(teacher_obj)
                        st.success(f"Faculty named {tname} added to {clg_name}")
                        break
elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.warning("No colleges available. Please create a college first.")
    else:
        clg_name=st.selectbox("Select College", [clg.cname for clg in st.session_state.colleges])
        for clg in st.session_state.colleges:
            if clg.cname == clg_name:
                if not clg.students:
                    st.info(f"No students found in {clg_name}.")
                else:
                    st.subheader(f"Students in {clg_name}:")
                    for student in clg.students:
                        st.write(f"Name: {student.name}, Age: {student.sage}, Roll No: {student.srollno}, Branch: {student.branch}")
                break
elif menu_choice == "Display Teacher":
    if not st.session_state.colleges:
        st.warning("No colleges available. Please create a college first.")
    else:
        clg_name=st.selectbox("Select College", [clg.cname for clg in st.session_state.colleges])
        for clg in st.session_state.colleges:
            if clg.cname == clg_name:
                if not clg.teachers:
                    st.info(f"No teachers found in {clg_name}.")
                else:
                    st.subheader(f"Teachers in {clg_name}:")
                    for teacher in clg.teachers:
                        st.write(f"Name: {teacher.name}, Age: {teacher.tage}, Subject: {teacher.tsubject}")
                break
elif menu_choice == "List of Colleges":
    st.subheader("List of Colleges:")
    if not st.session_state.colleges:
        st.warning("No colleges available. Please create a college first.")
    else:
        for i, clg in enumerate(st.session_state.colleges, start=1):
            st.write(f"{i}. College Name: {clg.cname}")