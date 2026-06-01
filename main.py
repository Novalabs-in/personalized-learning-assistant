import os
from openai import OpenAI

class LearningAssistant:
    """
    Personalized AI Study Guide & Flashcard Generator
    Intelligently chunks textbooks and formats cards/quizzes.
    """
    def __init__(self, api_key=None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def generate_study_deck(self, text_snippet):
        prompt = f"""
        Extract the core concepts from the text and generate a flashcard study deck.
        Text: {text_snippet}
        
        Format as a JSON array of dicts containing "question" and "answer" fields.
        """
        print("--- Querying Learning Model ---")
        # Under a real setup, we would execute self.client.chat.completions.create(...)
        # Returning mock JSON for offline running:
        mock_deck = [
            {"question": "What is Superposition?", "answer": "The ability of a quantum state to exist in multiple states simultaneously."},
            {"question": "What is Entanglement?", "answer": "A physical phenomenon where particles remain correlated across distances."}
        ]
        return mock_deck

if __name__ == "__main__":
    assistant = LearningAssistant(api_key="mock")
    deck = assistant.generate_study_deck("Quantum mechanics study guide...")
    for i, card in enumerate(deck, 1):
        print(f"Card #{i} | Q: {card['question']} | A: {card['answer']}")
