# Simultation of the producer consumer problem

import threading
import time
import random

# Sempahores to be shared between threads
emptyslots = None
filledslots = None

# mutex lock to access the buffer 
mutex = threading.Lock()

# size of buffer
BUFFER_SIZE = 10

# number of producers and consumers involved in the simulation
NO_PRODUCERS = 15
NO_CONSUMERS = 15

MAX_DELAY_PRODUCER = 1
MAX_DELAY_CONSUMER = 1

def _simulateProducer(pcbuffer):
    """ Simulate a single producer.
    """

    # wait for space on the buffer
    emptyslots.acquire()

    # obtain lock over the buffer
    mutex.acquire()

    # CRITICAL SECTION
    print "Producer produces :", "new item"
    pcbuffer.append("new item")
    # END CRITICAL SECTION

    # release lock over the buffer
    mutex.release()

    # signal the addition of a new item
    filledslots.release()

def _simulateConsumer(pcbuffer):
    """ Simulate a single consumer.
    """

    # wait for items on the buffer
    filledslots.acquire()

    # obtain lock over the buffer
    mutex.acquire()

    # CRITICAL SECTION
    print "Consumer consumes :", pcbuffer.pop()
    # END CRITICAL SECTION

    # release lock over the buffer
    mutex.release()

    # signal the consumption of a new item
    emptyslots.release()

def simulateProducer(pcbuffer):
    """ Simulate producers coming in. 
    """
    for i in xrange(NO_PRODUCERS):
        print "Producer {0} comes in.".format(i)
        _simulateProducer(pcbuffer)
        time.sleep(random.uniform(0, MAX_DELAY_PRODUCER))

def simulateConsumer(pcbuffer):
    """ Simulate the consumers coming in.
    """
    for i in xrange(NO_CONSUMERS):
        print "Consumer {0} comes in.".format(i)
        _simulateConsumer(pcbuffer)
        time.sleep(random.uniform(0, MAX_DELAY_CONSUMER))

def main():
    """ Simulate the producer consumer problem."""

    # the buffer used
    pcbuffer = []

    global emptyslots, filledslots
    emptyslots = threading.Semaphore(BUFFER_SIZE)
    filledslots = threading.Semaphore(0)

    # note the trailing , in  the tuple passed to args
    pthread = threading.Thread(target=simulateProducer, name="ProducerT", args=(pcbuffer, ))
    cthread = threading.Thread(target=simulateConsumer, name="ConsumerT", args=(pcbuffer, ))

    pthread.start()
    cthread.start()

    pthread.join()
    cthread.join()

    print "Done"

if __name__=="__main__":
    main()
