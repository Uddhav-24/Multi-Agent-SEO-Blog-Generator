# Multi-Agent SEO Blog Generator

## Project Overview
This project is a **multi-agent system** that automatically generates SEO-optimized blog posts on trending HR topics.  

## System Architecture
The system consists of multiple agents working together:  
1. **Research Agent**: Scrapes trending HR topics from multiple websites.  
2. **Content Planning Agent**: Generates a structured outline for the blog.  
3. **Content Generation Agent**: Writes the detailed blog content.  
4. **SEO Optimization Agent**: Enhances the blog with SEO best practices.  
5. **Review Agent**: Proofreads and improves readability.  

## Agent Workflow  
1. **Fetching HR Topics**: The **Research Agent** scrapes trending HR-related topics from websites.  
2. **Generating Blog Outline**: The **Content Planning Agent** creates a structured outline for the selected topic.  
3. **Writing the Blog**: The **Content Generation Agent** generates detailed blog content.  
4. **SEO Optimization**: The **SEO Agent** improves keyword density, meta descriptions, and readability.  
5. **Final Proofreading**: The **Review Agent** ensures grammatical correctness and clarity.  
6. **Saving the Blog**: The final blog post is saved as **Markdown (`.md`), HTML, PDF, and TXT formats** in the project directory.  

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

📄 Output

The generated blog post will be saved as:

1. Markdown (.md)
2. HTML (.html)
3. PDF (.pdf)
4. TXT (.txt)

📌 Notes

1. Ensure Ollama is installed and running before executing the script.
2. The script fetches live HR topics, so results may vary.
3. If no topics are found, default HR topics are used.
