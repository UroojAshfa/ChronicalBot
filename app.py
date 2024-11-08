
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import wikipedia
import torch
from sentence_transformers import SentenceTransformer, util

# Load models for embeddings and classification
model_name = "bert-base-uncased"  # Model for classifying question types
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Model for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Efficient for embeddings and similarity tasks

# Configure Wikipedia library
wikipedia.set_lang("en")
wikipedia.set_rate_limiting(True)
wikipedia.headers = {'User-Agent': 'HistoricalEventsExplorer/1.0 (uroojashfaq@hotmail.com)'}

# Function to classify question type (event, person, period, etc.)
def classify_question(query):
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class = torch.argmax(logits, dim=-1).item()
    categories = ['Person', 'Event', 'Period']
    return categories[predicted_class]  # Return the predicted category as the query type

# Enhanced Wikipedia search with embedding-based similarity ranking
def search_wikipedia(query, detailed=False):
    try:
        # Search Wikipedia for titles matching the query
        search_results = wikipedia.search(query)
        if not search_results:
            return "No results found on Wikipedia for your query."

        # Generate embeddings for the query
        query_embedding = embedding_model.encode(query, convert_to_tensor=True)

        # Retrieve summaries for top search results and rank by similarity
        summaries = []
        for title in search_results[:5]:  # Limit to top 5 results for efficiency
            try:
                summary_text = wikipedia.summary(title, sentences=5)
                title_embedding = embedding_model.encode(summary_text, convert_to_tensor=True)
                similarity = util.pytorch_cos_sim(query_embedding, title_embedding).item()
                summaries.append((title, summary_text, similarity))
            except wikipedia.exceptions.DisambiguationError:
                continue  # Skip ambiguous titles
            except wikipedia.exceptions.PageError:
                continue  # Skip missing pages

        # Sort summaries by similarity
        summaries = sorted(summaries, key=lambda x: x[2], reverse=True)
        best_summary = summaries[0][1] if summaries else "No suitable summary found."

        # Optionally fetch a more detailed summary
        if detailed:
            best_title = summaries[0][0] if summaries else None
            if best_title:
                best_summary = wikipedia.summary(best_title, sentences=20)

        return best_summary

    except wikipedia.exceptions.DisambiguationError:
        return "There are multiple results for that query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for the given query."
    except Exception as e:
        return f"An error occurred: {e}"

# Function for managing session context (multi-turn conversation)
def get_context():
    if "context" not in st.session_state:
        st.session_state.context = []
    return st.session_state.context

def update_context(query, answer):
    context = get_context()
    context.append({"query": query, "answer": answer})

# Streamlit Interface
def main():
    st.set_page_config(
    page_title="ChronicleBot",  
    page_icon="logo.webp",  
)

    st.markdown("<h1 style='color:#006400;'>ChronicleBot</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333333;'>From significant events to notable figures, dive into history by asking about events, people, or periods, and uncover the stories that shaped our world!</p>", unsafe_allow_html=True)
    # Retrieve and update session context
    context = get_context()

    # Display previous conversation context (if any)
    if context:
        st.write("### Previous Queries:")
        for turn in context:
            st.write(f"**Q:** {turn['query']}")
            st.write(f"**A:** {turn['answer']}")

    # Text input for user query
    st.markdown('<p style="font-size: 16px; color: #333333;">Ask me about the who(s), why(s), and what(s) of history:</p>', unsafe_allow_html=True)
    query = st.text_input ("") 

    if query:
        detailed = "detailed" in query.lower() or "more" in query.lower()
        
        # Classify the query type (Event, Person, Period, etc.)
        query_type = classify_question(query)
       
        
        # Enhanced Wikipedia search with embeddings
        response = search_wikipedia(query, detailed=detailed)

        # Display the response and update context
        st.write(response)
        update_context(query, response)

if __name__ == "__main__":
    main()


