import os
from setuptools import setup
 
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
 
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='reusable-blog-app',
    version='1.0.0',
    packages=['reusable_blog'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to create blogs',
    long_description=README,
    url='https://github.com/Eventyret',
    author='Simen Daehlin',
    author_email='simen@dehlin.info',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'Pillow',
        'django_forms_bootstrap',
        'django-disqus',
    ],
)