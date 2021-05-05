from threading import Timer
from inspect import signature
from functools import partial, wraps
import time


def debounce(interval):
    def decorator(fn):
        sig = signature(fn)
        caller = {}

        def debounced(*args, **kwargs):
            nonlocal caller

            try:
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                called_args = fn.__name__ + str(dict(bound_args.arguments))
            except:
                called_args = ''

            t_ = time.time()

            def call_it(key):
                try:
                    # always remove on call
                    caller.pop(key)
                except:
                    pass

                fn(*args, **kwargs)

            try:
                # Always try to cancel timer
                caller[called_args].cancel()
            except:
                pass

            caller[called_args] = Timer(interval, call_it, [called_args])
            caller[called_args].start()

        return debounced

    return decorator

class Throttle(object):
  def __init__(self,func,interval):
    self.func = func
    self.interval = interval
    self.last_run = 0
  def __get__(self,obj,objtype=None):
    if obj is None:
      return self.func
    return partial(self,obj)
  def __call__(self,*args,**kwargs):
    now = time.time()
    if now - self.last_run >= self.interval:
      self.last_run = now
      return self.func(*args,**kwargs)

def throttle(interval):
  def decorator(func):
    _throttle = Throttle(func=func,interval=interval)
    return wraps(func)(_throttle)
  return decorator