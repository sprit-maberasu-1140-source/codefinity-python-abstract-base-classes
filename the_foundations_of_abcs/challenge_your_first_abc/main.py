from abc import ABC, abstractmethod

# Defining the abstract base class
class BaseReport(ABC):
    @abstractmethod
    def generate(self, data):
        pass

    @abstractmethod
    def get_format(self):
        pass

# Concrete CSV report implementation
class CsvReport(BaseReport):
    def generate(self, data):
        headers = ",".join(data[0].keys())
        values = ",".join(str(value) for value in data[0].values())
        return f"{headers}\n{values}"

    def get_format(self):
        return "CSV"

csv_report = CsvReport()

report_format = csv_report.get_format()
report_output = csv_report.generate([{"id": "R-001", "amount": "4500.0", "status": "approved"}])

print(report_format)
print(report_output)