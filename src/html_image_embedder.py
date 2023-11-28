import base64
import imghdr
from selectolax.parser import HTMLParser


def embed_images(html, images):
    tree = HTMLParser(html)

    for img in tree.css("img"):
        src = img.attributes.get("src")

        if not src or src not in images:
            continue

        # Get the image data
        image_bytes = images[src]

        # Encode the image data as a Base64 string
        b64_encoded_image = base64.b64encode(image_bytes).decode()

        # Get the image extension
        extension = imghdr.what("", h=image_bytes)

        # Default to PNG for unknown image types
        if not extension:
            extension = "png"

        data_uri = f"data:image/{extension};base64,{b64_encoded_image}"
        img.attrs["src"] = data_uri

    return tree.body.html
