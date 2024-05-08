# Description: This script demonstrates how to avoid deadlock by using wait-die algorithm.

"""
	Wait-Die:
   - In wait-die, older transactions wait if they want to lock an item of data held by a newer transaction.
   - Newer transactions "die" if they attempt to lock an item of data held by an older transaction.
   - This script demonstrates wait-die by utilizing locks with blocking acquisition. Older transactions acquire locks first, while newer transactions wait.
"""

import threading
import time

def main():
    def transaction1():
        print('Transaction 1 start')
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
                    print('Transaction 1 lock1 released due to wait-die')
                    time.sleep(0.5)

    def transaction2():
        print('Transaction 2 start')
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
                    print('Transaction 2 lock2 released due to wait-die')
                    time.sleep(0.5)

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