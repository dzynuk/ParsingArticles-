# The code reads compressed XML files from an input folder, decompresses them using gzip, and saves the extracted XML files to an output folder.
# It iterates through a range of file numbers, opens the .xml.gz files for reading and .xml files for writing, and writes the content of the .xml.gz files to the .xml files.


import gzip
import os

input_folder = 'C:\\Users\\dzunk\\PycharmProjects\\DataScientist(Parser)\\folderofarticles\\'
output_folder = 'C:\\Users\\dzunk\\Desktop\\folder'

for i in range(1, 1167):
    file_number = f'{i:04d}'

    gz_file_path = os.path.join(input_folder, f'pubmed23n{file_number}.xml.gz')
    xml_file_path = os.path.join(output_folder, f'pubmed23n{file_number}.xml')

    with gzip.open(gz_file_path, 'rb') as file_gz, open(xml_file_path, 'wb') as file_xml:
        file_content = file_gz.read()

        file_xml.write(file_content)


