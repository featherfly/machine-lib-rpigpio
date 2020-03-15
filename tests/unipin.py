import sys
import time
import sys

if sys.implementation.name == 'micropython':
    from machine import Pin 
    UniPin =  type('UniPin', (Pin,), dict({}))
else:
    class UniPin:
        def p():
            print("aaa")
    pass #这里加入树莓派的判断代码

UniPin().p()

