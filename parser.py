import os


class Parser:
    def __init__(self, tokens, script_path):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = (
            self.tokens[self.current_token_index] if self.tokens else None
        )
        self.variables = {}
        self.script_dir = os.path.dirname(script_path)

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

    def parse_open(self):
        self.eat("OPEN")

        var_name = self.eat("ID")

        self.eat("ASSIGN")

        filename = self.eat("STRING").strip('"')

        full_path = os.path.join(self.script_dir, filename)

        try:
            file_handle = open(full_path, "r+")
            self.variables[var_name] = file_handle
        except IOError as e:
            raise RuntimeError(f"Error opening file: {e}")

    def parse_read(self):
        self.eat("READ")

        var_name = self.eat("ID")

        self.eat("ASSIGN")

        file_var = self.eat("ID")

        if file_var not in self.variables:
            raise ValueError(f"Undefined file handle: {file_var}")

        file_handle = self.variables[file_var]

        try:
            content = file_handle.read()
            self.variables[var_name] = content
        except IOError as e:
            raise RuntimeError(f"Error reading file: {e}")

    def parse_write(self):
        self.eat("WRITE")
        file_var = self.eat("ID")
        self.eat("ASSIGN")

        if self.current_token[0] == "STRING":
            content = self.eat("STRING").strip('"')
        elif self.current_token[0] == "ID":
            content_var = self.eat("ID")
            if content_var not in self.variables:
                raise ValueError(f"Undefined variable: {content_var}")
            content = self.variables[content_var]
        else:
            raise ValueError("Expected a STRING or an ID after assignment.")

        if file_var not in self.variables:
            raise ValueError(f"Undefined file handle: {file_var}")

        file_handle = self.variables[file_var]

        try:
            file_handle.write(content + "\n")
        except IOError as e:
            raise RuntimeError(f"Error writing to file: {e}")

    def parse_close(self):
        self.eat("CLOSE")

        file_var = self.eat("ID")

        if file_var not in self.variables:
            raise ValueError(f"Undefined file handle: {file_var}")

        file_handle = self.variables[file_var]

        try:
            file_handle.close()
            del self.variables[file_var]
        except IOError as e:
            raise RuntimeError(f"Error closing file: {e}")

    def parse(self):
        while self.current_token:
            if self.current_token[0] == "VARS":
                self.parse_var()
            elif self.current_token[0] == "OUTPUT":
                self.parse_output()
            elif self.current_token[0] == "INPUT":
                self.parse_input()
            elif self.current_token[0] == "OPEN":
                self.parse_open()
            elif self.current_token[0] == "READ":
                self.parse_read()
            elif self.current_token[0] == "WRITE":
                self.parse_write()
            elif self.current_token[0] == "CLOSE":
                self.parse_close()

            else:
                self.advance()
