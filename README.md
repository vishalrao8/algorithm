# Algorithms in Python

A clean, modular Python repository implementing classic data structures and algorithms with clear code, complexity analysis, and examples.

---

## 📌 Features & Algorithms

### Sorting Algorithms
| Algorithm | Best Time | Average Time | Worst Time | Space | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ Implemented |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | 🚧 Work in progress |

---

## 📁 Project Structure

```text
algorithm/
├── src/
│   └── algorithm/
│       ├── __init__.py               # Package entry point
│       └── algorithms/
│           ├── selection_sort.py     # Selection sort implementation
│           └── bubble_sort.py        # Bubble sort implementation
├── pyproject.toml                    # Project configuration & dependencies
├── README.md                         # Documentation
└── .python-version                   # Python version
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (or [uv](https://docs.astral.sh/uv/))

### Installation

Clone the repository:

```bash
git clone git@github.com:vishalrao8/algorithm.git
cd algorithm
```

#### Using `uv` (Recommended)

```bash
# Run directly
uv run python -m algorithm
```

#### Using standard Python & Virtual Environment

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in editable mode
pip install -e .
```

---

## 💻 Usage

### Running as a Module

```bash
python3 -m algorithm
```

### Importing into Your Code

```python
from algorithm.algorithms.selection_sort import selection_sort

data = [64, 25, 12, 22, 11]
sorted_data = selection_sort(data)
print("Sorted array:", sorted_data)
# Output: [11, 12, 22, 25, 64]
```

---

## 🤝 Contributing

Contributions are welcome! If you would like to implement a new algorithm or improve existing ones:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/insertion-sort`)
3. Commit your changes (`git commit -m "Add insertion sort"`)
4. Push to the branch (`git push origin feature/insertion-sort`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
