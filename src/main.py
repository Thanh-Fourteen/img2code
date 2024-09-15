import os
import extract
import getRespone as GR

def res_2_code(response, name_project, root, folder_ui):
    html_code, css_code = extract.extract_html_css(response)

    path_ui = os.path.join(root, folder_ui, name_project)
    if not os.path.exists(path_ui):
        os.makedirs(path_ui)

    name_html = "index.html"
    path_html = os.path.join(path_ui, name_html)
    name_css = "style.css"
    path_css = os.path.join(path_ui, name_css)
    extract.save_to_files(html_code, path_html, css_code, path_css)
    print("Đã tạo thành công file index.html và style.css!")
  

def slove(name_img, root, folder_img, folder_ui, save_res = True):
    path_img = os.path.join(root, folder_img, name_img)
    response = GR.getRes(path_img)
    name_project = name_img[:name_img.rfind(".")]
    res_2_code(response, name_project, root, folder_ui)

    if(save_res):
        folder_response = "response"
        name_response = name_img[:name_img.rfind(".")] + ".txt"
        path_save_res = os.path.join(root, folder_response, name_response)
        GR.save_file(response, path_save_res)
    
    return
  

if __name__ == "__main__":
    root = os.getcwd()
    folder_ui = "ui"
    folder_img = 'img'

    name_img = "company_home.png"

    print("Runing...........")
    res = slove(name_img, root, folder_img, folder_ui)
    print("Done..............")