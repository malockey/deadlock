# Description: This script demonstrates how to avoid deadlock by using timeout on acquiring locks.

"""
    Timeout:
    - In timeout, if a transaction cannot acquire a lock within a specified time limit, it releases the acquired locks and retries later.
    - This script demonstrates timeout by setting a timeout value when acquiring locks. If a lock cannot be acquired within the timeout period, the transaction releases the locks and retries.
"""	

import threading
import time

def main():
    def transaction1():
        print('Transaction 1 start')
        if lock1.acquire(timeout=2):
            print('Transaction 1 lock1 acquired')
            time.sleep(1)
            print('Transaction 1 waiting for lock2')
            if lock2.acquire(timeout=2):
                print('Transaction 1 lock2 acquired')
                lock2.release()
                print('Transaction 1 lock2 released')
                lock1.release()
                print('Transaction 1 lock1 released')
            else:
                lock1.release()
                print('Transaction 1 lock1 released due to timeout')
        else:
            print('Transaction 1 failed to acquire lock1')

    def transaction2():
        print('Transaction 2 start')
        if lock2.acquire(timeout=2):
            print('Transaction 2 lock2 acquired')
            time.sleep(1)
            print('Transaction 2 waiting for lock1')
            if lock1.acquire(timeout=2):
                print('Transaction 2 lock1 acquired')
                lock1.release()
                print('Transaction 2 lock1 released')
                lock2.release()
                print('Transaction 2 lock2 released')
            else:
                lock2.release()
                print('Transaction 2 lock2 released due to timeout')
        else:
            print('Transaction 2 failed to acquire lock2')

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