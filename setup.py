from setuptools import setup
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme:
    README = readme.read()

setup(
    name = 'django-wechat-menu',
    version = '0.0.1',
    description = 'add menu',
    long_description = README,

    url = 'https://github.com/ChanMo/django-wechat-menu/',

    author = 'ChanMo',
    author_email = 'chen.orange@aliyun.com',

    license = 'BSD License',

    keywords = 'wechat django weixin menu',

    packages = ['wechat_menu'],
    include_package_data = True,

    install_requires = ['django-wechat-base'],
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
