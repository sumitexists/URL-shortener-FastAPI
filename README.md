# 🔗 URL Shortener — FastAPI

A simple URL shortener REST API built with FastAPI and SQLModel. This is my first project while transitioning from Django REST Framework to FastAPI — built to get hands-on with core FastAPI concepts like Pydantic models, path parameters, redirects, and SQLModel integration.

---

## 🚀 Features

- Shorten any long URL into a compact short code
- Redirect to the original URL via the short code
- Persistent storage with SQLite via SQLModel
- Auto-generated interactive API docs at `/docs`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database ORM | SQLModel |
| Database | SQLite |
| Server | Uvicorn |
| Language | Python 3.10+ |


## ⚙️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/sumitexists/URL-shortener-FastAPI
cd URL-shortener-FastAPI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
fastapi dev
```

Server runs at `http://127.0.0.1:8000`

---

## 📌 API Endpoints

### `POST /url`
Accepts a long URL and returns a shortened version.

**Request body:**
```json
{
  "url_data": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

**Response:**
```json
{
  "shortend_url": "http://127.0.0.1:8000/abc123"
}
```

---

### `GET /{short_code}`
Redirects to the original URL associated with the short code.

```
GET /abc123  →  307 Redirect  →  https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

---

## 📖 API Docs

FastAPI generates interactive docs automatically:

| Type | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

## 🧠 What I Learned

Coming from Django REST Framework, here's what this project taught me about FastAPI:

- **Pydantic models** replace DRF serializers — type hints handle validation automatically
- **SQLModel** bridges Pydantic and SQLAlchemy cleanly — one model for both DB and schema
- **`RedirectResponse`** handles HTTP 307 redirects natively with one line
- **Auto docs** at `/docs` are always in sync with your code — no extra setup needed
- **Less boilerplate** — the same API takes significantly fewer lines than DRF


## 🗺️ Roadmap

- [ ] Custom aliases (e.g. `yoursite.com/my-link`)
- [ ] Click/visit tracking per short URL
- [ ] Expiry dates on short URLs
- [ ] Simple frontend UI

---

## 👨‍💻 Author

Built as part of my Django → FastAPI transition series.
Following along? Check out my [LinkedIn](https://www.linkedin.com/in/sumitsinghdevlife) for project updates.
