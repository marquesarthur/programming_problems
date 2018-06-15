def load_data(file_path):
    with open(file_path, 'r') as input_file:
        data = input_file.read()
        return data
    return None
