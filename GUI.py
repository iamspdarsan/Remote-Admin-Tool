import PySimpleGUI as ui
import AdminCore
import threading
import sys
admin=AdminCore.Admin()
ui.theme('SystemDefault')
rows=[
    [ui.Button("Start Server",enable_events=True,size=(6,2),pad=(20,0)),
ui.Input("Enter command here",size=(50,1),pad=(40),enable_events=True),ui.Button("Run",size=(3,1))],

[ui.Multiline((''),size=(100,16),key='_ListBox_',font=('',12))],

[ui.Button("Quit",font='6')],]

layout=[[ui.Column(rows,scrollable=False,vertical_scroll_only=True,key="column")],]
window=ui.Window("NetUser Tracker",layout,size=(700,450),finalize=True,resizable=True).Finalize()
while True:
    thread1=threading.Thread(target=admin.start_server,args=('',8080,2,))
    try:
        event,values=window.read()
        print(event,values)
        if event==ui.WIN_CLOSED:
            window.close()
            sys.exit()
        if event=='Start Server':
            if not thread1.is_alive():
                thread1.start()
        if event=='Run':
            if not thread1.is_alive():
                thread2=threading.Thread(target=admin.command_executer,args=(values[0],))
                thread2.start()
            thread2.join()
            window.Element("_ListBox_").update(admin.recdata.decode())
        if event=='Quit':
            window.close()
            sys.exit()

    except Exception:
        print()