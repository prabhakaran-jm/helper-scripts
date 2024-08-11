import os
import re
from ebooklib import epub

# Specify the directory containing the epub files
epub_directory = 'path/to/epub/directory'

def extract_text_from_epub(epub_path):
    try:
        book = epub.read_epub(epub_path)
        title = book.get_metadata('DC', 'title')
        author = book.get_metadata('DC', 'creator')
        if title and author:
            return f"{title[0][0]} by {author[0][0]}"
        elif title:
            return title[0][0]
    except Exception as e:
        print(f"Error extracting metadata from {epub_path}: {str(e)}")
    return os.path.basename(epub_path)

def generate_new_filename(text):
    # Remove special characters and spaces
    clean_text = re.sub(r'[^a-zA-Z0-9]', '_', text)
    # Limit the filename length
    return clean_text[:50] + '.epub'

def rename_epub_files(directory):
    # Iterate through all epub files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.epub'):
            file_path = os.path.join(directory, filename)
            try:
                # Extract text from the epub (metadata)
                extracted_text = extract_text_from_epub(file_path)
                
                # Generate new filename
                new_filename = generate_new_filename(extracted_text)
                
                # Rename the file
                new_file_path = os.path.join(directory, new_filename)
                os.rename(file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_filename}')
            except Exception as e:
                print(f"Skipping {filename} due to error: {str(e)}")

    print("Renaming process completed.")

if __name__ == '__main__':
    rename_epub_files(epub_directory)