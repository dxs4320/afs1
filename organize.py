from distutils import extension
import os
import shutil

source ="C:/Users/nshan/Downloads"
dest = "C:/Dakshitha py"
listOfFiles = os.listdir(source)
for filename in listOfFiles:
    name,exten = os.path.splitext(filename)
    if exten in [".pdf",".ppt",".txt",".docx",".xlsx",".pptx",".PDF",".doc",".xls"]:
        p1 = source + "/" + filename
        p2 = dest + "/" + "Docs"
        p3 = dest + "/" + "Docs" + "/" + filename
        if os.path.exists(p2):
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            shutil.move(p1,p3)