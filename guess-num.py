# 產生一個隨機整數1~100 (不要印出)
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"終於猜對了"
# 猜錯的話 要告訴他 比答案 大/小
import random

start = int(input('請輸入猜數字範圍起始值: '))
end = int(input('請輸入猜數字範圍結束值: '))

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('你猜的數字比答案大')
	elif num < r:
		print('你猜的數字比答案小')
	print('這是你猜的第', count, '次')