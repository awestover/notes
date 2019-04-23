# really nice library

import pyautogui as pg

pg.alert(text="Let us write some documentation", title="info", button="sounds legit")
x = pg.prompt(text="what is your documentation? (title: *)", title="documentation", default="")
title = x.split(":")[0]
body = " ".join(x.split(":")[1:])
yn = pg.confirm(text="this is your text right? title: " + title + "\nbody: " + body, title="confirm", buttons=['ok', 'no'])
if yn == 'ok':
  pwd = pg.password(text="input the phrase 'alek' to verify authenticity", title="password", default="alek", mask="*")
  if pwd == 'alek':
    pg.alert(text="you are good.", title='good', button='pretty good')
    with open("/home/alek/Desktop/documentation/{}.txt".format(title), "w") as f:
      f.write(body)
  
  else:
    pg.alert(text="failed", title="failed", button="i am a squid")
else:
  pg.alert(text="whatever man", title='disdain', button='goodbye')
