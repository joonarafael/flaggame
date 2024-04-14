echo "Initializing program environment and installing dependencies..."
sudo apt-get update
sudo apt-get install python3.6 python3-pip
sudo apt-get install python3-tk
pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 -m pip install pytest coverage pylint autopep8 2to3
chmod u+x ./run.sh ./test.sh ./pylint.sh ./coverage.sh