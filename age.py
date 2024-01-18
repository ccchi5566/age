#if 的雙層架構

driving = input('有沒有開過車?')
age = input('輸入年齡:' )
age =int(age)
if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('偷開車')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照')
	else:
		print('快可以考了')
else:
	print('不要亂輸入')

