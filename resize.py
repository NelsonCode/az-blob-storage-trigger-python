import azure.functions as func
from PIL import Image
from io import BytesIO

from blob import upload_blob

width = 640
height = 480

SIZE = width, height


def resize_image(file: func.InputStream):
    img = Image.open(BytesIO(file.read()))
    img.thumbnail(SIZE)
    # SAVES THE "FILE" IN MEMORY AND THEN RETURNS IT
    with BytesIO() as myfile:
        img.save(myfile, format="PNG")
        filename = file.name.split("/")[1]
        container = "images-mobile"
        upload_blob(filename=filename, container=container,
                    data=myfile.getvalue())

