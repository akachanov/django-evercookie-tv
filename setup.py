from setuptools import setup, find_packages

setup(
     name='django_evercookie',
     version='0.1',
     install_requires = [
          'Django>=1.5',
          'Pillow >= 2.0.0',
          'django-dont-vary-on==0.1.1',
     ],
     packages = find_packages(),
     include_package_data = True, 
     author = 'Alexey Haidamaka',
     author_email = 'ahaidamaka@gmail.com',
     description = 'Evercookie for Django',
     license = 'MIT License', 
     keywords = 'django evercookie',
     url='https://github.com/gdmka/django_evercookie',
     )

