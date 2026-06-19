# Importing Libraries
# Importing Google Text to Speech library
from gtts import gTTS

# Importing PDF reader PyPDF2
import PyPDF2

# Open file Path
pdf_File = open('functions.pdf', 'rb')

# Create PDF Reader Object
pdf_Reader = PyPDF2.PdfReader(pdf_File)
count = len(pdf_Reader.pages)  # counts number of pages in pdf
textList = []

# Extracting text data from each page of the pdf file
for i in range(count):
    try:
        page = pdf_Reader.pages[i]  # Use pages[page_number] instead of getPage(pageNumber)
        textList.append(page.extract_text())
    except Exception as e:
        print(f"Error extracting text from page {i + 1}: {e}")

# Print extracted text from each page
for i, text in enumerate(textList):
    print(f"Page {i + 1} text:\n{text}\n{'-' * 30}")

# Converting multiline text to single line text
textString = " ".join(textList)

# Print the combined text
print("Combined Text:\n", textString)

# Set language to English (en)
language = 'en'

# Call GTTS
if textString:
    myAudio = gTTS(text=textString, lang=language, slow=False)

    # Save as mp3 file
    myAudio.save("Audiof.mp3")
else:
    print("No text to speak. Check if the PDF extraction is successful.")
