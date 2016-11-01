##http://peterdowns.com/posts/first-time-with-pypi.html
	#$python setup.py register -r pypitest
	#$python setup.py sdist upload -r pypitest
	#$python setup.py register -r pypi
	#$python setup.py sdist upload -r pypi
	#$python setup.py register -r pypitest && python setup.py sdist upload -r pypitest && python setup.py register -r pypi && python setup.py sdist upload -r pypi && pip install captcha2 --upgrade
##https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/

from setuptools import setup, find_packages

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = ["requests >= 2.11.1"]

from distutils.core import setup

if __name__ == "__main__":
    setup(
      name = 'captcha2',
      packages = ['captcha2'], # this must be the same as the name above
      version = '0.0.1',
      description = 'An upload to 2captcha.com library',
      author = 'Nikola Dang',
      author_email = 'ducthinhdt@gmail.com',
      url = 'https://github.com/nikoladang/2captcha', # use the URL to the github repo
      download_url = 'https://github.com/nikoladang/2captcha/tarball/0.1', # I'll explain this in a second
      keywords = ['2captcha', 'captcha', 'uploading', 'automation', 'resolving', 'automate'], # arbitrary keywords
      classifiers = CLASSIFIERS,
      install_requires=INSTALL_REQUIRES,
    )
