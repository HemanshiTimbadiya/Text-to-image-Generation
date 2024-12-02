# app.py
import streamlit as st
from image_main import generate_image_from_prompt

# Your Hugging Face API token (securely store and don't hard-code in production)
API_TOKEN = #Replace with your own hugging face model tokens

def main():
    st.title("Text-to-Image Generation with Hugging Face")

    # Input field for the text prompt
    prompt = st.text_input("Enter a text prompt for image generation:", "")

    # Button to generate the image
    if st.button("Generate Image"):
        if prompt:
            try:
                # Call the function to generate the image
                generated_image = generate_image_from_prompt(prompt, API_TOKEN)
                # Display the generated image
                st.image(generated_image, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error generating image: {e}")
        else:
            st.warning("Please enter a text prompt.")

if __name__ == "__main__":
    main()
