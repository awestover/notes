import os
import win32com.client
 
DOC_FILEPATH = "c:/temp/something.docx"
doc = win32com.client.GetObject(DOC_FILEPATH)
text = doc.Range().Text

# do something with the text... 
with open("something.txt", "wb") as f:
	f.write(text.encode("utf-8"))
 
os.startfile("something.txt")

