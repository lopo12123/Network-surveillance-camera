'''
There are some problems that make it impossible 
to display Chinese even if UTF-8 encoding is used
'''

# -*- coding: utf-8 -*-
from flask import Flask, render_template
import datetime
import os

click_message = "stop" # a global variable

app = Flask(__name__)

@app.route("/") # main page
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'title',
      'time': timeString,
      'motion_state': click_message
      }
   return render_template('index.html', **templateData)

'''
The following are five functions corresponding to the five 
states of camera movement: up, down, left, and right, and stop.
You can change the value of the global variable 'click_message'
and display the current corresponding movement status on the web page.
The movement of the servo can be controlled by reading the value of 'click_message'
'''

@app.route("/up") # click up
def click_information1():
  # move up
  click_message = "up"
  print(click_message)
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  templateData2 = {
      'title' : 'click_up',
      'time': timeString,
      'motion_state': click_message
      }
  return render_template('index.html', **templateData2)
  
@app.route("/left") # click left
def click_information2():
  # move left
  click_message = "left"
  print(click_message)
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  templateData2 = {
      'title' : 'click_up',
      'time': timeString,
      'motion_state': click_message
      }
  return render_template('index.html', **templateData2)
  
@app.route("/stop") # click stop
def click_information3():
  # stop
  click_message = "stop"
  print(click_message)
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  templateData2 = {
      'title' : 'click_up',
      'time': timeString,
      'motion_state': click_message
      }
  return render_template('index.html', **templateData2)
  
@app.route("/right") # click right
def click_information4():
  # move right
  click_message = "right"
  print(click_message)
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  templateData2 = {
      'title' : 'click_up',
      'time': timeString,
      'motion_state': click_message
      }
  return render_template('index.html', **templateData2)

@app.route("/down") # click down
def click_information5():
  # move down
  click_message = "down"
  print(click_message)
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  templateData2 = {
      'title' : 'click_up',
      'time': timeString,
      'motion_state': click_message
      }
  return render_template('index.html', **templateData2)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
