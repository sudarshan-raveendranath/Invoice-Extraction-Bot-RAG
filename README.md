# Invoice Extraction Bot with Gemini and LangChain

![LangChain](https://img.shields.io/badge/LangChain-FF6A00?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-FFD700?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

A Streamlit application that extracts structured information from invoice PDFs using Google's Gemini model and LangChain framework.

## Features

- Extracts text from uploaded PDF invoices
- Creates vector embeddings using HuggingFace sentence transformers
- Performs semantic search using FAISS vector store
- Extracts key invoice fields into structured JSON format
- User-friendly web interface with Streamlit

## Extracted Fields

- Invoice number
- Description of items
- Quantity
- Date
- Unit price
- Amount
- Total amount
- Email address
- Phone number
- Physical address

## Tech Stack

- **Language Model**: Google Gemini 1.5 Pro
- **Framework**: LangChain
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2
- **PDF Processing**: PyPDFLoader
- **Web Interface**: Streamlit
- **Environment Management**: python-dotenv

## Prerequisites

- Python 3.8+
- Google API key (for Gemini access)
- Git (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/invoice-extraction-bot.git
cd invoice-extraction-bot
```
2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install required packages:
```bash
pip install -r requirements.txt
```
4. Set up your Google API key:
   - Create a `.env` file in the root directory and add your API key:
```bash
GOOGLE_API_KEY=your_google_api_key
```
5. Run the Streamlit app:
```bash
streamlit run app.py
```
6. Open your web browser and go to `http://localhost:8501` to access the app.

## Usage
1. Run the Streamlit app using the command above.
2. Upload a PDF invoice file.
3. Click the "Extract Invoice" button.
4. View the extracted information displayed in a structured format.

## Configuration Options
- embedding_model: HuggingFace model for embeddings (default: sentence-transformers/all-MiniLM-L6-v2)
- vector_store: The FAISS index used for semantic search.
- Language model: The Google Gemini model used for text generation and extraction.
- Prompt Template: Template for the extraction prompt (customizable in invoiceUtil.py)

## Limitations
- The app currently supports only English language invoices.
- Works best with digitally created PDFs (may have issues with scanned documents)
- Extraction accuracy depends on the invoice format and layout
- Google Gemini API usage may incur costs based on your usage
- Requires internet connection for model access

## Future Enhancements
- Support for multiple languages
- Integration with cloud storage (e.g., Google Drive, Dropbox)
- Improved error handling and user feedback
- Support for more complex invoice formats
- Customizable field extraction templates
- Local model support

