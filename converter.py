import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def convert_html_to_epub(html_file, epub_file):
    # Create a new EPUB book
    book = epub.EpubBook()

    # Set the book's metadata
    book.set_title('title')
    book.add_author('none')
    book.set_language('zh-TW')
    book.add_item(epub.EpubNcx())



    # Open the HTML file and parse its content
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Create a new EPUB section
    chapter = epub.EpubHtml(title='Chapter 2', file_name='chapter_1.xhtml', lang='en')
    chapter.content = str(soup)

    # Add the section to the book
    book.add_item(chapter)

    book.spine = [chapter]
    # Set the book's table of contents
    book.toc = [chapter]

    # Create the EPUB file
    epub.write_epub(epub_file, book, {})

# Usage
convert_html_to_epub('test.html', 'book.epub')
