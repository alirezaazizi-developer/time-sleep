"""
   This is a opensource tools for manage time for using computer
"""
import time
from playsound import playsound
from win10toast import ToastNotifier
import sqlite3

"""
   configuration of appication
"""
connection = sqlite3.connect('rest.db')

print(' This small app written with python language \n author is Alireza Azizi \n build in 2020 17 Frebriary \n lisence GUN3')

time_config = input('Please write your time (default is : 20 minute) : ')
register = input('Do you want add to windows registery (Y/N): ')

"""
   main part of application
"""
toaster = ToastNotifier()



"""
show message app started
"""
# while for check time 
while(True):
    time.sleep(5)
    toaster.show_toast('Its time to rest',
                   "please rest right now",
                   icon_path='favicon.ico',
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)