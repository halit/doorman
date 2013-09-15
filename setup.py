try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Doorman keeps your secret things',
    'author': 'Halit Alptekin.com',
    'url': '',
    'author_email': 'info@halitalptekin.com',
    'version': '0.1.1',
    'install_requires': ['nose'],
    'packages': ['doorman'],
    'scripts': [],
    'name': 'doorman',
    'entry_points': {
        'console_scripts': [
            'doorman = doorman.main:main',
        ]
    }
}

setup(**config)
