def main():
    import threading
    import time

    def thread1():
        print('Thread1 start')
        lock1.acquire()
        print('Thread1 lock1 acquired')
        time.sleep(1)
        print('Thread1 waiting for lock2')
        lock2.acquire()
        print('Thread1 lock2 acquired')
        lock2.release()
        print('Thread1 lock2 released')
        lock1.release()
        print('Thread1 lock1 released')

    def thread2():
        print('Thread2 start')
        lock2.acquire()
        print('Thread2 lock2 acquired')
        time.sleep(1)
        print('Thread2 waiting for lock1')
        lock1.acquire()
        print('Thread2 lock1 acquired')
        lock1.release()
        print('Thread2 lock1 released')
        lock2.release()
        print('Thread2 lock2 released')

    lock1 = threading.Lock()
    lock2 = threading.Lock()

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Main done')

if __name__ == '__main__':
    main()