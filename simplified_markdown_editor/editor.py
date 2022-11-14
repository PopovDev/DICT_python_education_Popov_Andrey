"""Markdown editor class"""


class Editor:
    """Markdown editor"""

    def __init__(self):
        self.text = ""

    def add_plain(self, text):
        """Add plain text to the document"""
        self.text += text

    def add_bold(self, text: str) -> None:
        """Add bold text to the document"""
        self.text += f"**{text}**"

    def add_italic(self, text: str) -> None:
        """Add italic text to the document"""
        self.text += f"*{text}*"

    def add_header(self, text: str, level: int) -> None:
        """Add header text to the document"""
        if level > 6 or level < 1:
            raise ValueError("Level must be between 1 and 6")
        self.text += f"{'#' * level} {text}\n"

    def add_link(self, label: str, url: str) -> None:
        """Add link to the document"""
        self.text += f"[{label}]({url})"

    def add_code(self, text: str) -> None:
        """Add code to the document"""
        self.text += f"`{text}`"

    def add_ordered_list(self, items: list) -> None:
        """Add ordered list to the document"""
        for i, item in enumerate(items):
            self.text += f"{i + 1}. {item}\n"

    def add_unordered_list(self, items: list) -> None:
        """Add unordered list to the document"""
        for item in items:
            self.text += f"* {item}\n"

    def add_new_line(self) -> None:
        """Add new line to the document"""
        self.text += "\n"

    def __str__(self) -> str:
        """Return the document text"""
        return self.text

    def save(self, filename: str) -> None:
        """Save the document to a file"""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text)

    def prompt_str(self, prompt: str) -> str:
        """Prompt correct string"""
        while True:
            input_str = input(f"{prompt}:\n> ").strip()
            if input_str:
                return input_str
            print("String cannot be empty")

    def prompt_int(self, prompt: str) -> int:
        """Prompt correct integer"""
        while True:
            try:
                return int(input(f"{prompt}:\n> "))
            except ValueError:
                print("Enter a valid integer")

    def prompt_string_list(self) -> list:
        """Prompt list of strings"""
        length = self.prompt_int("Number of rows")
        return [self.prompt_str(f"Row #{i + 1}") for i in range(length)]

    def help(self) -> str:
        """Help data"""
        return """Available formatters:
plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done"""

    def run(self) -> None:
        """Run the editor"""
        while True:
            try:
                command = self.prompt_str("Choose a formatter")
                match(command):
                    case "plain":
                        self.add_plain(self.prompt_str("Text"))
                    case "bold":
                        self.add_bold(self.prompt_str("Text"))
                    case "italic":
                        self.add_italic(self.prompt_str("Text"))
                    case "header":
                        self.add_header(self.prompt_str("Text"),
                                        self.prompt_int("Level"))
                    case "link":
                        self.add_link(self.prompt_str("Label"),
                                      self.prompt_str("URL"))
                    case "inline-code":
                        self.add_code(self.prompt_str("Text"))
                    case "ordered-list":
                        self.add_ordered_list(self.prompt_string_list())
                    case "unordered-list":
                        self.add_unordered_list(self.prompt_string_list())
                    case "new-line":
                        self.add_new_line()
                    case "!help":
                        print(self.help())
                        continue
                    case "!done":
                        filename = "output.md"
                        self.save(filename)
                        print(f"Saved to {filename}")
                        break
                    case _:
                        print("Unknown formatting type or command. Please try again")
                        continue
                print(self)
            except ValueError as error:
                print(error)
            except KeyboardInterrupt:
                print("\nThrowing the keyboard away")
                break
