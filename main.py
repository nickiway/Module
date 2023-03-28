import re

def get_lines(): 
    with open('input/file_1.txt') as file_1, open('input/file_2.txt') as file_2:
        file_1_lines = clean_paragraphs(file_1.readlines())
        file_2_lines = clean_paragraphs(file_2.readlines())

    return [file_1_lines, file_2_lines]

def clean_paragraphs(text): 
    return [line.replace('\n', 'n') for line in text]
    

if __name__ == "__main__":
    print(get_lines())
