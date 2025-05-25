# asset.py
class Asset:
    def __init__(self, name, category, value, beneficiary, note):
        self.name = name
        self.category = category  # Digital, Bank, Property, etc.
        self.value = value
        self.beneficiary = beneficiary
        self.note = note

    def __str__(self):
        return (
            f"Asset Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Value: {self.value}\n"
            f"Beneficiary: {self.beneficiary}\n"
            f"Note: {self.note}\n"
        )
