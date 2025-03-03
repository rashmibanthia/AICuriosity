# This example will:
# Create a thread pool with 1 worker
# Submit a task that takes 2 seconds to complete
# Attempt to get the result with a 1-second timeout
# Catch the timeout exception when the task isn't completed in time

import concurrent.futures
import time

def delayed_hello():
    time.sleep(5)  # Simulate work that takes 2 seconds
    return "Hello World!"

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # Submit the function to the executor
    future = executor.submit(delayed_hello)
    
    try:
        # Wait for result with 1-second timeout (shorter than the work duration)
        result = future.result(timeout=7)
        print(result)
    except concurrent.futures.TimeoutError:
        print("Task took too long! (Timeout after 1 second)")
    except Exception as e:
        print(f"An error occurred: {e}")