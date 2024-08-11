import fitz

def remove_pages(input_pdf, output_pdf, pages_to_remove):
    # Open the PDF file
    doc = fitz.open(input_pdf)
    
    # Create a list of all pages
    total_pages = len(doc)
    pages_to_keep = [i for i in range(total_pages) if i not in pages_to_remove]
    
    # Select only the pages we want to keep
    doc.select(pages_to_keep)
    
    # Save the modified PDF
    doc.save(output_pdf)
    doc.close()
    
    print(f"Successfully removed specified pages. New PDF saved as {output_pdf}")

def main():
    # Usage
    input_pdf = "path/to/input.pdf"
    output_pdf = "path/to/output.pdf"
    
    # Example: Specify the exact pages to remove (e.g., pages 4 and 5)
    pages_to_remove = [7, 8, 9, 10, 11]  # Zero-based index
    
    remove_pages(input_pdf, output_pdf, pages_to_remove)

if __name__ == "__main__":
    main()