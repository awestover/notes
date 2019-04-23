
## motivation:
# imagine you don't want to save an image but need a representation of it
# an image can be represented in base64 in a kinda long string (approx 20K characters?)
# this can be displayed by a web browser or converted into pixel values and opperated on


import base64
from io import BytesIO

buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())


