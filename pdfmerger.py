from PyPDF2 import PdfMerger  # PdfMerger is a class from the PyPDF2 library in Python,
                              # used to merge multiple PDF files into a single PDF file

# a list of PDF file paths stored in the pdf_files variable.
pdf_files = [r'D:\Experience letter\Employee Ex_Letter.pdf',
             r'D:\Experience letter\NTT Relieving Letter.pdf',
             r'D:\Experience letter\HCL ExperienceLetter.pdf']

# मर्जर ऑब्जेक्ट बनाएं
merger = PdfMerger()
#
# - merger: Variable name to store the PdfMerger object.
# - PdfMerger: Class name from the PyPDF2 library.
# - (): Initializes a new instance of the PdfMerger class.

try:
    #
    # For Loop Syntax
    # for variable in iterable:
    for pdf in pdf_files:
        # merger.append(pdf)
        ''' 
        Appending a PDF File to the Merger
        merger.append(pdf)
        - merger: The PdfMerger object created earlier.
        - append(): Method of the PdfMerger class to add a PDF file.
        - pdf: The PDF file path to be appended (stored in the pdf variable from the for loop).
        '''
        merger.append(pdf)

    # मर्ज की गई फाइल को सेव करें
    output_file = r'D:\Experience letter\Combine_Experience_Certificate.pdf'

    # ("\n"
    #  "    output_file = r'D:\Experience letter\Combine_Experience_Certificate.pdf'\n"
    #  "    output_file: Variable name to store the file path.\n"
    #  "    =: Assignment operator.\n"
    #  "    r: Prefix indicating a raw string (ignores backslash escape sequences).\n"
    #  "    D:\Experience letter\Combine_Experience_Certificate.pdf': File path as a string.\n"
    #  "\n"
    #  "    ")
# '''
# Raw String Example
#
# print(r'\n is a new line')
#
# Output: \n is a new line
#
# Read Mode Example
#
# file = open('example.txt', 'r')
#
# Opens example.txt in read mode.
#
# '''


    merger.write(output_file)
    print(f"All PDFs merged into {output_file}")
# merger.write(output_file)
#
# - merger: The PdfMerger object.
# - write(): Method to write the merged PDF content.
# - output_file: The file path where the merged PDF will be saved.

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    merger.close()
