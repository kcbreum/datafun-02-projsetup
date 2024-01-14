import pathlib

def create_project_directory(directory_name: str):
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main():
    create_project_directory('test')
    create_project_directory('docs')

if __name__ == '__main__':
    main()
