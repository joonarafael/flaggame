echo "EXPECTED test RUNTIME: 38 s."
python3 ./backups/take.py

pytest src
python3 ./backups/restore.py