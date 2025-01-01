import os
import shutil
import zipfile
import ctypes, sys

# paths
download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# global variables
file_types = {
    'audio': ('.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg', '.wma'),
    'archive': ('.zip', '.rar', '.7z', '.tar', '.gz'),
    'image': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'),
    'video': ('.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'),
    'document': ('.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'),
    'spreadsheet': ('.xlsx', '.xls', '.csv', '.ods'),
    'code': ('.py', '.js', '.html', '.css', '.java', '.cpp'),
    'executable': ('.exe', '.msi', '.bat')
}

# checks if user is admin
def is_user_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# move files from a folder to new folders depending on their name
def organize_downloads(path):
    for filename in os.listdir(path):
        src = path + "/" + filename
        # sorting samples/YouTube audio downloads
        if "youtube" and "audio" in filename:
            new_destination = os.path.join(os.path.expanduser('~'), "OneDrive\\Documents\\YouTube")
            shutil.move(src, new_destination)
        # sorting drum kit downloads
       # if "kit" in filename and ".zip" in filename:
       #     new_destination = "C:\\Program Files\\Image-Line\\FL Studio 2024\\Data\\Patches\\Packs"
       #     new_path = os.path.join(new_destination, filename)
       #     shutil.move(src, new_destination)
       #     with zipfile.ZipFile(new_path, "r") as zip_ref:
      #          zip_ref.extractall(new_destination)
      #      os.remove(new_path)
        if ".zip" in filename or "setup" in filename.lower() or "installer" in filename.lower():
            os.remove(src)

def print_files_in_folder(ext, path):
  for root, dirs, files in os.walk(path):
    for name in files:
      if name.endswith(ext):
        print(name)  # printing file name

def main():
    if not is_user_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        return
    organize_downloads(download_path)

if __name__ == '__main__':
  main()