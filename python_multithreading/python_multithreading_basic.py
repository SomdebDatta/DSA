def threading_module():
    """
    This is a very basic implementation of multithreading in python using the threading library.
    
    If you see the print statements from t1.start() till t2.join(), you'll notice that t2 starts before t1 ends which"""
    import threading
    import os

    def task1():
        print(f'Task1 assigned to thread - {threading.current_thread().name}')
        print(f'ID of process running this thread - {os.getpid()}')
    
    def task2():
        print(f'Task2 assigned to thread - {threading.current_thread().name}')
        print(f'ID of process running this thread - {os.getpid()}')

    # def task3():
    #     print(f'Task3 assigned to thread - {threading.current_thread().name}')
    #     print(f'ID of process running this thread - {os.getpid()}')
    
    print(f'ID of process running the main function - {os.getpid()}')

    print(f'Main thread name - {threading.current_thread().name}')

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    # t3 = threading.Thread(target=task3, name='t3')

    t1.start()
    t2.start()
    # t3.start()

    t1.join()
    t2.join()
    # t3.join()

def concurrent_futures_module():
    """
    """
    import concurrent.futures

    def worker():
        print('Worker thread running...')
    
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    pool.submit(worker)
    pool.submit(worker)
    pool.submit(worker)
    pool.submit(worker)

    pool.shutdown(wait=True)

    print('Main thread continuing to run...')


if __name__ == '__main__':
    # threading_module()
    concurrent_futures_module()
