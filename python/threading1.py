from threading import Thread
import time

database_value = 0

# def square_numbers():
#     for i in range(100):
#         i * i
       
if __name__ == "__main__":
#     threads = []
#     num_threads = 10

# # create threads
# for i in range(num_threads):
#     thread = Thread(target=square_numbers)
#     threads.append(thread)
    
# # start thread
# for thread in threads:
#     thread.start()
    
# # join
# for thread in threads:
#     thread.join()
    
# print('end main')
    print('start_value', database_value)
    
def increase():
    global database_value
    
    local_copy = database_value
    
    # processing
    local_copy += 1
    time.sleep(0.1)
    
    database_value = local_copy  
    
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
print('end value', database_value)
    
print('end main')







 