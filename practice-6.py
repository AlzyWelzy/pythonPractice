import time
from plyer import notification
import dbus

if __name__ == "__main__":
    notification.notify(
        title="Please drink water", message="A Human Male should drink 4L of water each day", app_icon="water-glass.png",
        timeout=5
    )
    time.sleep(60*60)
