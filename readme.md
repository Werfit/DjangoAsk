# Installation

Firstly, install all python dependencies:
<pre>pip install -r requirements.txt</pre>

If you are lucky, everything you need is to make migrations and to run a server:
<pre>python manage.py makemigrations</pre>
<pre>python manage.py migrate</pre>
<pre>python manage.py runserver</pre>

If you are not, then you should follow the installation guide of [WeasyPrint](https://weasyprint.readthedocs.io/en/latest/install.html) and [CropperJS](https://github.com/fengyuanchen/cropperjs/blob/master/README.md). Then you can get to making migrations and running your server.