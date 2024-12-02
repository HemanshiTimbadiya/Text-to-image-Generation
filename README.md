# Text-to-Image Generation

## Project Overview
This project demonstrates the use of a **Text-to-Image Generation** model, enabling the creation of high-quality images based on textual prompts. Utilizing Hugging Face's pretrained **DALL·E Mini** model, the application generates images directly from user-provided descriptions.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Model Description](#model-description)
- [Installation & Usage](#installation--usage)
- [Streamlit Deployment](#streamlit-deployment)
- [Acknowledgments](#acknowledgments)

---

## Technologies Used
| Technology       | Description                                     |
|------------------|-------------------------------------------------|
| **Python**       | Core programming language.                     |
| **Hugging Face** | Access to pretrained models via Transformers.  |
| **Pillow (PIL)** | Image processing library for handling outputs. |
| **Streamlit**    | Web app framework for deployment.              |

---

## Project Structure
| File/Directory         | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `app.py`               | Streamlit application for text-to-image generation.                   |
| `main.py`              | Core implementation of text-to-image generation logic.                |
| `requirements.txt`     | List of dependencies for running the project.                         |
| `README.md`            | Project documentation and instructions.                               |

---

## Model Description
This project uses the **DALL·E Mini** model, a scaled-down version of OpenAI’s DALL·E, for generating images from text prompts. The pretrained model is accessed via Hugging Face’s Transformers library. 

- **Input:** A textual description or prompt.
- **Output:** An image representing the input text.

---

## Installation & Usage

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/HemanshiTimbadiya/text-to-image-generation.git


  2. Navigate to the project directory:
   ```bash
   cd text-to-image-generation
   ```
 3. Install the required packages:
   ```bash
   pip install -r requirements.txt
```
### Usage
- Run the analysis in a Jupyter Notebook.
- To deploy the project using Streamlit, run:
  ```bash
  streamlit run image_app.py 

