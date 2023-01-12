.. _use:

Use the package
===============

The `GNU Scientific Library <https://www.gnu.org/software/gsl/>`_
(GSL) is a numerical library for C and C++ programmers.  Included in the library
are a number of
`physical constants <https://www.gnu.org/software/gsl/doc/html/const.html>`_.
The current package makes those
constants directly available to python users.

To use the constants, first open python and import the package:

    >>> from gslconsts.consts import *

Now use the constants, as defined by GSL, directly.  For example, you may
type:

    >>> print(GSL_CONST_MKSA_SPEED_OF_LIGHT)

The result is the GSL-defined value for the speed of light in vacuum in
`MKSA <https://en.wikipedia.org/wiki/MKS_system_of_units>`_ units.
The constants are :obj:`float` types, as can be seen by typing:

    >>> print(type(GSL_CONST_MKS_SPEED_OF_LIGHT))

and thus can be used directly in calculations.  For example, type:

    >>> r_mars_au = 1.52
    >>> r_mars_meters = r_mars_au * GSL_CONST_MKSA_ASTRONOMICAL_UNIT
    >>> print("The distance from the Sun to Mars is {:.2e} meters".format(r_mars_meters))
    >>> mars_light_travel_time_hours = r_mars_meters / GSL_CONST_MKSA_SPEED_OF_LIGHT / GSL_CONST_MKSA_HOUR
    >>> print("The light travel time from the Sun to Mars is {:.2f} hours".format(mars_light_travel_time_hours))

Constants in
`CGSM <https://en.wikipedia.org/wiki/Centimetre–gram–second_system_of_units>`_
units
are also available: just replace the *MKSA* with *CGSM*.  For example, type:

   >>> print(GSL_CONST_CGSM_SPEED_OF_LIGHT)

