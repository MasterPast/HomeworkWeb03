import concurrent.futures
import logging
from multiprocessing import cpu_count
from time import time


examp_numb = (128, 255, 99999, 10651060, 387879678)
# a = []
# b = []
# c = []
# d = []
temp_num = []


def factorize(number):

    timer = time()
    for num in number:
        temp = []
        for el in range(num + 1):
            if el != 0 and (num % (el)) == 0:
                temp.append(el)
        temp_num.append(temp)
    logging.debug(f'Function factorize in 1 thread {time() - timer}sec')

    return temp_num


def cpu_factorize(num):

    timer = time()
    temp = []
    for el in range(num+1):
        if el != 0 and (num % (el)) == 0:
            temp.append(el)

    return temp


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG,
                       format='%(threadName)s %(message)s')
    a, b, c, d, e = factorize(examp_numb)

    time_cpu = time()
    with concurrent.futures.ProcessPoolExecutor(cpu_count()) as executor:

        for number, fact in zip(examp_numb, executor.map(cpu_factorize, examp_numb)):
            logging.debug('%s is factorize of %s' % (fact, number))

    logging.debug(f'Function factorize in {cpu_count()}`th cores {time() - time_cpu}sec')
