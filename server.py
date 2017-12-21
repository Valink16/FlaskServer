import os, subprocess
from flask import Flask, send_from_directory, redirect

server = Flask(__name__, static_folder='static')

@server.route('/')
def redirectToHome():
    return redirect('/home')

@server.route('/home')
def welcome():
    return send_from_directory(os.path.join(server.static_folder, 'html'), "index.html")

@server.route('/getFile/<path:folder>/<path:file_name>')
def getFile(folder, file_name):
    return send_from_directory(os.path.join(server.static_folder, folder), file_name)

@server.route('/runScript/<path:script_name>')
def runScript(script_name):
    r=subprocess.Popen("python {}".format(os.path.join(server.static_folder, 'scripts', script_name)), stdout=subprocess.PIPE, shell=True)
    r=r.communicate()[0]
    t=''
    for c in r.decode('utf-8'):
        if c=='\n':
            t+="<br/>"
        else:
            t+=c
    return t
server.run('0.0.0.0')
