import re

# get lines
def get_lines(): 
    with open('input/file_1.txt') as file_1, open('input/file_2.txt') as file_2:
        file_1_lines = clean_paragraphs(file_1.readlines())
        file_2_lines = clean_paragraphs(file_2.readlines())

    return [file_1_lines, file_2_lines]

# clean paragraphs
def clean_paragraphs(text): 
    return ''.join([line.replace('\n', '') for line in text])
    
# compare sentece
def compare_sentences(line_1, line_2):
    same_lines = set(line_1) & set(line_2)
    diff_lines = set(line_1) ^ set(line_2)
    
    return [same_lines, diff_lines]

# write to files function
def write_to_files(output_file, lines):
    with open(output_file, 'w') as output:
        output.writelines(sorted(lines))
# main
if __name__ == "__main__":
    print(compare_sentences('My mate. Hello.', 'My no mate.Hello'))
    write_to_files('output/same.txt',compare_sentences(get_lines()[0], get_lines()[1])[0])
    write_to_files('output/diff.txt',compare_sentences(get_lines()[0], get_lines()[1])[1])
