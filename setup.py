import setuptools


def lines(text):
    """
    Returns each non-blank line in text enclosed in a list.
    See http://pypi.python.org/pypi/textdata for more sophisticated version.
    """
    return [l.strip() for l in text.strip().splitlines() if l.strip()]

setuptools.setup(name='paylike',
      version='0.1',
      description='Python wrapper for paylike.io\'s REST API',
      url='https://github.com/hungrydk/paylike-python-sdk',
      author='Sune Kjaergaard',
      author_email='sune@hungry.dk',
      license='MIT License',
      install_requires=['requests'],
      packages=setuptools.find_packages(),
      zip_safe=False,
      classifiers=lines("""
              Development Status :: 5 - Production/Stable
              Operating System :: OS Independent
              License :: OSI Approved :: MIT License
              Intended Audience :: Developers
              Programming Language :: Python :: 2.7
              Programming Language :: Python :: 3
              Programming Language :: Python :: 3.2
              Programming Language :: Python :: 3.3
              Programming Language :: Python :: 3.4
              Programming Language :: Python :: 3.5
              Programming Language :: Python :: 3.6
              Programming Language :: Python :: 3.7
              Programming Language :: Python :: Implementation :: CPython
              Programming Language :: Python :: Implementation :: PyPy
              Topic :: Software Development :: Libraries :: Python Modules
          """)
      )