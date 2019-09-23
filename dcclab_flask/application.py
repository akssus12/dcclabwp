'''
Created on 2019. 9. 23.

@author: Yeonwoo
'''
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def mainpage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()