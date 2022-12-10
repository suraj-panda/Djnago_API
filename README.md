# Djnago_API
Question 2: Create a Web API for scraping country data in JSON format.
Answer:
GitHub Link: 
Steps Followed:
Step 1: Created a virtual environment named “djangoApi”.
>> py -m venv djangoApi   #Venv Create
>> djangoApi\Scripts\activate.bat   #Venv Activated

Step 2: Install all the packages in virtual environment required using pip.
  1.	Django
  2.	BeautifulSoap4
  3.	Requests
  4.	Json
  5.	Djangorestframework

Step 3: Create a project named “RestApi”.
>> Django-admin startproject RestApi
>> cd RestApi

Step 4: Create an app named “API”.
>> Django-admin startapp API

Step 5: Verification of Project.
>> Python manage.py runserver

Step 6: Create the template folder and make necessary changes in settings.py file.

Step 7: Modify the urls.py and views.py to render the HTML file in template.

Step 8: Enter the country name in field of the HTML file and submit.

Step 9: Retrieve the data through scraping in views.py in dictionary format.

Step 10: Convert the dictionary into JSON format.
>> context = {}
>> context = {'flag_link': flag_link, 'capital':sample2, 'largest_city': largest_city, 'official_languages': official_languages, 'area_total': area_total, 'Population': Population, 'GDP_nominal': GDP_nominal}
>> json_object = json.dumps(context, indent = 4)

Step 11: Print the JSON output in CMD.

Step 12: Freeze the requirements of the project in virtual environment.

Step 13: Upload the project into GitHub Repository.
