'''
setup.py for zapextcbv project
'''
import os
from setuptools import setup

def read(fname):
    '''
        Utility function to read README file
    '''
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="zapextcbv",
    version="0.0.1",
    author = "Aleksandr Aibulatov",
    author_email = "zap.aibulatov@gmail.com",
    description = "Extended classbased views",
    license = "BSD",
    keywords = "django views classbased extension",
    classifires = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]
)
