from PIL import Image
import os

downloadsFolder = "D:/Users/carlos.alvarado/Downloads/"
picturesFolder = "D:/Users/carlos.alvarado/Downloads/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        # if extension in [".jpg", ".jpeg", ".png"]:
        #     picture = Image.open(downloadsFolder + filename)
        #     picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
        #     os.remove(downloadsFolder + filename)
        #     print(name + ": " + extension)

        if extension in [".exe"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/ejecutables/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".csv"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/csv/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".zip"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/comprimidos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".7z"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/comprimidos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".rar"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/comprimidos/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".xlsx"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/excel/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".xls"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/excel/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".png"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/img/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".jpeg"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/img/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".JPG"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/img/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".PNG"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/img/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".JPEG"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/img/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".jpg"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/img/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".msi"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/msiMicrosoft/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".pdf"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/pdf/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".pbix"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/powerBI/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".pptx"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/powerPoint/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".txt"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/txt/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".docx"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/word/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".doc"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/word/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".mdb"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/access/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".accdb"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/access/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".html"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/paginasWeb/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".sql"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/consultasSQL/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        if extension in [".mp4"]:
            musicFolder = "D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/grabaciones/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        
        



