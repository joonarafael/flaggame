echo "EXPECTED test RUNTIME: 38 s."
python3 ./backups/take.py

coverage run --branch -m pytest src
coverage html

python3 ./backups/restore.py