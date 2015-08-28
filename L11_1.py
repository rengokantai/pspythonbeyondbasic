__author__ = 'Hernan Y.Ke'
from random import randrange

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input("?"))

        except ValueError:#always specify a exception name
            continue
        if guess==number:
            print("Done")
            break

if  __name__ =="__main__":
    main()
