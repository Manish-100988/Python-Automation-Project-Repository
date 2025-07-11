# Define two classes with the same method (interface)
class PDFExporter:
    def export(self):  # Method to export to PDF
        print("Exporting to PDF")

class CSVExporter:
    def export(self):  # Method to export to CSV
        print("Exporting to CSV")

# Duck Typing in action:
# No need for inheritance or type checking
# As long as the object has the 'export' method, it works
def perform_export(exporter):
    # This function doesn't care about the type of 'exporter'
    # It just checks if it has an 'export' method
    exporter.export()  # This is where duck typing happens

# Using duck typing to achieve polymorphism
perform_export(PDFExporter())  # Output: Exporting to PDF
perform_export(CSVExporter())  # Output: Exporting to CSV
