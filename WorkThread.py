import threading


class WorkThread(threading.Thread):
    def __init__(self, user, price, **kwargs):
        self.user = user
        self.price = price
        super().__init__(**kwargs)

    def run(self):
        from migrate import migrate
