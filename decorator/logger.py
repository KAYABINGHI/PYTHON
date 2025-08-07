
import time


def logger(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        diff = end_time - start_time
        log_message = f"Function '{fn.__name__}' executed in {diff:.4f} seconds"
        print(log_message)
        write_file("logger.txt", log_message)
        return result
    return wrapper


def write_file(f_name, text):
    with open(f_name, 'a') as file:
        file.write(f'\n{text}\n')



@logger
def counter():
    for n in range(0,2000000):
        print(n)


@logger
def sum (*args):
    ans = 0
    for n in args:
        print(ans, "=", ans, "+", n)
        ans = ans + n
    
    print("Ans is", ans)
    return ans

counter()