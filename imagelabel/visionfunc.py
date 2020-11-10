import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'brave-octane-278909-304a5c353d56.json' #please put this json file in the same folder with this function file

# Imports the Google Cloud client library
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

# Instantiates a client
client = vision_v1.ImageAnnotatorClient()


# # Function to fatch labels from an Label


def detect_labels_url(url):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision_v1.ImageAnnotatorClient()
    image = vision_v1.types.Image()
    image.source.image_uri = url

    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))





