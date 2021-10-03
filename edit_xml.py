import xmltodict
import os


for f in os.listdir():
    if f.endswith('.xml'):
        xml_file = open(f, 'r+')
        data = xmltodict.parse(xml_file.read())
        new_path = '/train/'+data['annotation']['filename']
        data['annotation']['path']=new_path
        data['annotation']['folder']='train'
        xml_file.seek(0)
        xml_file.writelines(xmltodict.unparse(data,pretty=True))
        xml_file.truncate()
        xml_file.close()
