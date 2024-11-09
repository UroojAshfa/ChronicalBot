## 📜 ChronicleBot: A Conversational AI for Historical Exploration

ChronicleBot is an interactive history chatbot that brings the past to life by answering user queries about historical events, figures, and periods. Designed as a semantic search tool, it allows users to ask detailed questions and receive contextually rich responses drawn directly from Wikipedia, delivering historical insights right at your fingertips.

## 🚀 Features
🗣️ Intelligent Historical Chat:

* Contextual Q&A: Users can ask questions about historical events, people, or periods, and ChronicleBot provides relevant and fact-based summaries, making history easily accessible.

* Accurate Classification: Powered by transformer models, ChronicleBot classifies queries into types like events, people, or periods, enhancing the relevance of responses.

* Conversational Flow: Maintains conversational context by showing previous queries and responses, creating a smooth, interactive experience.

🧠 Embedding-Based Semantic Search:

* Enhanced Relevance Matching: Utilizing Sentence Transformers and vector embeddings, the bot performs similarity matching to improve response relevance, delivering more insightful answers.

* Summary Filtering: Ranks and filters Wikipedia results based on semantic similarity to the query, ensuring that responses align with user intent.

🌐 Wikipedia Integration:

* Wide Knowledge Base: Leverages the Wikipedia API to fetch real-time data, allowing access to a vast repository of historical information across various topics.

* Dynamic Query Handling: Supports follow-up queries and questions that rely on context, enabling deeper exploration within a single session.

## 🔧 Technologies Used

* Streamlit: Drives the user interface with an interactive and user-friendly design.

* Transformers (Hugging Face): Employs Transformer models for semantic search and classification to enhance response accuracy.

* Sentence Transformers: Generates vector embeddings to enable similarity matching between user queries and Wikipedia content.

* Wikipedia API: Primary data source for fetching summarized historical information.

* PyTorch: Framework used to run classification models, ensuring accurate identification of query types.

## 💡 Limitations
While ChronicleBot currently provides robust functionality, there are a few areas in which it's still under development:

* Source Limitations: At present, Wikipedia serves as the only data source. The integration of other reputable historical sources (e.g., British Library, Smithsonian) is planned to enhance the diversity of responses.

* Advanced User Interactions: Features such as follow-up question prompts and suggested queries for deeper exploration are in the works, aiming to make the interaction feel more natural and engaging.

* Visual Enhancements: An interactive timeline for viewing events chronologically is planned, which will allow users to filter and explore historical events visually.

* Reliability of Semantic Search: While semantic similarity ranking is in place, fine-tuning is ongoing to further improve result relevance and accuracy.

These limitations are actively being worked on to make ChronicleBot even more engaging and informative.

## 🔜 Future Enhancements

* API Integrations with Historical Libraries: Enriching data sources by adding APIs from the British Library, Smithsonian, Library of Congress, etc.

* Fact-Checking Capabilities: Adding APIs from sources like DBpedia or Wikidata to verify and cross-reference information, improving the accuracy and reliability of responses.

* Enhanced Follow-Up Prompts: Developing a guided follow-up question feature to encourage users to delve deeper into related historical events or figures.

* Interactive Timeline: Implementing a timeline view that allows users to see events chronologically, making history exploration both informative and visually engaging.

## ⚙️ Installaion

To set up ChronicleBot locally, follow these steps:

   1. Clone this repository:
```bash
git clone https://github.com/yourusername/ChronicleBot.git
cd ChronicleBot
```
   2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. Explore:
 Open the local server URL and start exploring history!

## 📝 Usage

1. Enter your query: Ask questions like "Who was Winston Churchill?" or "What caused the Industrial Revolution?"

2. Receive detailed responses: ChronicleBot searches W ikipedia, ranks results by relevance, and provides a summary tailored to your query.

3. Explore follow-ups: Use the conversational flow to explore related queries and responses in a seamless format.


## 🤝 Contributing

ChronicleBot is an evolving project, and contributions are always welcome! If you have ideas for new features or enhancements, feel free to open an issue or submit a pull request.




