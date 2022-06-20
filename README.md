# django-garage-management-system
#### garage management system using django framework and ajax

Good implementation of `QR` and `weasyprint` using django rest framework and ajax - at the request of one of the Iraqi brothers from the `Django programmers facebook group`.

you have to install `gobject-2.0-0` library from [here for windows](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) or follow the [instructions](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)

## install (win)
```bash
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```