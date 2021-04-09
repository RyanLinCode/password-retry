# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功"
# 如果不正確 就印出 "密碼錯誤! 還有_次機會!"
j = 3 #剩餘次數
password = 'a123456' 
while j > 0:
	j = j - 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功：')
		break #跳出迴圈
	else:
		print('密碼錯誤!')
		if j > 0:
			print('還有', j ,'次機會!')
		else:
			print('沒機會嘗試要鎖帳號了')
