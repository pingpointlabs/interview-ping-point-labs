# Technical Interview Exercise

## Overview

Welcome! This exercise simulates a real problem we solve at PingPoint Labs: extracting structured data from construction PDF documents.

**Your task:** Extract the door schedule from a construction drawing set into a structured format (CSV, JSON, or pandas DataFrame).

**Time allocation:** 90 minutes during our live session

**What we're evaluating:**
- Problem-solving approach
- Code organization and clarity
- How you handle messy, real-world documents
- Communication of your thought process

This isn't about perfection—we want to see how you approach the problem.

---

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Installation

1. **Clone this repository**
   ```bash
   git clone <repo-url>
   cd technical-interview
   ```

2. **Install uv (if you don't have it)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create virtual environment and install dependencies**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install .
   ```

### Verify Installation

Run this to confirm everything is working:
```bash
python verify_setup.py
```

You should see: ✅ All dependencies installed successfully

---

## Project Structure

```
technical-interview/
├── README.md                 # This file
├── pyproject.toml           # Python dependencies and project config
├── verify_setup.py          # Setup verification script
├── solution.py              # Your solution goes here (starter code provided)
└── output/                  # Place your extracted data here
```

---

## The Challenge

### Input
- A URL to a real construction drawing set containing a door schedule (will be provided at the start of the interview)

### Output
Extract the door schedule into a structured format with at least these fields:
- Door Mark (e.g., "101", "102A")
- Door Size (e.g., "3-0 x 7-0")
- Door Material/Type (e.g., "HM", "Wood")
- Fire Rating (if applicable)
- Hardware Set (e.g., "HS-1", "HS-2")

**Acceptable output formats:**
- CSV file in `output/door_schedule.csv`
- JSON file in `output/door_schedule.json`
- Pandas DataFrame saved as CSV or JSON

### What "Good" Looks Like

We're not looking for 100% accuracy—construction PDFs are messy by nature. We care about:

1. **Structured approach:** Breaking the problem into logical steps
2. **Code quality:** Clean, readable code with reasonable organization
3. **Error handling:** Gracefully handling issues (missing data, formatting problems)
4. **Validation thinking:** How do you know your extraction is working?
5. **Documentation:** Brief comments explaining non-obvious logic

---

## Available Tools & Libraries

You have `pymupdf` already installed, but feel free to use any additional libraries:

**PDF Processing:**
- `pymupdf` (PyMuPDF) - Already installed
- `pdfplumber` - If you prefer this approach
- `pytesseract` - For OCR if needed

**AI/LLM Integration (optional):**
- OpenAI API (we can provide a key)
- Anthropic Claude API (we can provide a key)
- Any other AI tools you're comfortable with

**Data Processing:**
- `pandas` - Already installed
- `numpy` - Already installed
- Any other standard data processing libraries

**To install additional packages:**
```bash
uv pip install <package-name>
```

---

## Getting Started

1. **Get the PDF URL**
   - At the start of our interview, I'll share a URL to the construction PDF
   - You can download it or work with it directly via URL
   
2. **Explore the PDF first**
   - Open the PDF and scan through it
   - Locate the door schedule (hint: look for tables with door marks)
   - Note any formatting challenges

3. **Start with `solution.py`**
   - We've provided starter code with a basic structure
   - Fill in the extraction logic
   - Test incrementally as you go

4. **Test your output**
   - Make sure your structured data is readable
   - Verify a few entries manually against the PDF

---

## Tips

- **Start simple:** Get something working, then refine
- **Test early and often:** Don't write 100 lines before running
- **Ask questions:** During our session, ask if anything is unclear
- **Document your thinking:** Brief comments help us understand your approach
- **It's okay to be imperfect:** Real construction PDFs are messy—handle what you can

---

## During the Interview

We'll work through this together via screen share. Feel free to:
- Use any resources (documentation, Stack Overflow, etc.)
- Ask clarifying questions about requirements
- Explain your thought process as you go
- Pivot your approach if something isn't working

---

## Questions Before We Meet?

Feel free to reach out if you have any setup issues or questions about the exercise.