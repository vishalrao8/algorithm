# Algorithms in Python

> [!NOTE]
> **Authorship & AI Contribution Disclosure**  
> All algorithm implementations in this repository are **handwritten by the author** to build a deep, intuitive grasp over core algorithms, data structures, and foundational problem-solving techniques. AI assistance was used exclusively for generating and formatting this documentation (`README.md`).

A clean, modular Python repository implementing classic data structures and algorithms with clear code, complexity analysis, and examples.

---

## 📌 Features & Algorithms

### 1. Sorting Algorithms (`sort/`)
| Algorithm | Best Time | Average Time | Worst Time | Space | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ Implemented |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ Implemented |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | 🚧 Work in progress |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | 🚧 Work in progress |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | 🚧 Work in progress |

### 2. Searching Algorithms (`search/`)
| Algorithm | Best Time | Average Time | Worst Time | Space | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Binary Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | 🚧 Work in progress |
| **Quick Select** | $O(n)$ | $O(n)$ | $O(n^2)$ | $O(1)$ | 🚧 Work in progress |

### 3. Recursion (`recursion/`)
- 🚧 Planned

---

## 📁 Project Structure

```text
algorithm/
├── src/
│   ├── __init__.py
│   └── algorithm/
│       ├── sort/
│       │   ├── bubble_sort.py
│       │   ├── insertion_sort.py
│       │   ├── merge_sort.py
│       │   ├── quick_sort.py
│       │   └── selection_sort.py
│       ├── search/
│       │   ├── binary_search.py
│       │   └── quick_select.py
│       └── recursion/
├── pyproject.toml
├── README.md
└── .python-version
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

### Importing into Your Code

```python
from algorithm.sort.selection_sort import selection_sort
from algorithm.sort.bubble_sort import bubble_sort

data = [64, 25, 12, 22, 11]

# Selection Sort
sorted_selection = selection_sort(data.copy())
print("Selection Sort:", sorted_selection)

# Bubble Sort
sorted_bubble = bubble_sort(data.copy())
print("Bubble Sort:", sorted_bubble)
```

---

## 🤝 Contributing

Contributions are welcome! If you would like to implement a new algorithm or improve existing ones:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/merge-sort`)
3. Commit your changes (`git commit -m "Add merge sort"`)
4. Push to the branch (`git push origin feature/merge-sort`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

