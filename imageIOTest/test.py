from PIL import Image
from io import BytesIO
import base64
import matplotlib.pyplot as plt

data = '''R0lGODlhDwAPAKECAAAAzMzM/////wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLlN48CXF8m2iQ3YmmKqVlRtW4MLwWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw==''' 

data_new = ''
with open("test.txt", "r") as f:
  data_new = f.read()

import ipdb
ipdb.set_trace()

im = Image.open(BytesIO(base64.b64decode(data_new)))
plt.imshow(im)
plt.show()

