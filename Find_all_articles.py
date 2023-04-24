# This code reads XML files from a folder and extracts information about authors and publication dates from articles that contain specific phrases in their MeshHeadings.
# It then appends the extracted information to a CSV file called 'result.csv'. The specific phrases to search for are defined in the 'phrases' list.
# The code uses the ElementTree library to parse the XML files and extract the desired information, and the csv library to write the extracted information to the CSV file.


import xml.etree.ElementTree as ET
import csv

# Initialize authors_list and publication_date_list
authors_list = []

for index in range(1, 26):
    count = str(index).zfill(4)
    file_path = f'C:\\Users\\dzunk\\Desktop\\folder\\pubmed23n{count}.xml'
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_string = file.read()

    # Create an ElementTree object
    root = ET.fromstring(xml_string)

    # Define the phrases to search for in DescriptorName or QualifierName
    phrases = ["polymorphism, genetic", "Gene Frequency", "Crossing Over, Genetic", "Chromosome Mapping",
               "Chromosome Aberrations", "Chromosome Disorders", "gene therapy", "genome editing", "genetic modification",
               "gene splicing", "genetic engineering", "gene transfer", "genetic modifications", "genetic changes",
               "gene mutation", "genetic mutation"]

    for article_element in (root.findall('.//PubmedArticle')):
        for mesh_heading in article_element.findall('.//MeshHeading'):
            descriptor_name = mesh_heading.find('DescriptorName').text
            qualifier_name = mesh_heading.find('QualifierName')
            if qualifier_name is not None:
                qualifier_name = qualifier_name.text

            if descriptor_name in phrases or (qualifier_name is not None and qualifier_name in phrases):
                # Extract authors and publication date
                authors = []
                pub_date = article_element.find('.//PubMedPubDate')
                year = pub_date.find('Year').text if pub_date is not None and pub_date.find('Year') is not None else ''
                month = pub_date.find('Month').text if pub_date is not None and pub_date.find('Month') is not None else ''
                day = pub_date.find('Day').text if pub_date is not None and pub_date.find('Day') is not None else ''
                for author in article_element.findall('.//Author'):
                    lastname = author.find('LastName').text if author.find('LastName') is not None else ''
                    firstname = author.find('ForeName').text if author.find('ForeName') is not None else ''
                    authors.append(f"{lastname} {firstname}")

                # Append authors and publication date to lists
                authors_list.append({
                    'author': authors,
                    'date': f"{year}-{month}-{day}"
                })
                break

with open('result.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for index in range(len(authors_list)):
        writer.writerow([authors_list[index]['author'], authors_list[index]['date']])