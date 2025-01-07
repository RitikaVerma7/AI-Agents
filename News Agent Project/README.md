# Mood Sensitive Newsbot

## Overview
Mood Sensitive Newsbot is a personalized NLP-driven project designed to provide users with a stress-free way to stay updated on current events. By tailoring news content based on the user's mood and preferences, the Newsbot ensures a more positive and relevant news experience.

## Features
### Current Implementation:
1. **Natural Input:**
   - Understands user preferences and emotional state.
2. **Live News Feed:**
   - Fetches the top 100 articles from a curated database.
   - Filters content based on user input for mood and relevancy.
3. **Intelligent Filters:**
   - Removes negative news based on user mood.
   - Returns up to 40 relevant and positive articles.
4. **Output Options:**
   - Full summaries and automated email delivery.
   
---

## Technology Stack
- **Backend:** Mistral, Chat, DSPy, Prompt Engineering.
- **Frontend:** Streamlit (To be improved in future versions).
- **NLP Models:** DistilBERT for Sentiment Analysis, MiniLM for embeddings.
- **Search and Similarity:** FAISS-based similarity search (384 dimensions).

---

## How It Works
1. Fetches and processes the top 100 news articles as of the previous day.
2. Filters and embeds articles based on user preferences and relevancy.
3. Returns curated results, filtered for positivity or full content based on mood.

---

## Thank You
Get the news that fits you!
