=======
Doorman
=======

Doorman keeps your secret things

Usage
-----

Firstly, you should create a config file and put in text like below lines:

    [secrets]
    # social accounts
    twitter_password = 12345678
    github_password = 12345678

    # secret text
    my_secret = really secret thing

    # secret function
    my_func = [i for i in others if i < 3]

    # files
    [files]
    twitter_password = /home/user/twitter.rb
    github_password = /home/user/pythoncodes/githubapi.py
    my_secret = /etc/secret.conf
    myfunc = /home/user/my.py
