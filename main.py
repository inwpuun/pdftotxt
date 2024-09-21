import pdftojpg
import jpgtotxt
from pathlib import Path
import pytesseract # type: ignore

def create_directory(directory_path):
    directory = Path(directory_path)
    result = directory.exists()
    if not directory.exists():
        directory.mkdir(parents=True)

    return result

def is_file_exist(directory_path, filename):
    directory = Path(directory_path) 
    file_path = directory / filename

    return file_path.is_file()

def list_files(directory_path):
    directory = Path(directory_path)
    result = []

    # List all files in the directory
    for file in directory.iterdir():
        if file.is_file():  # Check if it's a file
            result.append(file.name)

    return result

def main():
    files = list_files('pdf-files')
    for file in files:
        
        print('convert pdf to jpg file:', file, end=' ')
        
        already_convert = create_directory('jpg-files/' + file.split('.')[0])
        if already_convert:
            print('--> already convert')
        else: 
            pdftojpg.convert_pdf_to_jpg('pdf-files/' + file, 'jpg-files/' + file.split('.')[0] + '/')
            print()

        print('convert jpg to txt file:', file, end=' ')
        already_convert = is_file_exist('txt-files', file.split('.')[0] + '.txt')
        if already_convert:
            print('--> already convert')
            continue
        print()
        with open('txt-files/' + file.split('.')[0] + '.txt', 'w') as f:
            jpg_files = sorted(list_files('jpg-files/' + file.split('.')[0]))
            for jpg_file in jpg_files:
                print('convert jpg to txt file:', jpg_file)
                txt = jpgtotxt.convert_jpg_to_txt('jpg-files/' + file.split('.')[0] + '/' + jpg_file)
                f.write(txt)
            print()
        print('\n')

    
        
        

if __name__ == '__main__':
    print("python-tesseract version: ", pytesseract.get_tesseract_version())
    print("Supported thai") if 'tha' in pytesseract.get_languages() else print("Not supported thai")

    create_directory('jpg-files')
    create_directory('txt-files')
    main()
    