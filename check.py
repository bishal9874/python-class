start_num = int(29)
end_num = int(36)
cnt = start_num
while cnt <= end_num:
	# if number divisible by 7 and 5
	if cnt % 7 == 0 and cnt % 5 == 0:
		print(cnt, " is divisible by 7 and 5.")
	cnt += 1
