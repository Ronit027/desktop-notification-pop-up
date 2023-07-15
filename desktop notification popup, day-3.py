from winotify import Notification
toast=Notification(app_id="Ronit Roy",
                   title="Message Title",
                   msg="Hello! This is Ronit",
                   duration="short",
                   icon=r"C:\Users\hp\Downloads\Picsart_22-12-01_12-52-08-925.jpg")
toast.show()
