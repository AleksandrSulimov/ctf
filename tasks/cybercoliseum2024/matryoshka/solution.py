import os
import zipfile

first = "flag_A1.zip"
password = first[:-4]
with zipfile.ZipFile(first) as z:
    z.extractall()
    nextzip = z.namelist()[0]

while nextzip.endswith(".zip"):
    password = password.encode("utf-8")
    print(f"zip={nextzip}, password={password}")
    with zipfile.ZipFile(nextzip) as z2:
        z2.setpassword(password)
        z2.extractall(pwd=password)
        password = nextzip[:-4]
        zip_to_delete = nextzip
        nextzip = z2.namelist()[0]
    os.remove(zip_to_delete)
