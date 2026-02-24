def file_to_read(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e :
        print(f"Error reading file: {e}")
        return None
    
def count_words(file, count=0):
    if file == None:
        return 0
    for i in file:
        if i.isalpha():
            count += 1
    print(count)
    
file = file_to_read('/home/nacho/Desktop/Doc_test')
count_words(file)