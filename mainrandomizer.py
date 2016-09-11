

import random

qcounter = list(range(25))
print (qcounter)

random.shuffle(qcounter)
print (qcounter)

current_q_increment = 0
current_q = qcounter[0]