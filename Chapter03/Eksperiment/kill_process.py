#%%
import multiprocessing
import time

def foo():
    print ('Starting function')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Process before execution:', p, p.is_alive())
    p.start()
    print ('Process running:', p, p.is_alive())
    p.terminate()
    print ('Process terminated:', p, p.is_alive())
    p.join()
    print ('Process joined:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)

#%%
import multiprocessing
import time

def pungsi():
    print ('Start')
    time.sleep(0.1)
    print ('Finish')

if __name__ == '__main__':
    p = multiprocessing.Process(target=pungsi)
    print ('BEFORE:', p, p.is_alive())
    
    p.start()
    print ('DURING:', p, p.is_alive())

    p.terminate()
    print ('TERMINATED:', p, p.is_alive())

    p.join()
    print ('JOINED:', p, p.is_alive())
# %%
