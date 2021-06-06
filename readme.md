# Installation

Firstly, install all python dependencies:
<pre>pip install -r requirements.txt</pre>

If you are lucky, everything you need is to make migrations and to run a server:
<pre>python manage.py makemigrations</pre>
<pre>python manage.py migrate</pre>
<pre>python manage.py runserver</pre>

If you are not, then you should follow the [WeasyPrint](https://weasyprint.readthedocs.io/en/latest/install.html) installation guide. Then you can get to making migrations and running your server.