from os import *

def logout():
    return system("shutdown -t")
def restart():
    return system("shutdown /r /t 0")
def stop() :
    return system("shutdown /s /t 0")

logout()