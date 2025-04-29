import os
import shutil

source_path = os.path.join(os.path.dirname(__file__), "trades_live.db")
target_path = "/mnt/data/trades.db"

shutil.copyfile(source_path, target_path)
print("✅ Force copied trades_live.db → /mnt/data/trades.db")

