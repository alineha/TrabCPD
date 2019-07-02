import traceback
import threading
from queue import Queue

def tk_call_async(window, computation, args=(), kwargs={}, callback=None, errback=None, polling=500):
	future_result = _request_result_using_threads(computation, args=args, kwargs=kwargs)
    
	if callback is not None or errback is not None:
		_after_completion(window, future_result, callback, errback, polling)
        
	return future_result

def _request_result_using_threads(func, args, kwargs):
    future_result = Queue()

    worker = threading.Thread(target=_compute_result, args=(func, args, kwargs, future_result))
    worker.daemon = True
    worker.start()

    return future_result


def _after_completion(window, future_result, callback, errback, polling):
    def check():
        try:
            result = future_result.get(block=False)
        except:
            window.after(polling, check)
        else:
            if isinstance(result, Exception):
                if errback is not None:
                    errback(result)
            else:
                if callback is not None:
                    callback(result)
                
    window.after(0, check)

def _compute_result(func, func_args, func_kwargs, future_result):
    try: 
        _result = func(*func_args, **func_kwargs)
    except Exception as errmsg:
        _result = Exception(traceback.format_exc())

    future_result.put(_result)