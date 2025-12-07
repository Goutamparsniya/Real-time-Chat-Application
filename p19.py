def process_paragraph(paragraph):
    words = paragraph.split()
    for i in range(len(words)):
        if '.' in words[i]:
            index_of_dot = words[i].index('.')
            words[i] = words[i][:index_of_dot + 1] + words[i][index_of_dot + 1:].upper()
    return ' '.join(words)

paragraph = input("Enter a paragraph: ")
processed_paragraph = process_paragraph(paragraph)
print("\nProcessed paragraph:")
print(processed_paragraph)
