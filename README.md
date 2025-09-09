# FastAPI Query Parameters Demo

A FastAPI application demonstrating basic query parameters for filtering, pagination, and optional request modifications.

---

## 🚀 Features

- **FastAPI framework** with automatic OpenAPI documentation
- Demonstrates **query parameters** with default values
- Implements **pagination** using `skip` and `limit` parameters
- Shows **optional vs required** query parameters
- Interactive API documentation at [`/docs`](http://127.0.0.1:8000/docs) and [`/redoc`](http://127.0.0.1:8000/redoc)
- Python 3.7+ compatibility
- Virtual environment setup

---

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/fastapi-query-parameters-demo.git
   cd fastapi-query-parameters-demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Dependencies

The project uses the following main dependencies:

- **fastapi** — The web framework for building APIs
- **uvicorn** — ASGI server for running FastAPI applications

To generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 🚀 Running the Application

Start the development server:
```bash
uvicorn main:app --reload --reload-exclude venv
```

Access the application:

- **API:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative docs:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints

### `GET /items/`

Returns a paginated list of items with optional `skip` and `limit` parameters.

**Query Parameters:**

- `skip` (int, optional): Number of items to skip (default: 0)
- `limit` (int, optional): Maximum number of items to return (default: 10)

#### Examples:

```bash
# Default parameters
curl "http://127.0.0.1:8000/items/"

# Skip first item, return next 2
curl "http://127.0.0.1:8000/items/?skip=1&limit=2"

# Skip first 2 items, return next 5
curl "http://127.0.0.1:8000/items/?skip=2&limit=5"
```

#### Sample Responses:

```json
// Default response
[
  {"item_name": "Foo"},
  {"item_name": "Bar"},
  {"item_name": "Baz"}
]

// With skip=1, limit=2
[
  {"item_name": "Bar"},
  {"item_name": "Baz"}
]
```

---

## 🎯 Key Concept: Query Parameters

- **What are Query Parameters?**
  - Key-value pairs that appear after `?` in a URL
  - Format: `?key1=value1&key2=value2`
  - Used for optional filtering, sorting, pagination
  - Not part of the path—they come after the path

- **How FastAPI Handles Them:**
  - Any function parameter not in the path becomes a query parameter
  - Default values make parameters optional
  - No default value = required query parameter
  - Type hints provide validation and documentation

---

## 🧪 Testing the API

Test different query parameter combinations:

- **Default parameters:**
  ```bash
  curl "http://127.0.0.1:8000/items/"
  ```
- **Custom pagination:**
  ```bash
  curl "http://127.0.0.1:8000/items/?skip=1"
  curl "http://127.0.0.1:8000/items/?limit=2"
  curl "http://127.0.0.1:8000/items/?skip=1&limit=2"
  ```
- **Interactive testing:**  
  Use the Swagger UI at `/docs` to test with different parameters.

---

## 📁 Project Structure

```
fastapi-query-parameters-demo/
├── main.py          # Main application file
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── venv/            # Virtual environment (gitignored)
```

---

## 🔧 Code Explanation

### `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

# Sample data
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    Fetch a list of items with pagination.
    - skip: number of items to skip (for pagination)
    - limit: max number of items to return
    """
    return fake_items_db[skip : skip + limit]
```

**Key Points:**
- `skip: int = 0` → Optional parameter with default value 0
- `limit: int = 10` → Optional parameter with default value 10
- Parameters not in path → Automatically become query parameters
- Type hints (`int`) → Validation and OpenAPI documentation

---

## 🎓 Learning Points

- **Query Parameters:** Use for optional request modifications
- **Default Values:** Make parameters optional with `= default_value`
- **Type Validation:** FastAPI validates types automatically
- **Pagination:** Common use case for query parameters
- **Automatic Docs:** FastAPI documents all parameters automatically

---

## 🔧 Troubleshooting

**Common Issues:**

- **Type validation errors**  
  Ensure correct parameter types (e.g., `skip=1` not `skip=one`)

- **Parameter ordering**  
  Query parameter order doesn't matter in URLs

- **Missing parameters**  
  Parameters with defaults are optional; without defaults are required

- **Reload issues**  
  ```bash
  uvicorn main:app --reload --reload-exclude venv
  ```

---

## 📚 Learning Resources

- [FastAPI Query Parameters Documentation](https://fastapi.tiangolo.com/tutorial/query-params/)
- [FastAPI Optional Parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

---

## 🤝 Contributing

1. **Fork the project**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- Uvicorn team for the ASGI server
- Python community for ongoing support
