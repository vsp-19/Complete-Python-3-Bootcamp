import zipfile
zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
zip_obj.extractall('extracted')
