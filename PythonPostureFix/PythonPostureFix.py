from plyer import notification  #pip install plyer
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon= 'F:\\Hopstarter-Halloween-Avatar-Diablo.ico',



        timeout = 15,
        app_name='PostureApp'

    )


if __name__ == '__main__':
    while True:
        notifyMe("HELLO!!", "FIX UR POSTURE")
        time.sleep(1200)