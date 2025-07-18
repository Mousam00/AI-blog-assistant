# 🧠 AI Blog Assistant

A lightweight, GenAI-powered backend built with **FastAPI** and **Cohere API** that generates intelligent blog content based on user-provided topics. Includes **duplicate detection**, **MongoDB-based storage**, and clean, scalable architecture. Ideal for showcasing backend, GenAI, and cloud-ready development skills.

---

## 🚀 Features

- ✅ Generate unique blog posts using **Cohere's GenAI API**
- 🔍 Prevents duplicate blog generation with topic-based caching via **MongoDB**
- 📦 Built with **FastAPI**, using clean routes and modular architecture
- 🛢️ Persistent storage with **MongoDB Atlas**
- 🐳 Ready to be containerized and deployed with **Docker**
- 🧪 Easy to extend with endpoints for search, pagination, or classification

---

## 🧱 Tech Stack

- **Backend**: FastAPI, Pydantic  
- **GenAI**: Cohere API (Command model)  
- **Database**: MongoDB Atlas  
- **Environment**: Python 3.11 
- **Tools**: Uvicorn, Python-dotenv

---

## 📦 API Endpoints

### `POST /generate-blog`

**Description**: Generates a new blog post for a given topic (or returns existing one if already generated).

**Request Body**:
```json
{
  "topic": "How AI is changing education"
}
