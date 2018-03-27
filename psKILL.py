import psutil
loud=False

for proc in psutil.process_iter():
	try:
		pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
	except psutil.NoSuchProcess:
		pass
	else:
		if loud:
			print(pinfo)
		if 'python' in pinfo['name']:
			if loud:
				print(pinfo['pid'])
			proc.kill()


