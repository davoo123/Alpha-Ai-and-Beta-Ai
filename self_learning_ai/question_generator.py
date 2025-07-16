import re
import random

def generate_questions_from_text(text, num=3):
    """Generate intelligent follow-up questions from given text using advanced rule-based approach"""
    try:
        # Clean and prepare the text
        clean_text = text.strip()
        if len(clean_text) < 10:
            return generate_fallback_questions(clean_text, num)

        # Extract key information from the text
        questions = []

        # Analyze the text for different types of content
        questions.extend(generate_contextual_questions(clean_text))
        questions.extend(generate_analytical_questions(clean_text))
        questions.extend(generate_practical_questions(clean_text))
        questions.extend(generate_comparative_questions(clean_text))

        # Remove duplicates and filter quality
        unique_questions = []
        for q in questions:
            if q not in unique_questions and len(q) > 10:
                unique_questions.append(q)

        # If we have enough questions, return them
        if len(unique_questions) >= num:
            return random.sample(unique_questions, num)

        # If not enough, add fallback questions
        fallback = generate_fallback_questions(clean_text, num - len(unique_questions))
        unique_questions.extend(fallback)

        return unique_questions[:num]

    except Exception as e:
        print(f"Error in question generation: {e}")
        return generate_fallback_questions(text, num)

def generate_contextual_questions(text):
    """Generate questions based on context and content analysis"""
    questions = []
    text_lower = text.lower()

    # Extract key nouns and concepts
    key_terms = extract_key_terms(text)

    # Technology/Science related questions
    if any(word in text_lower for word in ['technology', 'science', 'research', 'study', 'algorithm', 'system', 'method']):
        if key_terms:
            questions.append(f"How does {key_terms[0]} impact modern technology?")
            questions.append(f"What are the latest developments in {key_terms[0]}?")

    # Process/Method related questions
    if any(word in text_lower for word in ['process', 'method', 'approach', 'technique', 'procedure']):
        questions.append("What are the step-by-step details of this process?")
        questions.append("What are alternative methods to achieve similar results?")

    # Problem/Solution related questions
    if any(word in text_lower for word in ['problem', 'solution', 'issue', 'challenge', 'difficulty']):
        questions.append("What are the root causes of this problem?")
        questions.append("What other solutions have been tried for this issue?")

    # Definition/Concept related questions
    if any(word in text_lower for word in ['is', 'are', 'means', 'refers to', 'defined as']):
        if key_terms:
            questions.append(f"What are real-world examples of {key_terms[0]}?")
            questions.append(f"How is {key_terms[0]} different from similar concepts?")

    return questions

def generate_analytical_questions(text):
    """Generate analytical and deeper thinking questions"""
    questions = []
    key_terms = extract_key_terms(text)

    if key_terms:
        main_term = key_terms[0]
        questions.extend([
            f"What are the advantages and disadvantages of {main_term}?",
            f"How has {main_term} evolved over time?",
            f"What factors influence the effectiveness of {main_term}?",
            f"What are the potential future developments in {main_term}?",
            f"How does {main_term} compare to traditional approaches?"
        ])

    # General analytical questions
    questions.extend([
        "What are the underlying principles behind this concept?",
        "What evidence supports this information?",
        "What are the limitations or constraints involved?",
        "How might this change in the future?"
    ])

    return questions

def generate_practical_questions(text):
    """Generate practical application questions"""
    questions = []
    key_terms = extract_key_terms(text)

    if key_terms:
        main_term = key_terms[0]
        questions.extend([
            f"How can {main_term} be implemented in practice?",
            f"What skills are needed to work with {main_term}?",
            f"What tools or resources are required for {main_term}?",
            f"What are common mistakes when dealing with {main_term}?"
        ])

    # General practical questions
    questions.extend([
        "What are the practical applications of this concept?",
        "How can someone get started with this?",
        "What are the costs and benefits involved?",
        "What training or preparation is needed?"
    ])

    return questions

def generate_comparative_questions(text):
    """Generate comparative and relational questions"""
    questions = []
    key_terms = extract_key_terms(text)

    if key_terms:
        main_term = key_terms[0]
        questions.extend([
            f"How does {main_term} relate to other fields or disciplines?",
            f"What industries or sectors use {main_term}?",
            f"How does {main_term} vary across different contexts?",
            f"What are the global perspectives on {main_term}?"
        ])

    return questions

def extract_key_terms(text):
    """Extract key terms and concepts from text"""
    # Remove common words and extract meaningful terms
    common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}

    # Clean and split text
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # Filter out common words and short words
    key_terms = [word for word in words if word not in common_words and len(word) > 3]

    # Return unique terms, prioritizing longer ones
    unique_terms = list(dict.fromkeys(key_terms))  # Preserve order while removing duplicates
    return sorted(unique_terms, key=len, reverse=True)[:5]  # Return top 5 longest terms

def generate_fallback_questions(text, num=3):
    """Generate fallback questions when AI model fails"""
    words = text.split()[:5]
    base_text = ' '.join(words) if words else "this topic"

    fallback_questions = [
        f"What more can you tell me about {base_text}?",
        f"How does {base_text} work in practice?",
        f"What are the real-world applications of {base_text}?",
        f"How is {base_text} related to other concepts?",
        f"What are the benefits and limitations of {base_text}?",
        f"Can you explain {base_text} in more detail?",
        f"What should I know about {base_text}?",
        f"How can {base_text} be improved or enhanced?"
    ]

    return fallback_questions[:num]
