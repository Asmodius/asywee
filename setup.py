#!/usr/bin/env python3

from setuptools import setup  #, find_packages

from asywee import version


setup(
    name='asywee',
    version=version,
    author='Asmodius',
    author_email='asmodius.a@gmail.com',
    description="Asywee is asynchronous ORM framework based on peewee",
    long_description=open('README.md').read(),
    keywords='peewee asyncio postgres asywee',
    license='New BSD License',
    url='https://github.com/Asmodius/asywee',
    download_url='https://github.com/Asmodius/asywee/archive/master.zip',
    # packages=find_packages(),
    packages=[
        'asywee',
        'asywee/db',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    zip_safe=False,
    setup_requires=open("requirements.txt").read().split("\n"),
    install_requires=open("requirements.txt").read().split("\n"),
)

#     install_requires=[
#         'aiopg==0.9.2',
#         'cached-property==1.3.0',
#         'peewee==2.8.0',
#         'tasklocals==0.2',
#     ],
# )
