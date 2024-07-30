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

    def parse_expression(self):
        # Simple expression parser: handles +, -, *, /
        # Assumes tokens are in correct order without parentheses
        result = self.parse_term()
        while self.current_token and self.current_token[0] in {"PLUS", "MINUS"}:
            operator = self.eat(self.current_token[0])
            right = self.parse_term()
            if operator == "+":
                result += right
            elif operator == "-":
                result -= right
        return result

    def parse_term(self):
        # Handles * and / operators
        result = self.parse_factor()
        while self.current_token and self.current_token[0] in {"MULTIPLY", "DIVIDE"}:
            operator = self.eat(self.current_token[0])
            right = self.parse_factor()
            if operator == "*":
                result *= right
            elif operator == "/":
                result /= right
        return result

    def parse_factor(self):
        # Handles numbers and variables
        token_type = self.current_token[0]
        if token_type == "NUMBER":
            return float(self.eat("NUMBER"))
        elif token_type == "ID":
            var_name = self.eat("ID")
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise ValueError(f"Undefined variable: {var_name}")
        else:
            raise ValueError(f"Unexpected token: {token_type}")

    def parse_var(self):
        while self.current_token:
            if self.current_token[0] == "VARS":
                self.eat("VARS")
                var_name = self.eat("ID")
                self.eat("ASSIGN")
                value_type = self.current_token[0]
                if value_type in {
                    "NUMBER",
                    "STRING",
                    "ID",
                    "PLUS",
                    "MINUS",
                    "MULTIPLY",
                    "DIVIDE",
                }:
                    value = self.parse_expression()
                else:
                    raise ValueError(
                        f"Expected NUMBER, STRING, or ID, but got {value_type}"
                    )
                self.variables[var_name] = value
                # Comment this out later(only here for debugging)
                print(f"Parsed variable: {var_name} = {value}")
            elif self.current_token[0] in {"OUTPUT", "INPUT", "IF", "TILL", "FOR"}:
                # Handle other types of statements if needed
                self.advance()  # Skip over the current token
            else:
                self.advance()  # Skip over the current token


# ----------------------------------------------------#
parser = Parser(code)
parser.parse_var()
