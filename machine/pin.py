import RPi.GPIO as GPIO

class Pin:
    IN = GPIO.IN
    OUT = GPIO.OUT
    #OPEN_DRAIN = 7
    PULL_UP = GPIO.PUD_UP
    PULL_DOWN = GPIO.PUD_DOWN
    IRQ_FALLING = GPIO.FALLING
    IRQ_RISING = GPIO.RISING
    # IRQ_LOW_LEVEL = 2
    # IRQ_HIGH_LEVEL = 3
    def __init__(self, id:int, mode:int, pull:int = None, value:int = None):
        self.id = id
        self.init(mode, pull, value)
    
    def init(self, mode:int, pull:int = None, value:int = None):        
        self._set_mode(mode)
        self._set_value(value)
        self._set_pull(pull)
        if mode == GPIO.OUT:
            GPIO.setup(self.id, GPIO.OUT, initial = self._get_value())
        else:
            GPIO.setup(self.id, GPIO.IN, pull_up_down = self._get_pull())
        
    def value(self, value = None):
        self._set_value(value)
        if self.mode == GPIO.IN:
            return GPIO.input(self.id)
        else:
            GPIO.output(self.id, self._get_value())
    
    def on(self):
        self.value(GPIO.HIGH)

    def off(self):
        self.value(GPIO.LOW)

    def mode(self, mode = None):
        if mode == None:
            return self._get_mode()
        else:
            self._set_mode(mode)
            if self._get_mode() == GPIO.OUT:
                GPIO.setup(self.id, GPIO.OUT, initial=self._get_value())
            else:
                GPIO.setup(self.id, GPIO.IN)

    def pull(self, pull = None):
        if pull == None:
            return self._get_pull()            
        else:
            self._set_pull(pull)
            GPIO.setup(self.id, GPIO.IN, pull_up_down=self._get_pull())
    
    def _set_value(self, value):
        if value == True:
            self._value = GPIO.HIGH
        else:
            self._value = GPIO.LOW

    def _get_value(self):
        return self._value
    
    def _set_mode(self, mode):
        if mode == True:
            self._mode = GPIO.IN
        else:
            self._mode = GPIO.OUT

    def _get_mode(self):
        return self._mode
    
    def _set_pull(self, pull):
        pud = GPIO.PUD_OFF
        if pull != None:
            pud = pull
        self._pull = pud
    
    def _get_pull(self):
        return self._pull

    def _set_trigger(self, trigger):
        self._trigger = trigger
    
    def _get_trigger(self):
        return self._trigger

    def irq(self, handler, trigger=[Pin.IRQ_FALLING, Pin.IRQ_RISING]):
        if handler == None:
            return
        length = len(trigger)
        if length == 1:
            GPIO.add_event_detect(self.id, trigger[0], callback=lambda pn: handler(self))
        else:
            GPIO.add_event_detect(self.id, GPIO.BOTH, callback=lambda pn: handler(self))
        