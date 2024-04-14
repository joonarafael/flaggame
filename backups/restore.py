import shutil

logs_dir = "src/logs"
empty_dir = "src/logs/empty"
backup_dir = "src/logs/backup"

try:
    shutil.copy(f"{backup_dir}/history_backup.txt", f"{logs_dir}/history.txt")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/history_empty.txt", f"{logs_dir}/history.txt")

try:
    shutil.copy(f"{backup_dir}/rounds_backup.csv", f"{logs_dir}/rounds.csv")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/rounds_empty.csv", f"{logs_dir}/rounds.csv")

try:
    shutil.copy(f"{backup_dir}/stats_backup.csv", f"{logs_dir}/stats.csv")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/stats_empty.csv", f"{logs_dir}/stats.csv")

try:
    shutil.copy(f"{backup_dir}/streaks_backup.csv", f"{logs_dir}/streaks.csv")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/streaks_empty.csv", f"{logs_dir}/streaks.csv")