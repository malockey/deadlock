# Description: Demonstrates a deadlock situation in Python using threads and locks.

"""
    Deadlock Concept:
    - Deadlock occurs when multiple transactions compete for the same resources and cannot proceed because each transaction is waiting for a resource held by another.
    - In the initial script, deadlock is demonstrated as two threads attempt to acquire locks in a way that results in a circular dependency. Both threads wait indefinitely for locks held by each other, causing a deadlock situation.
"""

import threading
import time

def main():
    def transaction1():
        print('Transaction 1 start')
        lock1.acquire()
        print('Transaction 1 lock1 acquired')
        time.sleep(1)
        print('Transaction 1 waiting for lock2')
        lock2.acquire()
        print('Transaction 1 lock2 acquired')
        lock2.release()
        print('Transaction 1 lock2 released')
        lock1.release()
        print('Transaction 1 lock1 released')

    def transaction2():
        print('Transaction 2 start')
        lock2.acquire()
        print('Transaction 2 lock2 acquired')
        time.sleep(1)
        print('Transaction 2 waiting for lock1')
        lock1.acquire()
        print('Transaction 2 lock1 acquired')
        lock1.release()
        print('Transaction 2 lock1 released')
        lock2.release()
        print('Transaction 2 lock2 released')

    lock1 = threading.Lock()
    lock2 = threading.Lock()

    t1 = threading.Thread(target=transaction1)
    t2 = threading.Thread(target=transaction2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Main done')

if __name__ == '__main__':
    main()