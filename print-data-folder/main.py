import os

def list_directory(path):
    """List contents of a single directory."""
    if not os.path.exists(path):
        print(f"Directory {path} does not exist")
        return
    
    if not os.path.isdir(path):
        print(f"{path} is not a directory")
        return
    
    try:
        items = os.listdir(path)
        if not items:
            print(f"Directory {path} is empty")
        else:
            print(f"Contents of {path}:")
            for item in sorted(items):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    print(f"  [DIR]  {item}")
                else:
                    print(f"  [FILE] {item}")
    except PermissionError:
        print(f"Permission denied accessing {path}")
    except Exception as e:
        print(f"Error reading directory: {e}")

def list_all_directories():
    """List contents of /data and its subdirectories."""
    directories = [
        "/data",
        "/data/aws_s3_open",
        "/data/aws_s3_internal"
    ]
    
    for directory in directories:
        list_directory(directory)
        print()  # Empty line between directories

if __name__ == "__main__":
    list_all_directories()
