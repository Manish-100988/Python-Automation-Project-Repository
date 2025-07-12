# ==============================================================================
# 3. Main Thread and Naming
# ==============================================================================

# Definition:
# This program demonstrates how to identify and name threads including the main thread.
# Helpful for debugging and tracking thread behavior in multi-threaded programs.

import threading  # Required to work with threads

# Get the main thread using current_thread()
main_thread = threading.current_thread()  # Fetches the thread object for the currently executing thread
print(f'\n[Main] Current thread: {main_thread.name}')  # Output will typically be "MainThread"

# Define a simple function to print the current thread's name
def print_thread_name():
    # Print name of the thread executing this function
    print(f'[Main] New thread started: {threading.current_thread().name}')  # Name is auto-assigned unless specified

# Create a new thread for the above function
t5 = threading.Thread(target=print_thread_name)  # Creates a new thread without a custom name (default: Thread-N)

# Print the default name assigned to the thread before it starts
print(f'[Main] Created thread name: {t5.name}')  # Helps understand thread naming mechanism

# Start the thread
t5.start()  # Transitions from Newborn → Runnable → Running, executes print_thread_name

# Wait for the thread to complete
t5.join()   # Blocks main thread until t5 completes (Running → Dead)
