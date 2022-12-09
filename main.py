import time
import model, view, controller

while True:
    time.sleep(1/60)
    model.step()
    controller.process_events()
    view.draw()