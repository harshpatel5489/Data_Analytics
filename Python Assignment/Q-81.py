def list_file(file_name, data_list):
    with open(file_name, 'a') as file:  # Use 'a' for appending
        for item in data_list:
            file.write(f"{item}\n")


file_name = 'Q-82.txt'
data_list = ['Apple', 'Banana', 'Cherry', 'Date']
list_file(file_name, data_list)
