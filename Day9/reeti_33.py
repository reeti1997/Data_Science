# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:15:31 2018

@author: reeti
"""

from pymongo import MongoClient
from datetime import datetime
#import json

client = MongoClient('localhost', 27017)
mydb = client.db_University

def add_student(student_name, student_age, student_roll_no, student_branch):
    unique_student = mydb.student_info.find_one({"Roll No":student_roll_no}, {"_id":0})
    if unique_student:
        return "Student information already exists"
    else:
        mydb.student_info.insert(
                {
                "Student Name" : student_name,
                "Age" : student_age,
                "Roll No" : student_roll_no,
                "Branch" : student_branch,
                "Date-Time" : datetime.now()
                })
        return "Information added successfully"

def view_client(student_name):
    user = mydb.student_info.find_one({"Student Name":student_name}, {"_id":0})
    if user:
        name = user["Student Name"]
        age = user["Age"]
        roll_no = user["Roll No"]
        branch = user["Branch"]
        time = user["Date-Time"]
        return {"Student Name":name, "Age":age, "Roll No":roll_no, "Branch":branch}
    else:
        return "Sorry, No such student exists"

lim = input("No. of students = ")
for info in range(0,lim):
    name = raw_input("Enter Student Name: ")
    age = raw_input("Enter Student Age: ")
    roll_no = raw_input("Enter Student Roll No: ")
    branch = raw_input("Enter Student Branch: ")

    print add_student(name, age, roll_no, branch)

user = raw_input("Enter Student Name to find: ")
user_data = view_client(user)

print user_data