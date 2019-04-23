
import os
from os.path import join
import sys

import numpy as np # for sorting, b/c I was feeling lazy

from PyPDF2 import PdfFileMerger


if len(sys.argv) != 2:
	print("add folder for pdfconcat to use as an argument")
	sys.exit()
else:
	folder = sys.argv[1]

pdfs = os.listdir(folder)
pdfs = [join(folder, pdf) for pdf in pdfs if ".pdf" in pdf and "pset" in pdf]

try:
	nums = [int(pdfn.replace('.pdf','').split('-')[1]) for pdfn in pdfs]
	idxs = np.argsort(nums)
except:
	print("bad file names")
	print(pdfs)
	sys.exit()

merger = PdfFileMerger()
for idx in idxs:
	pdf = pdfs[idx]
	print('merging {}'.format(pdf))
	merger.append(pdf)

merger.write(join(folder, 'alek_westover_mathe23a_hw.pdf'))

