from bs4 import BeautifulSoup as bs
import os
import shutil
import subprocess


def user_selection():
    print("Please choose one of the following options: ")
    print("1) Make project")
    print("2) Edit project")
    print("3) Remove project")
    choice = input("Please choose one of the following options: ")
    

def make_project():
    project_name = str(input("Enter the name of the project: ") + ".html")
    project_title = input("Enter the project title: ")
    project_image = input("Enter the image name of the project: ")
    project_description = input("Enter the description of the project: ")
    
    shutil.copyfile("project_template.html", project_name)
    
    html = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), project_name))
    clean_html = bs(html, "html.parser")
    clean_html.find('p', id="projectTitle").string = project_title
    clean_html.find('h2', id="bigTitle").string = project_title
    clean_html.find('p', id="projectDescription").string = project_description
    clean_html.find('img', id="picture")['src'] = ("images/gallery/" + project_image + ".jpg")
    
    with open(project_name, 'w') as new_site:
        new_site.write(str(clean_html))
  
    


make_project()
    
    