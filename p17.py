def process_paragraph(paragraph):
    sentences = paragraph.split('.')
    num_sentences = len(sentences) - 1
    capitalized_paragraph = ' '.join(word.capitalize() for word in paragraph.split())
    return num_sentences, capitalized_paragraph

paragraph = input("Enter a paragraph: ")
num_sentences, capitalized_paragraph = process_paragraph(paragraph)
print(f"\nNumber of sentences: {num_sentences}")
print("Capitalized paragraph:")
print(capitalized_paragraph)
