import threading


def big_countdown(n):
    while n:
        n -= 1


if __name__ == '__main__':
    # big_countdown(200000000)
    thread1 = threading.Thread(target=big_countdown, args=(100000000,))
    thread2 = threading.Thread(target=big_countdown, args=(100000000,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


