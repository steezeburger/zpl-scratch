import imgkit
from PIL import Image
from zpl import label

def html_to_image(html, output_file):
    imgkit.from_string(html, output_file)

def image_to_zpl(image_file, output_file):
    img = Image.open(image_file)
    img = img.convert('1')  # Convert to black and white
    zpl_label = label.Label(38, 19)
    zpl_label.origin(0, 0)
    zpl_label.write_graphic(img, 134)
    zpl_label.endorigin()

    with open(output_file, 'w') as f:
        f.write(zpl_label.dumpZPL())

def main():
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 24px;
            }
            p {
                font-size: 18px;
            }
            .barcode {
                font-family: "CCode39";
                font-size: 36px;
            }
        </style>
        </head>
        <body>
            <h1>Product Name</h1>
            <div>Description: This is a product description.</div>
            <div>*12345678*</div>
        </body>
        </html>
        '''

    image_output = 'label.png'
    zpl_output = 'label.zpl'

    html_to_image(html_template, image_output)
    image_to_zpl(image_output, zpl_output)

if __name__ == '__main__':
    main()
