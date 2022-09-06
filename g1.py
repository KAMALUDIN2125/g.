import random
import sys
import time
def mengetik(s):
	for c in s + '\n' :
	    sys.stdout.write(c)
	    sys.stdout.flush()

	    time.sleep(random.random() * 0.5)

mengetik('JANGAN LUPA SHOLAT 5 WAKTU JANGAN LUPA BERUSAHA JANGAN LUPA SEMANGAT UNTUK MENCAPAI KESUKSESAN')
