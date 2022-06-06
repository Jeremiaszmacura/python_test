class DataLoader:
    def __init__(self):
        self.data = []
        self.file_handler = None

    def open_file(self):
        self.file_handler = open(self.file_name, "r")
        return self.file_handler

    def close_file(self):
        if self.file_handler:
            self.file_handler.close()

    def read_data(self, file_name):
        forbidden_words = ["shit", "fuck"]
        try:
            self.file_name = file_name
            self.file_handler = self.open_file()

            for line_no, line in enumerate(self.file_handler.readlines()):
                d = line.strip().split(",")
                # Zadanie 3 - wrong separators in file
                wrong_separators = set(";./|:")
                if any((c in wrong_separators) for c in line):
                    raise ValueError(f"Used wrong separator in input file")
                data_tuple = name, surname = (d[0], d[1])
                # Zadanie 4 - duplicate name and surname pairs in file
                if data_tuple in self.data:
                    raise ValueError(
                        f'Duplicate name and surname pair in "{self.file_name}" file at {line_no} line'
                    )
                # Zadanie 5 - forbidden words in file
                for word in forbidden_words:
                    if word.lower() in (name.lower() or surname.lower()):
                        raise ValueError(f"Used forbidden words in input file")
                self.data.append(data_tuple)
        finally:
            self.close_file()

        if not self.data:
            raise ValueError(f"File is empty: {self.file_name}")

        return self.data
