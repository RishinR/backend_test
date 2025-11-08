# FastAPI Performance Testing Project

A FastAPI-based backend project that demonstrates and compares different approaches to making concurrent HTTP requests: asynchronous, multi-threaded, and blocking/synchronous methods.

## 📋 Project Overview

This project includes a simple FastAPI server and three different client implementations to benchmark the performance of various request handling strategies when making 24,999 HTTP requests.

## 🚀 Features

- **FastAPI Server** (`main.py`): A lightweight REST API with two endpoints
- **Async Client** (`test_async.py`): Uses `aiohttp` and `asyncio` for non-blocking concurrent requests
- **Threaded Client** (`test_thread.py`): Uses `ThreadPoolExecutor` for concurrent requests with threading
- **Blocking Client** (`test_blocking.py`): Traditional synchronous approach using `requests`

## 📊 Performance Comparison

Based on the benchmark results in the code:

| Method | Time Taken | Performance |
|--------|-----------|-------------|
| **Async (aiohttp)** | ~3.6s | ⭐⭐⭐ Fastest |
| **Threading** | ~7.8s | ⭐⭐ Moderate |
| **Blocking** | ~11.1s | ⭐ Slowest |

The async approach is approximately **3x faster** than blocking and **2x faster** than threading for high-volume requests.

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

1. Clone or download the project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### 1. Start the FastAPI Server

First, start the server in one terminal:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

### 2. Run Performance Tests

In separate terminals, run any of the test scripts:

#### Async Test (Fastest)
```bash
python test_async.py
```

#### Threading Test
```bash
python test_thread.py
```

#### Blocking Test (Slowest)
```bash
python test_blocking.py
```

## 🔌 API Endpoints

### `GET /`
Returns a random 5-character lowercase string.

**Response:**
```json
{
  "data": "abcde"
}
```

### `GET /items/{item_id}`
Returns the provided item ID.

**Parameters:**
- `item_id` (int): The ID of the item

**Response:**
```json
{
  "item_id": 123
}
```

## 📁 Project Structure

```
backend_test/
├── main.py              # FastAPI server with API endpoints
├── test_async.py        # Async client using aiohttp
├── test_thread.py       # Multi-threaded client using ThreadPoolExecutor
├── test_blocking.py     # Synchronous blocking client
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## 📦 Dependencies

- **fastapi**: Modern web framework for building APIs
- **uvicorn**: ASGI server for FastAPI
- **aiohttp**: Async HTTP client/server framework
- **requests**: HTTP library for synchronous requests
- **pydantic**: Data validation using Python type annotations

## 🔍 How Each Test Works

### Async Test (`test_async.py`)
- Uses `aiohttp` for async HTTP requests
- Creates tasks for all URLs using `asyncio.create_task()`
- Executes all tasks concurrently with `asyncio.gather()`
- Non-blocking I/O allows handling thousands of requests efficiently

### Threading Test (`test_thread.py`)
- Uses `requests` with `ThreadPoolExecutor`
- Creates multiple threads to handle requests in parallel
- Each thread makes blocking requests but runs concurrently with others
- Good balance between simplicity and performance

### Blocking Test (`test_blocking.py`)
- Traditional synchronous approach using `requests`
- Makes requests one at a time in a loop
- Simple but slowest for high-volume requests
- Useful baseline for comparison

## 💡 Key Takeaways

1. **Async is King**: For I/O-bound operations like HTTP requests, async/await provides the best performance
2. **Threading is Practical**: ThreadPoolExecutor offers a good middle ground with simpler code than async
3. **Context Matters**: For a small number of requests, the overhead differences are negligible
4. **Session Reuse**: All methods use session objects to reuse connections, improving performance

## 🧪 Customizing Tests

To modify the number of requests, change the `urls` range in any test file:

```python
urls = range(1, 25000)  # Change 25000 to your desired number
```

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for learning and benchmarking purposes.

## ⚠️ Notes

- The performance results may vary based on your system specifications and network conditions
- For production use, consider implementing proper error handling and rate limiting
- Large numbers of concurrent requests may overwhelm the server; adjust accordingly
