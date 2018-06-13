# really nice library

import pyautogui as pg

pg.alert(text="hey", title="hmm", button="well")
pg.prompt(text="hey", title="al", default="asdf")
pg.confirm(text="hey", title="al", buttons=['ok', 'no'])
pg.password(text="hey", title="al", default="asdf", mask="*")
