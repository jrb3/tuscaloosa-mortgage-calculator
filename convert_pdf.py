from docling.document_converter import DocumentConverter
import csv

# Initialize converter
converter = DocumentConverter()

# Convert the PDF
pdf_path = '/home/jrbarrow3/Docling Conversions/CHECKINGSTATEMENT_06-23-2025.pdf'
print("Converting PDF...")
result = converter.convert(pdf_path)

# Get all text content
all_text = result.document.export_to_text()
print(f'Document converted successfully!')
print(f'Total text length: {len(all_text)} characters')

# Save as CSV
output_path = '/home/jrbarrow3/Git/CHECKINGSTATEMENT_06-23-2025.csv'
with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['content'])
    writer.writerow([all_text])

print(f'CSV file saved to: {output_path}')

# Also extract tables if any
tables = []
for element in result.document.body.elements:
    if hasattr(element, 'label') and element.label == 'table':
        table_data = element.text
        tables.append(table_data)

if tables:
    print(f'Found {len(tables)} tables')
    # Save tables separately
    table_output_path = '/home/jrbarrow3/Git/CHECKINGSTATEMENT_06-23-2025_tables.csv'
    with open(table_output_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['table_number', 'table_content'])
        for i, table in enumerate(tables):
            writer.writerow([i+1, table])
    print(f'Tables saved to: {table_output_path}')
else:
    print('No tables found in the document')