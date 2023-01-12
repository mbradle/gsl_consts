.. _installation:

Installing gslconsts 
====================

First ensure that you have `pip <https://pip.pypa.io/en/stable/>`_
installed on your system by typing (at the command line prompt $)::

      $ pip --help

If this command does not return a proper usage statement,
install pip according to the instructions at the
pip `website <https://pip.pypa.io/en/stable/>`_.  Note that with python
version 3, you may have `pip3` instead of `pip`.

With pip installed, you may now use it to install gslconsts by typing::

      $ pip install gslconsts

If the installation fails, you may need to install with root privileges using
`sudo`::

      $ sudo pip install gslconsts

Alternatively, you can just install for yourself with the ``--user`` option::

      $ pip install gslconsts --user

If you have previously installed gslconsts and want to upgrade, type::

      $ pip install --upgrade gslconsts

To test that gslconsts has installed correctly, type::

      $ pip show gslconsts

which should return information about the package.  To check that the
package is in place, open python by typing::

      $ python

or, perhaps for version 3::

      $ python3

and try importing gslconsts by typing at the python prompt:

     >>> import gslconsts

This command should simply return.  Of course, to exit python,
type::

     >>> exit()
