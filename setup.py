#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-sms',
    version='0.0.0',
    description="A django-otp plugin that delivers tokens via a Custom SMS service.",
    author="Victor Miti",
    author_email='victormiti@gmail.com',
    url='https://github.com/engineervix/django-otp-sms',
    project_urls={
        "Documentation": 'https://django-otp-sms.readthedocs.io/',
        "Source": 'https://github.com/engineervix/django-otp-sms',
    },
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'django-otp >= 1.0.0',
        'requests',
    ],
)
