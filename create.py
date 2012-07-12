#!/usr/bin/python

import mechanize


def create_account(wiki_login_url, username, email, realname, reason='',
                   password=None, extra_parameters=None, b=None):
    '''Create an account on a MediaWiki wiki. The parameters are:

    * username: Username on the wiki
    * password: Password on the wiki (optional; if None, uses "By e-mail")
    * email: Email address of new user
    * realname: "Real name" of user that will be created
    * reason: (optional) The reason of account creation

    These parameters are currently passed to
    https://labsconsole.wikimedia.org/wiki/Special:UserLogin/signup .

    * extra_parameters: (optional) a dictionary that corresponds to the
                        name attribute on extra <input> elements in the
                        login form

    * b: (optional) a mechanize.Browser instance (essential if you have
                    some cookies stored that you want to re-use.)
    '''
    # FIXME: Support optional API created by Extension:SignupAPI
    # FIXME: Support password
    fp = b.open(wiki_login_url)
    response = fp.read()

    # Make sure we are logged-in
    assert 'Your user page' in response

    b.select_form(name='userlogin2')
    b['wpName'] = username
    b['wpEmail'] = email
    b['wpRealName'] = realname
    b['wpReason'] = reason
    

