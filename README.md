## README.md

# Image-to-HTML-CSS

This project utilizes the Google Gemini API to convert images of UI designs into functional HTML and CSS code.

## How it Works:

1. **Image Input:** Place your UI design image (PNG format) in the `img` folder.
2. **API Call:** The `getRespone.py` script sends the image to the Gemini API with a prompt to extract all UI details and generate HTML/CSS code.
3. **Response Processing:** The API response, containing the generated code, is saved in the `response` folder as a text file.
4. **Code Extraction:** The `extract.py` script parses the response text file and separates the HTML and CSS code.
5. **File Generation:** The extracted HTML and CSS code is saved into separate files within a new project folder under the `ui` directory. The project folder name is derived from the input image name.

## Requirements:

* Python 3.x
* Google Gemini API access (and API key)
* Pillow (PIL) library

## Installation:

1. Clone the repository:

```bash
git clone https://github.com/your-username/Image-to-HTML-CSS.git
```

2. Navigate to the project directory:

```bash
cd Image-to-HTML-CSS
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up your Google Gemini API key:
    -  Replace `"Your_API"`  in `getRespone.py` with your actual API key.

## Usage:

1. Place your UI design image in the `img` folder.
2. Replace `"Your_API"` with your actual Google Gemini API key in the `getRespone.py`
3. Replace `"name_img"` function main of file `main.py`
2. Run the `main.py` script:

```bash
python main.py
```

This will generate the HTML and CSS files for your image in the `ui` folder.

## Example:

Let's say you have a UI design image named `pricing.png` in the `img` folder. After running `main.py`, you will find a new folder named `pricing` inside the `ui` folder, containing `index.html` and `style.css` files.

## Notes:

* The accuracy of the generated code depends on the quality and complexity of the input image.
* You can customize the generated code by modifying the prompts in the `getRespone.py` script.
* The `save_res` parameter in the `slove` function within `main.py` controls whether to save the API response in the `response` folder. You can set it to `False` to disable this feature.

## Contributing:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


Please note that you should replace `"Your_API"` with your actual Google Gemini API key in the `getRespone.py` file before running the code. 
