from lab_app.data_loader import DataLoader


INPUT_FILE_PATH = "input_test.csv"


class APP:
    def __init__(self):
        self.data_loader = DataLoader()

    def generate_mail(self, name, surname):
        arg_l = [name.lower(), surname.lower()]
        m_str = "_".join(arg_l)
        return f"{m_str}@example.com"

    def run(self, file_name):
        print("Welcome to mail generator app")
        print(f"Using input file {file_name}")

        data = self.data_loader.read_data(file_name)
        mails = []
        for name, surname in data:
            _mail = self.generate_mail(name, surname)
            mails.append(_mail)
        return mails


if __name__ == "__main__":
    APP().run(INPUT_FILE_PATH)
