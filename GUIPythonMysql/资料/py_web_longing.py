# -*- coding: cp936 -*-
import web
import os


data = {
	'username': 'admin',
	'password': '123456'
}

urls = (
	'/', 'hello',
	'/login', 'login',
	'/regist', 'regist'
)
app = web.application(urls, globals())


class hello():
	def __init__(self):
		self.render = web.template.render('templates/')

	def GET(self):
		return self.render.form()


class login():
	def POST(self):
		para = web.input()
		username = para['username']
		password = para['password']

		# TODO:...
		# if authenticate(username,password):
		# return render.hello(username)
		return 'hello world'


class regist():
	def GET(self):
		return 'hello world'

	# return self.render.form()
	def POST(self):
		para = web.input()
		username = para['username']
		password = para['password']

		# TODO:...
		return 'hello world'


if __name__ == '__main__':
	app.run()