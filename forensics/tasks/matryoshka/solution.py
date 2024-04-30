import os
import zipfile

current_zip = "flag_A1.zip"
password = current_zip[:-4]
with zipfile.ZipFile(current_zip) as z:
    z.extractall()
    next_zip = z.namelist()[0]

while next_zip.endswith(".zip"):
    password = password.encode("utf-8")
    print(f"zip={next_zip}, password={password}")
    with zipfile.ZipFile(next_zip) as z2:
        z2.setpassword(password)
        z2.extractall(pwd=password)
        password = next_zip[:-4]
        zip_to_delete = next_zip
        next_zip = z2.namelist()[0]
    os.remove(zip_to_delete)
