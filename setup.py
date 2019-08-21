from setuptools import setup, find_packages

setup(
    name='passfort_demo',
    version='1.0.0',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)
