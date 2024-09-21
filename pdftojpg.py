from pdf2image import convert_from_path # type: ignore

def convert_pdf_to_jpg(pdf_path, output_path):
    images = convert_from_path(pdf_path)
    for i in range(len(images)):
        images[i].save(output_path + 'page'+ str(i) +'.jpg', 'JPEG')
