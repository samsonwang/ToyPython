#! /usr/bin/python3

try:
	print('try')
	#r = 10 / ord('a')
	r = 10 / int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionerror:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')






