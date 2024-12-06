ln -s ../../../shared/shared_python3/helpers ./solution-in-python3/

# pytest -v # Full output 
# pytest -v

# Avoid pytest running older python versions (that do not recognise match case syntax, enum etc.)
python3 -m pytest -v
