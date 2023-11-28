# html_image_embedder

A Python package that embeds images into HTML documents using data URIs.

## Installation

You can install html_image_embedder using pip:

```pip install html_image_embedder```

## Usage

To use html_image_embedder, you need to import the embed_images function from the package:

```python
from html_image_embedder import embed_images
```

The embed_images function takes two arguments: html and images. The html argument is a string containing the HTML code. The images argument is a dictionary mapping image URLs to image bytes. For example, you can use the requests library to get the image bytes from a URL:

```python
import requests

url = "https://example.com/image.png"
response = requests.get(url)
image_bytes = response.content
```

The embed_images function returns a modified HTML string with the image data embedded in the src attributes of the img tags. For example:

```python
html = "<html><body><img src='https://example.com/image.png'></body></html>"
images = {"https://example.com/image.png": image_bytes}
new_html = embed_images(html, images)
print(new_html)
# <html><body><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."></body></html>
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.