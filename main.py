import time
import model, view, controller

while True:
    time.sleep(1/60)
    controller.process_events()