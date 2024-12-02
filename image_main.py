# main.py
import requests
from PIL import Image
from io import BytesIO

def generate_image_from_prompt(prompt, api_token):
    """
    Function to generate an image from a text prompt using Hugging Face API.
    
    Args:
    - prompt (str): The text prompt for image generation.
    - api_token (str): Hugging Face API token for authorization.
    
    Returns:
    - PIL.Image: The generated image.
    """
    # API URL for the model
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

    # Prepare headers and payload
    headers = {"Authorization": f"Bearer {api_token}"}
    data = {"inputs": prompt}

    # Make the API request
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        # Load the image from the response content
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
