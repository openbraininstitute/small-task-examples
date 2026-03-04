import os

def list_data_directory():
    data_path = "/data"
    
    if not os.path.exists(data_path):
        print(f"Directory {data_path} does not exist")
        return
    
    if not os.path.isdir(data_path):
        print(f"{data_path} is not a directory")
        return
    
    try:
        items = os.listdir(data_path)
        if not items:
            print(f"Directory {data_path} is empty")
        else:
            print(f"Contents of {data_path}:")
            for item in sorted(items):
                item_path = os.path.join(data_path, item)
                if os.path.isdir(item_path):
                    print(f"  [DIR]  {item}")
                else:
                    print(f"  [FILE] {item}")
    except PermissionError:
        print(f"Permission denied accessing {data_path}")
    except Exception as e:
        print(f"Error reading directory: {e}")

if __name__ == "__main__":
    list_data_directory()
