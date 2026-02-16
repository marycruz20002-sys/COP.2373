import re

def get_spam_keywords():
    """Returns a list of 30 common spam words and phrases."""
    return [
        "act now", "apply online", "bank account", "trial gift", "best price",
        "bonus", "click here", "congratulations", "credit card", "bonus cash",
        "double your income", "earn money", "exclusive deal", "free access",
        "free", "guaranteed", "instant", "investment", "limited time",
        "lottery", "last call", "no cost", "offer", "credit check",
        "pre-approved", "prize", "risk-free", "special",
        "unsubscribe", "winner"
    ]

def analyze_email(email_text):
    """Scans email, calculates score, and identifies keywords."""
    keywords = get_spam_keywords()
    score = 0
    found_words = []
    
    # Lowercase for case-insensitive matching
    email_lower = email_text.lower()
    
    for word in keywords:
        # Use regex to find whole phrases or words
        matches = re.findall(rf'\b{re.escape(word)}\b', email_lower)
        if matches:
            count = len(matches)
            score += count
            found_words.append(f"{word} (x{count})")
            
    return score, found_words

def rate_likelihood(score):
    """Rates the likelihood of spam based on the score."""
    if score == 0:
        return "Low (Safe)"
    elif score <= 3:
        return "Medium (Suspicious)"
    else:
        return "High (Likely Spam)"

def main():
    print("--- Email Spam Scanner ---")
    user_email = input("Enter your email message content:\n")
    
    score, found = analyze_email(user_email)
    likelihood = rate_likelihood(score)
    
    print("\n--- Results ---")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")
    print(f"Spam Keywords Found: {', '.join(found) if found else 'None'}")

if __name__ == "__main__":
    main()
