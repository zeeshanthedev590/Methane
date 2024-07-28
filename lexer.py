import re

KEYWORDS = [
    ("FUNCS", "DEC"),
    ("VARS", "cook"),
    ("IF", "IF"),
    ("TILL", "TILL"),
    ("FOR", "FOR"),
]

TOKENS = [
    ("NUMBER", r"\d+"),
    ("LPAREN", r"\{"),
    ("RPAREN", r"\)"),
    ("COMMA", r","),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("WHITESPACE", r"\s+"),
    ("ASSIGN", r"="),
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
]
