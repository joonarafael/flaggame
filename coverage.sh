echo "EXPECTED test RUNTIME: 38 s."
python3 ./backups/take.py

python3 -m coverage run --branch -m pytest src
python3 -m coverage html

python3 ./backups/restore.py