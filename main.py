import fitz  # PyMuPDF for PDF files
from ebooklib import epub
from difflib import SequenceMatcher
import time
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView

# Helper function for similarity
def calculate_accuracy(original, typed):
    return SequenceMatcher(None, original, typed).ratio() * 100

# Function to extract text from a PDF file
def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.splitlines()

# Function to extract text from an EPUB file
def extract_epub_text(epub_path):
    book = epub.read_epub(epub_path)
    text = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text.append(item.get_body_content().decode('utf-8'))
    return "".join(text).splitlines()

# Function to download a PDF from a URL
def download_pdf(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return save_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
        return None

class RetypingApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Enter a URL or select a PDF/EPUB file:")
        self.layout.add_widget(self.label)

        self.file_chooser = FileChooserIconView()
        self.layout.add_widget(self.file_chooser)

        self.start_button = Button(text="Start Typing Practice")
        self.start_button.bind(on_press=self.start_typing_practice)
        self.layout.add_widget(self.start_button)

        self.result_label = Label()
        self.layout.add_widget(self.result_label)

        return self.layout

    def start_typing_practice(self, instance):
        selected = self.file_chooser.selection
        if not selected:
            url = self.file_chooser.path
            file_path = download_pdf(url, "downloaded_file.pdf") if url.startswith("http") else None
        else:
            file_path = selected[0]

        if file_path:
            file_type = "pdf" if file_path.lower().endswith(".pdf") else "epub" if file_path.lower().endswith(".epub") else None
            if file_type:
                lines = extract_pdf_text(file_path) if file_type == "pdf" else extract_epub_text(file_path)
                self.typing_practice(lines)
            else:
                self.result_label.text = "Unsupported file type."
        else:
            self.result_label.text = "No file provided."

    def typing_practice(self, lines):
        for line in lines:
            if not line.strip():
                continue
            
            self.result_label.text = f"Type this: {line}"
            typed = input("Your input: ")
            if typed.lower() == "exit":
                break
            
            accuracy = calculate_accuracy(line, typed)
            self.result_label.text = f"Accuracy: {accuracy:.2f}%"

if __name__ == "__main__":
    RetypingApp().run()
