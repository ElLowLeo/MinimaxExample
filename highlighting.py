from termcolor import colored
import re

def highlight_comment(comment):
    parts = comment.split('#', 1)
    if len(parts) == 2:
        return colored('#', 'dark_grey') + colored(parts[1], 'dark_grey')
    return comment

def syntax_highlight(code):
    highlighted_code = ""

    for line in code.split('\n'):
        
        line_without_comment = line.split('#', 1)[0]
            
        highlighted_line = re.sub(r'\b(função|se|senão|para cada|enquanto|retorne|Nulo|Verdadeiro|Falso)\b', 
                                      lambda m: colored(m.group(), 'light_cyan'), line_without_comment)

        highlighted_line = highlighted_line.replace(
            'infinito', colored('infinito', 'magenta')
        )
            
        highlighted_line = re.sub(r'"[^"]*"', lambda m: colored(m.group(), 'light_green'), highlighted_line)
        highlighted_line = re.sub(r"'[^']*'", lambda m: colored(m.group(), 'light_green'), highlighted_line)
            
        if '"""' in line:
            in_multiline_comment = not in_multiline_comment
            
        highlighted_line = line.replace(line_without_comment, highlighted_line)
        highlighted_line = highlight_comment(highlighted_line)

        highlighted_code += highlighted_line + '\n'

    return highlighted_code

if __name__ == "__main__":
    with open('MinimaxExampleCode/minimaxExample.pt', 'r') as file:
        code = file.read()
    highlighted_code = syntax_highlight(code)
    print(highlighted_code)
