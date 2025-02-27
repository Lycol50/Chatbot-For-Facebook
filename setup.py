from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Facebook Chatbot',
    version='1.2.0',

    description='A simple chatbot for Facebook personal profile.',
    long_description=long_description,


    url='https://github.com/the-javapocalypse/Chatbot-For-Facebook',


    author='Muhammad Ali Zia',
    author_email='muhammad.17ali@gmail.com',


    classifiers=[

        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],


    keywords='python chatbot facebook apiai fbchat',


    install_requires=['fbchat'],

   
)
