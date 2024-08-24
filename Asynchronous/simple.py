import asyncio
import time


def first(sec):
    time.sleep(sec)
    print("first function executed")


def second(sec):
    time.sleep(sec)
    print("second function executed")


def third(sec):
    time.sleep(sec)
    print("third function executed")



first(3)
second(2)
third(1)


