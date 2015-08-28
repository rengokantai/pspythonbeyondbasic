__author__ = 'Hernan Y.Ke'
class Loggin:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

with Loggin() as l:
    print(l)