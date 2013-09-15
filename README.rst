Doorman
=======

Doorman keeps your secret things

Install
-------
.. code-block:: python

    pip install doorman
    
Usage
-----

Firstly, you should create a config file(~/.doormanrc) and put in text like below lines:

.. code-block::

    # social accounts
    twitter_password >> 12345678 >> /home/user/twitter.rb
    github_password >> 12345678 >> /home/user/pythoncodes/githubapi.py

    # secret text
    my_secret >> really secret thing >> /etc/secret.conf

    # secret function
    my_func >> [i for i in others if i < 3] >> /home/user/my.py

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

    ... my twitter password is 12345678 ...
    ... i keep really secret thing from other ...

TODO
----

Config Parse: need to find an elegant solution

Command line: need to fix logically bug

File open and replace: need to completely re-write

Add More exception handler

