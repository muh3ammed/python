import multiprocessing # pip install multiprocess

def start():

    print('Started')

if __name__ == '__main__':

    for i in range(25):

        p = multiprocessing.Process(target=start,)
        p.start()
        p.join() # Wait till processes finish
