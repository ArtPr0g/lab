from contextlib import contextmanager
import time

@contextmanager
def cm_timer_1():
    start = time.perf_counter()
    yield
    print("Время работы блока кода: {} секунд".format(time.perf_counter() - start))

class cm_timer_2:

    def __init__(self):
        self.start = time.perf_counter()

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print("Время работы блока кода: {} секунд".format(time.perf_counter() - self.start))

with cm_timer_1():
    time.sleep(2)
with cm_timer_2():
    time.sleep(2)