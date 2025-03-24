#IMPORTING THE LIBRARIES

import ollama
import requests
from bs4 import BeautifulSoup
import random
import datetime

# Research Agent: Finds Trending HR Topics
# Have not used search engine APIs, but used web scraping to fetch trending HR topics from various websites.
# The function fetch_trending_hr_topics() fetches trending HR topics from three different websites: HR Exchange Network, HR Dive, and SHRM.

def fetch_trending_hr_topics():
    """Fetches trending HR topics from the web."""
    urls = [
        "https://www.hrexchangenetwork.com/hr-tech",
        "https://www.hrdive.com/topic/hr-technology-analytics/",
        "https://www.shrm.org/in/topics-tools/news"
    ]
    
    topics = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = soup.find_all("h2")[:5]  # Get top 5 headlines
            
            for headline in headlines:
                topics.append(headline.get_text(strip=True))
        except Exception:
            continue

# This return line ensures that the function returns a valid list of topics even if no topics are found dynamically.

    return topics if topics else ["Employee Engagement Strategies", "Remote Work Challenges", "HR Tech Trends"]

# Content Planning Agent: Generates Blog Outline
# The function generate_outline(topic) generates a structured blog outline using Mistral and ensures the current year is used.
# The outline is generated based on the topic provided as input.

CURRENT_YEAR = datetime.datetime.now().year  # Get current year dynamically

def generate_outline(topic):
    """Generates a structured blog outline using Mistral and ensures the current year is used."""
    prompt = f"Create an outline for a 2000-word blog on '{topic}' in {CURRENT_YEAR}. Ensure the content is up-to-date and reflects current trends."
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Content Generation Agent: Writes the Blog
# The function generate_blog_content(outline) generates a detailed blog post ensuring it's for the current year.

def generate_blog_content(outline):
    """Generates a detailed blog post ensuring it's for the current year."""
    prompt = f"Write a detailed SEO-optimized blog post for {CURRENT_YEAR} based on this outline:\n{outline}. Ensure the trends and insights are relevant to {CURRENT_YEAR}."
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# SEO Optimization Agent: Enhances SEO Aspects
# The function optimize_for_seo(content) improves SEO by suggesting keywords and readability improvements.
# It uses the Mistral model to optimize the content for SEO.

def optimize_for_seo(content):
    """Improves SEO by suggesting keywords and readability improvements."""
    prompt = f"Optimize the following blog for SEO with relevant keywords, meta descriptions, and better readability:\n{content}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Review Agent: Proofreads and Enhances Readability
# The function proofread_content(content) proofreads and enhances the readability of the blog post.

def proofread_content(content):
    """Proofreads and enhances readability of the blog."""
    prompt = f"Proofread this blog for grammar, clarity, and readability. Keep the structure intact:\n{content}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Main Function: Executes the Multi-Agent Workflow
# The main() function orchestrates the entire workflow by calling the respective functions in sequence.
# It fetches trending HR topics, generates a blog outline, writes the blog content, optimizes for SEO, and proofreads the final content.
# The final blog post is then saved as a Markdown file.

def main():
    print("🔍 Fetching trending HR topics...")
    trending_topics = fetch_trending_hr_topics()
    
    selected_topic = random.choice(trending_topics)
    print(f"✅ Selected Topic: {selected_topic}")

    print("\n📝 Generating Blog Outline...")
    outline = generate_outline(selected_topic)
    print("\n[OUTLINE GENERATED]")

    print("\n✍️ Generating Blog Content...")
    blog_content = generate_blog_content(outline)
    print("\n[BLOG CONTENT GENERATED]")

    print("\n📈 Optimizing for SEO...")
    seo_content = optimize_for_seo(blog_content)
    print("\n[SEO OPTIMIZATION DONE]")

    print("\n🔍 Proofreading Content...")
    final_content = proofread_content(seo_content)
    print("\n[FINAL CONTENT READY]")

    # Save the blog post
    with open("final_blog_post_1.md", "w", encoding="utf-8") as file:
        file.write(final_content)

    print("\n✅ Blog Post Generated Successfully! Saved as 'final_blog_post_1.md'")

if __name__ == "__main__":
    main()