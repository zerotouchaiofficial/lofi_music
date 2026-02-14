# Contributing Guidelines

Thank you for your interest in contributing! 🎉  
We welcome bug fixes, improvements, new features, and documentation updates.

---

## 📌 Getting Started

### 1. Fork & Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If there is a development requirements file:

```bash
pip install -r requirements-dev.txt
```

---

## 🌿 Branching

Create a new branch for every change:

```bash
git checkout -b feature/short-description
```

Branch naming examples:

- `feature/add-api-endpoint`
- `fix/validation-error`
- `refactor/cleanup-logic`
- `docs/update-readme`

---

## 🐛 Reporting Issues

Before opening a new issue:

- Check existing issues to avoid duplicates.
- Clearly describe the problem.
- Include steps to reproduce.
- Provide error messages and logs if available.
- Mention your Python version.

Example:

```bash
python --version
```

---

## 🛠 Development Guidelines

### Code Style

- Follow PEP 8 style guidelines.
- Use meaningful variable and function names.
- Keep functions small and focused.
- Avoid unnecessary comments.
- Write docstrings for public functions and classes.

### Formatting (if using Black)

```bash
black .
```

### Linting (if using Flake8)

```bash
flake8 .
```

---

## 🧪 Testing

- Add tests for new features.
- Ensure all tests pass before submitting a PR.

Run tests:

```bash
pytest
```

If using unittest:

```bash
python -m unittest
```

---

## ✍️ Commit Message Guidelines

Use clear, descriptive commit messages.

Format:

```
type: short description
```

Examples:

- `feat: add user authentication`
- `fix: handle empty input error`
- `refactor: simplify data processing`
- `docs: update installation guide`
- `test: add tests for utils module`

Keep commits small and focused.

---

## 🔁 Pull Request Process

1. Push your branch:

```bash
git push origin feature/short-description
```

2. Open a Pull Request against the `main` branch.
3. Clearly describe what your PR does.
4. Ensure:
   - Code runs without errors
   - Tests pass
   - No linting issues

---

## 📚 Documentation

Improvements to documentation are always welcome:

- Fix typos
- Improve explanations
- Add usage examples
- Improve docstrings

---

## 🏷 Versioning

This project follows Semantic Versioning:

- MAJOR — breaking changes
- MINOR — new features
- PATCH — bug fixes

---

## 🙌 Thank You

We appreciate your time and effort in making this project better!

Happy coding! 🚀
