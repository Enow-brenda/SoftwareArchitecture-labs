import pygame
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def resize_image():
    try:
        # Get file from request
        file = request.files["image"]
        output_format = request.form.get("format", "png")  # Default to PNG
        width = int(request.form.get("width", 200))
        height = int(request.form.get("height", 200))

        # Load image into Pygame
        file_path = "/tmp/input_image"
        file.save(file_path)
        pygame.init()
        image = pygame.image.load(file_path)

        # Resize the image
        resized_image = pygame.transform.scale(image, (width, height))

        # Save resized image
        output_path = f"/tmp/output_image.{output_format}"
        pygame.image.save(resized_image, output_path)

        # Send the resized image back as a response
        with open(output_path, "rb") as output_file:
            return output_file.read(), 200, {"Content-Type": f"image/{output_format}"}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

