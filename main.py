# Simultation of the producer consumer problem

import threading
import time
import random

NO_PRODUCERS = 10
NO_CONSUMERS = 15

MAX_DELAY_PRODUCER = 1
MAX_DELAY_CONSUMER = 1

def _simulateProducer(pcbuffer):
    """ Simulate a single producer.
    """
    print "Producer produces."
    print "new item"
    pcbuffer.append("new item")

def _simulateConsumer(pcbuffer):
    """ Simulate a single consumer.
    """
    print "Consumer consumes."
    print pcbuffer.pop()

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
