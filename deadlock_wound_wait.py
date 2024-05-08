# Description: This script demonstrates how to avoid deadlock by using wound-wait algorithm.

"""
	Wound-Wait:
   - In wound-wait, older transactions "wound" (abort) newer transactions if they attempt to lock an item of data held by them.
   - Newer transactions wait if they attempt to lock an item of data held by older transactions.
   - This script demonstrates wound-wait by acquiring locks in a specific order, allowing older transactions to wound newer transactions if necessary.
"""

import threading
import time

def main():
    def transaction1():
        print('Transaction 1 start')
        my_timestamp = time.time()
        while True:
            print('Transaction 1 waiting for lock1')
            if lock1.acquire(blocking=False):
                print('Transaction 1 lock1 acquired')
                time.sleep(1)
                print('Transaction 1 waiting for lock2')
                if lock2.acquire(blocking=False):
                    print('Transaction 1 lock2 acquired')
                    lock2.release()
                    print('Transaction 1 lock2 released')
                    lock1.release()
                    print('Transaction 1 lock1 released')
                    break
                else:
                    lock1.release()
                    print('Transaction 1 lock1 released due to wound-wait')
                    time.sleep(0.5)
            else:
                other_thread = threading.current_thread().name
                other_thread_timestamp = transaction2.timestamp
                if other_thread_timestamp < my_timestamp:
                    print(f'Transaction 1 wound-waiting for {other_thread}')
                    time.sleep(0.5)

    def transaction2():
        print('Transaction 2 start')
        my_timestamp = time.time()
        while True:
            print('Transaction 2 waiting for lock2')
            if lock2.acquire(blocking=False):
                print('Transaction 2 lock2 acquired')
                time.sleep(1)
                print('Transaction 2 waiting for lock1')
                if lock1.acquire(blocking=False):
                    print('Transaction 2 lock1 acquired')
                    lock1.release()
                    print('Transaction 2 lock1 released')
                    lock2.release()
                    print('Transaction 2 lock2 released')
                    break
                else:
                    lock2.release()
                    print('Transaction 2 lock2 released due to wound-wait')
                    time.sleep(0.5)
            else:
                other_thread = threading.current_thread().name
                other_thread_timestamp = transaction1.timestamp
                if other_thread_timestamp < my_timestamp:
                    print(f'Transaction 2 wound-waiting for {other_thread}')
                    time.sleep(0.5)

    lock1 = threading.Lock()
    lock2 = threading.Lock()

    transaction1.timestamp = time.time()
    transaction2.timestamp = time.time()

    t1 = threading.Thread(target=transaction1)
    t2 = threading.Thread(target=transaction2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Main done')

if __name__ == '__main__':
    main()