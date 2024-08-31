import re

# Keywords and Tokens
KEYWORDS = {
    "DEC": "FUNCS",
    "cook": "VARS",
    "when": "IF",
    "otherwise": "ELSE",
    "WHILE": "WHILE",
    "FOR": "FOR",
    "gets": "INPUT",
    "puts": "OUTPUT",
    "read": "READ",
    "write": "WRITE",
    "close": "CLOSE",
    "open": "OPEN",
    "bring": "IMPORT",
    "call": "CALL",
}

TOKENS = [
    ("NUMBER", r"\d+(\.\d*)?"),
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
    ("EQ", r"=="),
    ("NEQ", r"!="),
    ("LE", r"<="),
    ("GE", r">="),
    ("QUOTE", r"'"),
    ("STRING", r"'[^']*'|\"[^\"]*\""),
    ("COMMENTS", r"#.*"),
    ("AMPERSAND", r"&"),
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
        # Dividing the code into tokens
        tokens = []
        pos = 0
        while pos < len(code):
            match = None
            for token_spec in self.token_specification:
                name, pattern = token_spec
                match = pattern.match(code, pos)
                if match:
                    text = match.group(0)
                    if name != "WHITESPACE" and name != "COMMENTS":
                        # Ignoring all whitespace and comments
                        if name == "ID" and text in self.keywords:
                            tokens.append((self.keywords[text], text))
                        else:
                            tokens.append((name, text))
                    pos = match.end(0)
                    break
            if not match:
                raise RuntimeError(f"Unexpected character: {code[pos]}")
        return tokens

    # Read code from a file (for the main interface)
    def read_code_from_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()


# Lexer instance
lexer = Lexer(token_specification, KEYWORDS)
