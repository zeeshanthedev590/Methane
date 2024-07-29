from lexer import code


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]
        self.variables = {}

    def advance(self):
        if self.current_token_index < len(self.tokens) - 1:
            self.current_token_index += 1
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None

        remaining_tokens_count = len(self.tokens) - self.current_token_index - 1

    def eat(self, expected_token_type):
        if self.current_token[0] != expected_token_type:
            raise ValueError(
                f"Expected {expected_token_type}, but got {self.current_token[0]}"
            )
        else:
            value = self.current_token[1]
            self.advance()
            return value

    def parse_var(self):
        self.eat("VARS")
        var_name = self.eat("ID")
        self.eat("ASSIGN")

        value_type = self.current_token[0]
        if value_type in {"NUMBER", "STRING", "ID"}:
            value = self.eat(value_type)
        else:
            raise ValueError(f"Expected NUMBER, STRING, or ID, but got {value_type}")

        self.variables[var_name] = value
        print(f"Parsed variable: {var_name} = {value}")


# ----------------------------------------------------#
parser = Parser(code)
parser.parse_var()
