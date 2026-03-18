import re

def split_into_sentences(paragraph):
    """
    Splits a paragraph into a list of sentences using regex.
    Handles various sentence end cases, including sentences that
    begin with numbers.
    """
    sentences = re.split(r'(?:[.!?])(?=\s|$)', paragraph)
    
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def main():
    print("Enter a paragraph (including sentences that may begin with numbers).")
    print("Press Enter twice to finish input:\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    paragraph = " ".join(lines)
    
    if not paragraph:
        print("No paragraph entered.")
        return

    sentences_list = split_into_sentences(paragraph)
    
    print("\n" + "="*30)
    print(f"Total number of sentences: {len(sentences_list)}")
    print("="*30 + "\n")
    
    print("Individual sentences:")
    # Display each sentence with a number prefix
    for i, sentence in enumerate(sentences_list, 1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()
