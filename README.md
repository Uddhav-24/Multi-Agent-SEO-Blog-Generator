# Multi-Agent SEO Blog Generator

## Project Overview
This project is a **multi-agent system** that automatically generates SEO-optimized blog posts on trending HR topics.  

## System Architecture
The system consists of multiple agents:
1. **Research Agent**: Scrapes trending HR topics from multiple websites.
2. **Content Planning Agent**: Generates a structured outline for the blog.
3. **Content Generation Agent**: Writes the detailed blog content.
4. **SEO Optimization Agent**: Enhances the blog with SEO best practices.
5. **Review Agent**: Proofreads and improves readability.

## Tools and Frameworks Used
- **Python**
- **Ollama** (for LLM-based text generation using Mistral)
- **BeautifulSoup** (for web scraping)
- **Markdown Exporting** (for blog post storage)

## 🚀 Installation & Setup

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/Multi-Agent-SEO-Blog-Generator.git
cd Multi-Agent-SEO-Blog-Generator 
```

### **Step 2: Set Up the Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Pull the Required LLM Model**
```bash
ollama pull mistral
```

### **Step 5: Run the Script**
```bash
python multi_agent_seo_blog.py
```
