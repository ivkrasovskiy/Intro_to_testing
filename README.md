Testing encode: 

python -m doctest -v issue-01.py 
python -m doctest -v -o NORMALIZE_WHITESPACE issue-01.py

Testing decode: python -m doctest -v issue-02.py

Testing unittest: python issue-03.py

Testing pytest: python -m pytest issue-04.py

Testing pytest issue-05:

coverage run -m unittest discover
coverage report -m