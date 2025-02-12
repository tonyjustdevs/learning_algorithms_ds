from showcallstack import showcallstack, getcallstack

import logging # https://realpython.com/python-logging/

logging.basicConfig(
  	filename="rec_max_bad.log",
  	encoding="utf-8",
	filemode="a",
	level=logging.DEBUG,
	format="{asctime} - {levelname} - {message}",
	style="{")

logger = logging.getLogger(__name__)
def max_rec_bad(arr): 
	if len(arr)==1:
		showcallstack()
		callstackstr = getcallstack()
		logging.info(callstackstr)
		return arr[0]
	if arr[0]>max_rec_bad(arr[1:]):
		return arr[0]
	else:
		return max_rec_bad(arr[1:])

max_rec_bad([1,9,6,4,7,2,4])
		