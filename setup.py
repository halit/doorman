try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = dict(description='Doorman keeps your secret things', author='Halit Alptekin',
              url='https://github.com/halitalptekin/doorman', author_email='info@halitalptekin.com', license='MIT',
              keywords='password,secret,parse,config,security, crypt', version='0.3.0', install_requires=['nose','pyYAML','appdirs'],
              packages=['doorman'], scripts=[], name='doorman', entry_points={
        'console_scripts': ['doorman = doorman.main:main', ]})

setup(**config)
