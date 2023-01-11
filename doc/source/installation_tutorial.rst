.. _installation:

Installing gsl_consts 
=====================

First ensure that you have `pip <https://pip.pypa.io/en/stable/>`_
installed on your system by typing (at the command line prompt $)::

      $ pip --help

If this command does not return a proper usage statement,
install pip according to the instructions at the
pip `website <https://pip.pypa.io/en/stable/>`_.  Note that with python
version 3, you may have `pip3` instead of `pip`.

With pip installed, you may now use it to install gsl_consts by typing::

      $ pip install gsl_consts

If the installation fails, you may need to install with root privileges using
`sudo`::

      $ sudo pip install gsl_consts

Alternatively, you can just install for yourself with the ``--user`` option::

      $ pip install gsl_consts --user

If you have previously installed gsl_consts and want to upgrade, type::

      $ pip install --upgrade gsl_consts

To test that gsl_consts has installed correctly, type::

      $ pip show gsl_consts

which should return information about the package.  To check that the
package is in place, open python by typing::

      $ python

or, perhaps for version 3::

      $ python3

and try importing gsl_consts by typing at the python prompt:

     >>> import gsl_consts

This command should simply return.  Of course, to exit python,
type::

     >>> exit()
