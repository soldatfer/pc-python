# Simultation of the producer consumer problem

import threading
import time

def simulateProducer(pcbuffer, buffer_limit):
    """ Simulate the producer. 
    
    For now simply prints out "Producer" buffer_limit times.
    """
    for i in xrange(buffer_limit):
        print "Producer"
        time.sleep(0.5)

def simulateConsumer(pcbuffer, buffer_limit):
    """ Simulate the consumer. 
    
    For now simply prints out "Consumer" 10 times.
    """
    for i in xrange(buffer_limit):
        print "Consumer"
        time.sleep(0.5)

def main():
    """ Simulate the producer consumer problem."""

    # the buffer used
    pcbuffer = []

    # limit of the buffer
    buffer_limit = 10

    pthread = threading.Thread(target=simulateProducer, name="ProducerT", args=(pcbuffer, buffer_limit))
    cthread = threading.Thread(target=simulateConsumer, name="ConsumerT", args=(pcbuffer, buffer_limit))

    pthread.start()
    cthread.start()

    pthread.join()
    cthread.join()

    print "Done"

if __name__=="__main__":
    main()
