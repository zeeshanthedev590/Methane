KEYWORDS = [
    ("FUNCS", "DEC"),  # Functions
    ("VARS", "cook"),  # Variables
    ("IF", "IF"),  # IF statements
    ("TILL", "TILL"),  # While loops are till loops
    ("FOR", "FOR"),  # For loops
    ("INPUT", "gets"),  # input statements
    ("OUTPUT", "puts"),  # prints statements
]

TOKENS = [
    ("NUMBER", r"\d+"),
    ("LPAREN", r"\{"),
    ("RPAREN", r"\}"),
    ("COMMA", r","),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("WHITESPACE", r"\s+"),
    ("ASSIGN", r"="),
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
]
