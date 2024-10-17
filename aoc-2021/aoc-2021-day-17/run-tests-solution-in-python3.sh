# Remove existing sym. linked shared libraries
rm solution-in-python3/helpers

# Sym. link shared libraries (if not already)
ln -s ../../../shared/shared_python3/helpers ./solution-in-python3/

pytest -v
