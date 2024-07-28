from lexer import lexer


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]

    def advance(self):
        if self.current_token_index < len(self.tokens) - 1:
            self.current_token_index += 1
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None

        remaining_tokens_count = len(self.tokens) - self.current_token_index - 1

    def eat(self):
        pass
