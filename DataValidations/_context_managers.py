class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)
    
    def __enter__(self):
        print('Enter')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'{exc_type}, {exc_value}, {traceback}')
        print('Exit')
        self.file.close()
        if exc_type == Exception:
            return True


with File('file.txt', 'w') as f:
    print('Middle')
    f.write('Hello!')
    raise FileExistsError()


   






    






