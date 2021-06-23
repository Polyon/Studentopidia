# Studentopidia -> A website that hold student academic record.
# Creator -> Polyon Mondal

## How to setup a project in Django:-
* At first create you project by using following command in terminal:
> django-admin startproject `[ProjectName]`
* Then create a app by using following command:
> python manage.py startapp `[AppName]`
* Then run this following command to initialising your defualt datatable:
> python manage.py makemigrations
* After that push the initialized datatable to your default django database using following command:
> python manage.py migrate
* After doing above task you have to create a superuser for access your default database:
> python manage.py createsuperuser\
> * After running above command the following imformation you have to put:
>> Username (leave blank to use 'default'): [UserName]\
>> Email Address: [example@gmail.com]\
>> Password: [--------]\
>> Password (again): [--------]

## After successfully run above command your folder structure should be like this:
> `ProjectName`
>> `ProjectName`
>>> `__pycache__`\
>>> \__init.py__\
>>> asgy.py\
>>> settings.py\
>>> urls.py\
>>> wsgi.py\

>>`AppName`
>>> `__pycache__`\
>>> `migrations`\
>>> \__init.py__\
>>> admin.py\
>>> apps.py\
>>> models.py\
>>> tests.py\
>>> views.py\

>> manage.py\
>> db.sqlite3

* Now your project initialized done successfully.
** To check run the following command:
> python manage.py runserver\
** After successfully run your project ready to edit.
