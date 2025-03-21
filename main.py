import google.generativeai as genai
import requests
import markdown
import os
from agents import ResearchAgent, ContentPlanningAgent
from utils import save_to_file


genai.configure(api_key="AIzaSyCZHYrh0b2YHIRFyujSpckmDea2afO9Ybs")

def research_trending_topics():
    """Finds trending HR topics (Placeholder: Replace with a real API like Google Trends or News API)"""
    return "Latest HR Trends in 2025"

def generate_outline(topic):
    """Generates a structured blog outline."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"""Create a detailed outline for a blog post on '{topic}'. 
    Include introduction, key sections, and conclusion."""
    response = model.generate_content([prompt])
    return response.text.strip() if response.text else "No response received"

def generate_blog(outline):
    """Writes the blog post based on the outline."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"Write an engaging, SEO-optimized blog post based on this outline:\n{outline}"
    response = model.generate_content([prompt])
    return response.text.strip() if response.text else "No response received"

def optimize_seo(blog_content):
    """Optimizes the blog post for SEO (basic keyword density improvements)."""
    # Placeholder for real SEO optimization (e.g., keyword analysis, readability check)
    return blog_content.replace("HR", "Human Resources")  # Example optimization

def proofread_content(blog_content):
    """Reviews and enhances blog content."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"Proofread and improve the quality of the following content:\n{blog_content}"
    response = model.generate_content([prompt])
    return response.text.strip() if response.text else blog_content

def save_to_files(topic, blog_content):
    """Saves blog content in Markdown, HTML, and TXT formats."""
    safe_topic = topic.replace(" ", "_").lower()
    os.makedirs("output", exist_ok=True)
    
    with open(f"output/{safe_topic}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(blog_content)
    
    with open(f"output/{safe_topic}.md", "w", encoding="utf-8") as md_file:
        md_file.write(f"# {topic}\n\n" + blog_content)
    
    html_content = markdown.markdown(blog_content)
    with open(f"output/{safe_topic}.html", "w", encoding="utf-8") as html_file:
        html_file.write(f"<h1>{topic}</h1>" + html_content)

if __name__ == "__main__":
    chosen_topic = research_trending_topics()
    outline = generate_outline(chosen_topic)
    print("\n🔹 Blog Outline Generated:\n", outline)
    
    blog_content = generate_blog(outline)
    blog_content = optimize_seo(blog_content)
    blog_content = proofread_content(blog_content)
    print("\n🔹 Full Blog Post:\n", blog_content)
    
    save_to_files(chosen_topic, blog_content)
    print("\n✅ Blog saved in output/ folder as TXT, Markdown, and HTML!")
