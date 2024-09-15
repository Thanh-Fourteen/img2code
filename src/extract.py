import os

def extract_html_css(content):
    """
    Đọc file text chứa code HTML và CSS, sau đó tách chúng thành hai string riêng biệt.

    Args:
        path_text (str): Tên file text.

    Returns:
        tuple: Tuple chứa code HTML và CSS (html_code, css_code).
    """
    html_start = content.find("```html") + len("```html\n")
    html_end = content.find("\n```", html_start + len("```html"))
    html_code = content[html_start:html_end]

    css_start = content.find("```css") + len("```css\n")
    css_end = content.find("\n```", css_start + len("```css"));
    css_code = content[css_start:css_end]

    return html_code, css_code


def save_to_files(html_code, path_html, css_code, path_css):
    """
    Lưu code HTML và CSS vào hai file riêng biệt.

    Args:
        html_code (str): Code HTML.
        css_code (str): Code CSS.
    """
    with open(path_html, "w") as html_file:
        html_file.write(html_code)

    with open(path_css, "w") as css_file:
        css_file.write(css_code)


if __name__ == "__main__":
    root = os.getcwd()
    folder_response = "response"
    name_response = "contact_form.txt"
    path_text = os.path.join(root, folder_response, name_response)
    with open(path_text, 'r') as f:
        content = f.read()
    html_code, css_code = extract_html_css(path_text)

    folder_test = "test"
    name_html = "index.html"
    path_html = os.path.join(root, folder_test, name_html)
    name_css = "style.css"
    path_css = os.path.join(root, folder_test, name_css)
    save_to_files(html_code, path_html, css_code, path_css)
    print("Đã tạo thành công file index.html và style.css!")