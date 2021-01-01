import pytesseract as pt
from PIL import Image

image = Image.open('/home/sun/Desktop/abc.jpg')

text = pt.image_to_string(image)
print(type(text))
print(text)
print('='*20)

result = pt.image_to_boxes(image)
print(result)
print('='*20)
result = pt.image_to_data(image)
print(result)
print('='*20)

'''报错
# result = pt.image_to_osd(image)
# print(result)
# print('='*20)
# result = pt.image_to_pdf_or_hocr(image)
# print(type(result))
# print(result)
# print(result.decode())
'''