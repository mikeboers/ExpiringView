
from distutils.core import setup

setup(
    name='ExpiringView',
    version='0.2',
    description='Mapping class which gives key/value pairs an expiry time.',
    url='http://github.com/mikeboers/ExpiringView',
    py_modules=['expiringview'],
    
    author='Mike Boers',
    author_email='expiringview@mikeboers.com',
    license='BSD-3',
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
