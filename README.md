# 🔑 KeyValueStore API

A lightweight, token-authenticated Flask API for securely storing and retrieving key-value pairs. Ideal for internal tooling, testing environments, or lightweight configuration services.

---

## 🚀 Features

- ✅ Token-based authentication using Bearer tokens
- 🔒 CORS enabled for specific frontends (`localhost` & `razinco-procurement.web.app`)
- ⚡ Simple JSON-based interface for setting and retrieving key-value data
- 📦 In-memory store (no database required)
- 🌱 `.env` support for secure API token management

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/KeyValueStore.git
cd KeyValueStore
```

2. **Create a virtual environment & install dependencies:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. **Create a `.env` file with your API token:**

```env
API_TOKEN=your_secret_token_here
```

---

## 🛠️ API Usage

### Authentication

All endpoints require a Bearer token via the `Authorization` header:

```
Authorization: Bearer your_secret_token_here
```

---

### 🔐 `POST /api/set`

Store a key-value pair.

#### Request Body:

```json
{
  "key": "username",
  "value": "john_doe"
}
```

#### Response:

```json
{
  "message": "Key :username set successfully."
}
```

---

### 🔍 `POST /api/get`

Retrieve the value for a given key.

#### Request Body:

```json
{
  "key": "username"
}
```

#### Response:

```json
{
  "key": "username",
  "value": "john_doe"
}
```

---

## 🌐 CORS Support

This API allows cross-origin requests from:

- `http://localhost:4200`
- `Enter your host url`

---

## 🧪 Running Locally

```bash
python app.py
```

Server starts on `http://127.0.0.1:5000` in development mode.

---

## 📁 Example `.env`

```env
API_TOKEN=supersecrettoken123
```

---

## ⚠️ Notes

- All data is stored **in-memory** and will be lost on server restart.
- For persistent storage, consider integrating with a database or file system.
- Protect your `.env` file and never expose it in public repositories.

---

## 📃 License

MIT License
