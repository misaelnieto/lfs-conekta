from setuptools import setup, find_packages
import os

version = '1.0'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(
    name='lfs-conekta',
    version=version,
    description='Conekta Payment processor for LFS',
    long_description=README,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django e-commerce online-shop payment processor',
    author='Noe Nieto',
    author_email='nnieto@noenieto.com',
    license='MIT',
    url='http://github.com/tzicatl/lfs-conekta',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      'django-settings'
    ],
)
