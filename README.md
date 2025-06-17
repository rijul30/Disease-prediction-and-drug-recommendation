gitDownload DBBrowser for SQLITE database
https://sqlitebrowser.org/dl/

Technologies used:
asgiref==3.8.1  
Django==4.0  
joblib==1.3.2  
numpy==1.26.4  
pillow==10.2.0  
scikit-learn==1.2.2  
scipy==1.12.0  
sqlparse==0.4.4  
threadpoolctl==3.4.0  
typing_extensions==4.10.0  
tzdata==2024.1  

NOTE: Make sure your Anacond has sckit-learn==1.2.2 (To see this, open anaconda prompt then pip list to see the list of packages)

# Quick Way To Run project
Open CMD/cterminal then clone the repository, 

then create Python virtual environment 
# python -m venv venv 
then change directory to system 
# cd system 
then activate virtual environment 
# ./venv/scripts/activate
after that install project dependecies
# pip install -r requirements.txt
make migration 
# python manage.py makemigrations 
# python manage.py migrate 
then start the Django server
# python manage.py runserver 

To login as patient (username: patient and password=patient)  
To login as doctor (username: doctor and password=doctor)  
