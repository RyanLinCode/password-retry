# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功"
# 如果不正確 就印出 "密碼錯誤! 還有_次機會!"
j = 3 #剩餘次數
password = 'a123456' 
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功：')
		break #跳出迴圈
	else:
		j = j - 1
		print('密碼錯誤! 還有', j ,'次機會!')
		if j == 0:
			break