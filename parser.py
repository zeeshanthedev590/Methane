# For testing
# from lexer import code


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = (
            self.tokens[self.current_token_index] if self.tokens else None
        )
        self.variables = {}

    def advance(self):
        """Move to the next token."""
        if self.current_token_index < len(self.tokens) - 1:
            self.current_token_index += 1
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None

    def eat(self, expected_token_type):
        """Consume the current token if it matches the expected type."""
        if self.current_token is None:
            raise ValueError(f"Unexpected end of input, expected {expected_token_type}")
        if self.current_token[0] != expected_token_type:
            raise ValueError(
                f"Expected {expected_token_type}, but got {self.current_token[0]}"
            )
        else:
            value = self.current_token[1]
            self.advance()
            return value

    def parse_expression(self):
        """Parse an expression involving +, -, *, and /."""
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
        """Parse a term involving * and /."""
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
        """Parse a factor which could be a number, variable, or string."""
        token_type = self.current_token[0]
        if token_type == "NUMBER":
            return float(self.eat("NUMBER"))
        elif token_type == "ID":
            var_name = self.eat("ID")
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise ValueError(f"Undefined variable: {var_name}")
        elif token_type == "STRING":
            return self.eat("STRING").strip('"')
        else:
            raise ValueError(f"Unexpected token: {token_type}")

    def parse_var(self):
        """Parse variable declarations and assignments."""
        while self.current_token and self.current_token[0] == "VARS":
            self.eat("VARS")
            var_name = self.eat("ID")
            self.eat("ASSIGN")
            value = self.parse_expression()
            self.variables[var_name] = value

    def parse_output(self):
        """Parse an output statement."""
        self.eat("OUTPUT")
        self.eat("LPAREN")
        if self.current_token[0] == "STRING":
            value = self.eat("STRING").strip('"')
        elif self.current_token[0] == "NUMBER":
            value = float(self.eat("NUMBER"))
        elif self.current_token[0] == "ID":
            var_name = self.eat("ID")
            if var_name in self.variables:
                value = self.variables[var_name]
            else:
                raise ValueError(f"Undefined variable: {var_name}")
        else:
            value = self.parse_expression()
        self.eat("RPAREN")
        print(value)

    def parse_input(self):
        """Parse an input statement."""
        self.eat("INPUT")
        self.eat("LPAREN")
        self.eat("AMPERSAND")
        var_name = self.eat("ID")
        self.eat("RPAREN")
        user_input = input()
        if user_input.isdigit():
            self.variables[var_name] = int(user_input)
        else:
            self.variables[var_name] = user_input

    def parse(self):
        while self.current_token:
            if self.current_token[0] == "VARS":
                self.parse_var()
            elif self.current_token[0] == "OUTPUT":
                self.parse_output()
            elif self.current_token[0] == "INPUT":
                self.parse_input()
            else:
                self.advance()


# ----------------Testing only------------------------#
# Parser instance
# parser = Parser(code)
# parser.parse()
