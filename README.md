# AI-Powered Code Explainer

A Streamlit web app that uses OpenAI to explain code snippets in various styles.

---

## Features

- **Paste code** and get instant AI-generated explanations.
- **Choose explanation style:** Brief, Detailed, or Step-by-Step.
- **Modular codebase:** Easily extend with embeddings or other features.

---

## File Overview

- **`app.py`**  
  The Streamlit user interface. Lets you paste code, select explanation style, and view results.

- **`explainer.py`**  
  Handles communication with OpenAI’s API. Builds prompts based on user-selected style and returns the explanation.

- **`config.py`**  
  Stores your OpenAI API key.  
  **Example:**
  ```python
  OPENAI_API_KEY = "your-openai-api-key-here"
  ```

- **`embeddings.py`**  
  (Optional/Extendable)  
  For future use: add code to generate or use embeddings for advanced features like code similarity or search.

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-code-explainer.git
    cd ai-code-explainer
    ```

2. **Install dependencies:**
    ```bash
    pip install streamlit openai
    ```

3. **Add your OpenAI API key:**
    - Create a `config.py` file in the project root:
      ```python
      OPENAI_API_KEY = "your-openai-api-key-here"
      ```

4. **Run the app:**
    ```bash
    streamlit run app.py
    ```

---

## Usage

1. Paste your code into the text area.
2. Select the explanation style.
3. Click **Explain Code** to get your explanation.

---

## Example Screenshot

![screenshot](screenshot.png)

---

## Extending

- Add new explanation styles in `explainer.py`.
- Use `embeddings.py` for advanced features (e.g., code search, similarity).

---

## License

MIT

---

Made with ❤️ using Streamlit