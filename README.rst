Doorman
=======
.. image:: https://pypip.in/v/doorman/badge.png
   :target: https://pypi.python.org/pypi/doorman
.. image:: https://pypip.in/d/doorman/badge.png
   :target: https://crate.io/packages/doorman/
.. image:: https://api.travis-ci.org/halitalptekin/doorman.png
    :target: https://travis-ci.org/halitalptekin/doorman
.. image:: https://pypip.in/license/doorman/badge.png
    :target: https://pypi.python.org/pypi/doorman/   

Doorman keeps your secret things but main purpose of this tool, the convenience of the people working on the same file does not store passwords.

Install
-------
.. code-block:: python

    pip install doorman
    
Usage
-----

Firstly, you should create a config file(~/.doormanrc.yml) or put in text like below lines:

.. code-block::
    
    # social accounts
    /home/user/twitter.rb:
     twitter_passowrd: bHc0yz
     private_key: 1VpzKbLDTqC1vXb
    /home/user/pythoncodes/githubapi.py
     github_password: wKJ4cV

    # secret text
    /etc/secret.conf:
     my_secret: really secret thing

    # secret function
    ../settings/my_settings.py:
     my_func: [i for i in others if i < 3]

Hide all secret things;

.. code-block:: 

    doorman -s
    
.. code-block::     

    ... my twitter password is {{ twitter_password }} ...
    ... i keep {{ my_secret }} from other ...

Un-hide all secret things;

.. code-block:: 

    doorman -u
    
.. code-block::     

    ... my twitter password is bHc0yz ...
    ... i keep really secret thing from other ...

Help for usage;

.. code-block::

    doorman -h

.. code-block::

    usage: doorman [-h] [-s] [-u] [-c CONFIG_FILE]

    Doorman keeps your secret things

    optional arguments:
      -h, --help            show this help message and exit
      -s, --secret          Hide all secret things
      -u, --unsecret        Open all secret things
      -c CONFIG_FILE, --config CONFIG_FILE
                            Config file


TODO
----

Command line: need to fix logically bug

File open and replace: need to completely re-write
