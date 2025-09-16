# News Summarizer

An AI-powered tool that generates concise summaries from long news articles.  
Built using Natural Language Processing (NLP) techniques to save time and help users stay updated quickly.

## Features
- Summarises long news articles into short, meaningful text  
- Accepts input as raw text or article URLs  
- Uses modern NLP models for extractive/abstractive summarisation  
- Lightweight and easy to run locally  

## Tech Stack
- **Python**  
- **NLP Libraries**: NLTK, spaCy, Hugging Face Transformers  
- **Frameworks**: Flask / Streamlit (for UI)  

## Getting Started

```bash
# Clone the repository
git clone https://github.com/bosukorampara/News_Summarizer.git
cd News_Summarizer

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
