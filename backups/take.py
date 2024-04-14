import shutil

logs_dir = "src/logs"
empty_dir = "src/logs/empty"
backup_dir = "src/logs/backup"

try:
    shutil.copy(f"{logs_dir}/history.txt", f"{backup_dir}/history_backup.txt")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/history_empty.txt", f"{backup_dir}/history_backup.txt")

try:
    shutil.copy(f"{logs_dir}/rounds.csv", f"{backup_dir}/rounds_backup.csv")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/rounds_empty.csv", f"{backup_dir}/rounds_backup.csv")

try:
    shutil.copy(f"{logs_dir}/stats.csv", f"{backup_dir}/stats_backup.csv")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/stats_empty.csv", f"{backup_dir}/stats_backup.csv")

try:
    shutil.copy(f"{logs_dir}/streaks.csv", f"{backup_dir}/streaks_backup.csv")

except FileNotFoundError:
    shutil.copy(f"{empty_dir}/streaks_empty.csv", f"{backup_dir}/streaks_backup.csv")