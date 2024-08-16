import sys
import threading
from json import loads

import FreeSimpleGUI as ui

import AdminCore

admin=AdminCore.Admin()
ui.theme('SystemDefault')
rows=[
    [ui.Button("Connect Remote",enable_events=True,size=(6,2),pad=(20,0)),
ui.Input("Enter command here",size=(50,1),pad=(40),enable_events=True),ui.Button("Run",size=(3,1))],

[ui.Multiline((''),size=(100,16),key='_ListBox_',font=('',12))],

[ui.Button("Quit",font='6')],]

layout=[[ui.Column(rows,scrollable=False,vertical_scroll_only=True,key="column")],]
window=ui.Window("NetUser",layout,size=(700,450),finalize=True,resizable=True).Finalize()
while True:
    thread1=threading.Thread(target=admin.connect_server,args=('localhost',8080))
    try:
        event,values=window.read()
        if event==ui.WIN_CLOSED:
            window.close()
            sys.exit()
        if event=='Connect Remote':
            if not thread1.is_alive():
                thread1.start()
        if event=='Run':
            if not thread1.is_alive():
                thread2=threading.Thread(target=admin.command_executer,args=(values[0],))
                thread2.start()
            thread2.join()
            stdio = loads(admin.recdata.decode())
            
            window.Element("_ListBox_").update(stdio['op'] if not stdio['err'] else stdio['err'])
            
        if event=='Quit':
            window.close()
            sys.exit()

    except Exception as err:
        print(err)