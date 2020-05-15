from PyPDF2 import PdfFileMerger


# Merging 2 PDF Files
merger = PdfFileMerger()
file_names = ["Scrum.pdf","python-for-iaas-automation.pdf"]
for file_name in file_names:
    # with open(file_name, "rb") as f:
    merger.append(file_name, import_bookmarks=False)


merger.write('Combined1.pdf')


# Rotate PDF file
# with open("python-for-iaas-automation.pdf","rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotated.pdf", "wb") as output:
#         writer.write(output)