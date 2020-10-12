set -x
cd ..
python3 -m pip freeze >requirements.txt
cd -
make clean
make html
