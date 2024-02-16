import os
import sys
from PyPDF2 import PdfReader, PdfMerger
import re
import fitz  # PyMuPDF

def is_pdf_document(file_path, max_width=1000, max_height=1000):
    try:
        doc = fitz.open(file_path)
        for page_num in range(doc.page_count):
            page = doc[page_num]
            rect = page.rect
            width, height = rect.width, rect.height
            if width > max_width or height > max_height:
                return False  # Filter out PDFs with dimensions above the threshold
        return True
    except Exception as e:
        print(f"Error checking PDF type: {e}")
        return False

def is_pdf_less_than_20_pages(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            return len(pdf_reader.pages) <= 20
    except Exception as e:
        print(f"Error checking number of pages for {file_path}: {e}")
        return False

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def concatenate_pdfs_recursive(directory, output_filename):
    merger = PdfMerger()

    # Keep track of files being concatenated
    concatenated_files = []

    # Recursively get all PDF files in the specified directory
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        if "svg-inkscape" in root:
            continue

        for file in files:
            if "cocreate" not in file and file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))

    pdf_files.sort(key=natural_sort_key)  # Sort files naturally

    for pdf_file in pdf_files:
        # Check if the PDF has 20 or fewer pages
        if is_pdf_less_than_20_pages(pdf_file) and is_pdf_document(pdf_file):
            merger.append(pdf_file)
            concatenated_files.append(pdf_file)

    # Write the merged PDF to the output file
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)

    print(f'Merged PDFs (with 20 or fewer pages) saved to: {output_filename}')
    print('Concatenated files:')
    for file_path in concatenated_files:
        print(file_path)

if len(sys.argv) != 2:
    print("Usage: python script_name.py <directory_path>")
    sys.exit(1)

input_directory = sys.argv[1]
input_directory = input_directory.rstrip('/')

output_filename = input_directory + '.pdf'
concatenate_pdfs_recursive(input_directory, output_filename)


#  import os
#  import sys
#  from PyPDF2 import PdfReader, PdfMerger

#  def is_pdf_less_than_20_pages(file_path):
#      try:
#          with open(file_path, 'rb') as pdf_file:
#              pdf_reader = PdfReader(pdf_file)
#              return len(pdf_reader.pages) <= 20
#      except Exception as e:
#          print(f"Error checking number of pages for {file_path}: {e}")
#          return False

#  def concatenate_pdfs_recursive(directory, output_filename):
#      merger = PdfMerger()

#      # Keep track of files being concatenated
#      concatenated_files = []

#      # Recursively get all PDF files in the specified directory
#      for root, dirs, files in os.walk(directory):
#          print("SCANNING\t", root)
#          # Check if the current directory is "svg-inkscape" and skip it
#          if "svg-inkscape" in root:
#              print("SKIP", root, dirs, files)
#              continue

#          pdf_files = [file for file in files if file.endswith('.pdf')]
#          pdf_files.sort()  # Sort files alphabetically

#          for pdf_file in pdf_files:
#              file_path = os.path.join(root, pdf_file)

#              # Check if the PDF has 20 or fewer pages
#              if is_pdf_less_than_20_pages(file_path):
#                  merger.append(file_path)
#                  concatenated_files.append(file_path)

#      # Write the merged PDF to the output file
#      with open(output_filename, 'wb') as output_file:
#          merger.write(output_file)

#      print(f'Merged PDFs (with 20 or fewer pages) saved to: {output_filename}')
#      print('Concatenated files:')
#      for file_path in concatenated_files:
#          print(file_path)

#  if len(sys.argv) != 2:
#      print("Usage: python script_name.py <directory_path>")
#      sys.exit(1)

#  input_directory = sys.argv[1]
#  input_directory = input_directory.rstrip('/')

#  output_filename = input_directory + '.pdf'
#  concatenate_pdfs_recursive(input_directory, output_filename)

