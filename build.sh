# Script to automate build for PyPI.

rm -fr dist
python gslconsts/make_consts.py /opt/local/include/gsl > gslconsts/consts.py
python gslconsts/make_math.py /opt/local/include/gsl > gslconsts/math.py
black gslconsts/*.py
python -m pip install --upgrade build
python -m build
