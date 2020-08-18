country = input('where are you from: ')
age = input('what is your age: ')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can get driving licence')
	else: 
		print('you cant get driving licence')
elif country == 'usa':
    if age >= 16:
    	print('you can get the driving licence')
    else:
    	print('you cant get the driving licence')