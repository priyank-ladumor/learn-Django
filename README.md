<!-- virtual env create  -->
python -m venv .venv

<!-- virtual env activate (Git-Bash) -->
source .venv/Scripts/activate  

<!-- virtual env deactivate (Git-Bash) -->
deactivate

<!-- install Django  -->
pip install django

<!-- for create django server project -->
django-admin startproject myProject
cd myProject

<!--  Check version  -->
django-admin --version

<!-- Run the development server -->
python manage.py runserver

 <!-- Create a Django App -->
 <!-- Inside your project folder (where manage.py is) -->
python manage.py startapp any_name_want

 <!-- for creating requirements.txt -->
pip freeze > requirements.txt 

 <!-- for installing requirements.txt -->
pip install -r requirements.txt 

 <!-- how to remove all the packages in a virtual env -->
pip uninstall -r requirements.txt -y