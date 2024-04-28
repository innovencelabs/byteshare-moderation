from io import BytesIO

from PIL import Image
from transformers import pipeline

classify = pipeline("image-classification", model="Falconsai/nsfw_image_detection")


def scan_image(file_stream):
    pil_image = _convert_to_pil_image(file_stream)

    result = classify(pil_image)

    nsfw_score = next(
        (item["score"] for item in result if item["label"] == "nsfw"), None
    )

    if nsfw_score > 0.9:
        return False
    else:
        return True


def _convert_to_pil_image(file_stream):
    image_buffer = BytesIO(file_stream.read())
    try:
        image = Image.open(image_buffer)
        return image
    except OSError:
        raise ValueError("Unsupported image format")
