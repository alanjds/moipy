#!/usr/bin/env python

from distutils.core import setup

setup(name='Moipy',
      version='0.2.1',
      description='Python integration with MoIP payment gateway via API',
      author=['Herberth Amaral','Ale Borba','Victor', 'Alan Justino'],
      author_email=['herberthamaral@gmail.com','ale.alvesborba@gmail.com','vitalbh@gmail.com', 'alan.justino@yahoo.com.br'],
      url='https://github.com/alanjds/moipy/',
      packages=['moipy'],
      install_requires=[
          'lxml',
          'pycurl',
      ],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOSX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',  
      ])
