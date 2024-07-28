import re

# Keywords and Tokens
KEYWORDS = {
    "DEC": "FUNCS",  # Functions
    "cook": "VARS",  # Variables
    "IF": "IF",  # IF statements
    "TILL": "TILL",  # While loops are till loops
    "FOR": "FOR",  # For loops
    "gets": "INPUT",  # Input statements
    "puts": "OUTPUT",  # Output statements
}

TOKENS = [
    ("NUMBER", r"\d+"),
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COMMA", r","),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("SEMICOLON", r";"),
    ("WHITESPACE", r"\s+"),
    ("ASSIGN", r"="),
    ("GT", r">"),
    ("LT", r"<"),
    ("QUOTE", r"'"),
    ("STRING", r"'[^']*'|\"[^\"]*\""),
    ("COMMENTS", r"//.*"),
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
]

# Combine Tokens
token_specification = TOKENS


# Lexer Class
class Lexer:
    def __init__(self, token_specification, keywords):
        self.token_specification = [
            (name, re.compile(pattern)) for name, pattern in token_specification
        ]
        self.keywords = keywords

    def tokenize(self, code):
        tokens = []
        pos = 0
        while pos < len(code):
            match = None
            for token_spec in self.token_specification:
                name, pattern = token_spec
                match = pattern.match(code, pos)
                if match:
                    text = match.group(0)
                    if (
                        name != "WHITESPACE" and name != "COMMENTS"
                    ):  # Skip whitespace and comments
                        # Check if the identifier is a keyword
                        if name == "ID" and text in self.keywords:
                            tokens.append((self.keywords[text], text))
                        else:
                            tokens.append((name, text))
                    pos = match.end(0)
                    break
            if not match:
                raise RuntimeError(f"Unexpected character: {code[pos]}")
        return tokens


# Sample Usage
lexer = Lexer(token_specification, KEYWORDS)
