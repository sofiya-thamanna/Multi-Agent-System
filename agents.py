import google.generativeai as genai

class ResearchAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")

    def get_trending_topics(self):
        prompt = "Find trending HR topics for 2025."
        response = self.model.generate_content([prompt])
        return response.text.strip() if response.text else "No topics found"

class ContentPlanningAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")

    def generate_outline(self, topic):
        prompt = f"Create a detailed blog outline for '{topic}'."
        response = self.model.generate_content([prompt])
        return response.text.strip() if response.text else "No outline generated"
