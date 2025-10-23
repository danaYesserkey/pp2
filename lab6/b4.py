import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"square {number} after {delay_ms} milliseconds {result}")

delayed_sqrt(144, 81)
