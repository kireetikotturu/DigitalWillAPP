# will.py
import os
from asset import Asset

class Will:
    def __init__(self, username):
        self.username = username
        self.assets = []

    def add_asset(self, name, category, value, beneficiary, note):
        asset = Asset(name, category, value, beneficiary, note)
        self.assets.append(asset)

    def export_to_file(self):
        folder = f"data/wills"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"{self.username}_will.txt")
        
        with open(file_path, "w") as file:
            file.write(f"Digital Will for {self.username}\n")
            file.write("="*40 + "\n\n")
            for i, asset in enumerate(self.assets, 1):
                file.write(f"Asset #{i}\n")
                file.write(str(asset))
                file.write("-"*30 + "\n")
        return file_path
