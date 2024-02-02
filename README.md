# imageToText

`imageToText` is a Django-based web application that allows users to extract text from images using OCR (Optical Character Recognition) technology. Built with simplicity and efficiency in mind, it provides an intuitive interface for users to upload images from which they wish to extract text. Additionally, it supports pasting images directly from the clipboard for a streamlined user experience.

This application is perfect for quickly digitizing written notes, extracting text from screenshots, or any other scenario where text needs to be extracted from an image.

## Live Demo

Try out `imageToText` live at: [https://motiimagetotext.pythonanywhere.com/](https://motiimagetotext.pythonanywhere.com/)

## Screenshots

![image](https://github.com/divyesh1099/imageToText/assets/65925922/1e6e1a5e-9191-4574-9a38-a7489ca87723)

![image](https://github.com/divyesh1099/imageToText/assets/65925922/f1c2f945-ee3e-4652-a4b9-f1e1c3780445)

![image](https://github.com/divyesh1099/imageToText/assets/65925922/d6110b55-5904-4ef3-922b-39c179c2ce26)

## Features

- **Image Upload**: Users can upload images in various formats (JPEG, PNG, etc.) to extract text.
- **Clipboard Support**: Paste images directly from the clipboard without the need to save and upload files manually.
- **Text Extraction**: Utilizes the powerful Tesseract OCR engine to provide accurate text extraction.
- **Responsive Design**: A clean, responsive interface that adapts to various screen sizes, ensuring a seamless experience on both desktop and mobile devices.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/divyesh1099/imageToText.git
cd imageToText
```

2. Create a virtual environment (optional):

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your web browser to view the application.

## Deployment

This project is deployed on PythonAnywhere. Check out the [official PythonAnywhere documentation](https://help.pythonanywhere.com/pages/) for guidance on deploying your own projects.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - OCR engine
- [Tailwind CSS](https://tailwindcss.com/) - For styling

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Motivation

I wanted a tool that quickly extracts text from image. I couldn't find a simple one, so I made it. 

## Acknowledgments

- Dino James (Keede)
- Tesseract
- Moti❤️
