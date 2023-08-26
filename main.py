import os
import datetime

os.chdir(r"C:\\Users\\user\\Downloads")
print(os.getcwd())

files = os.listdir()
extensions = {
    "images": [".jpg", ".png", ".jpeg", ".gif",".svg","ico"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar",".gz"],
    "documents": [".doc", ".docx", ".pdf", ".txt",".csv",".xlsx"],
    "programs": [".py", ".php", ".html",".sql",".xml",".json","rss"],
    "exe": [".exe",".msi",".dll"],
    "iso": [".iso"]
}

def sorting(file):
    keys = list(extensions.keys())
    for key in keys:
        for ext in extensions[key]:
            if file.endswith(ext):
                return key




date_du_jour = datetime.date.today()


directori = "C:\\Users\\user\\Downloads\\classement"+date_du_jour.strftime("%Y-%m-%d")

for file in files:
    dis = sorting(file)
    if dis:
        source_path = os.path.join(os.getcwd(), file)
        destination_dir = os.path.join(directori, dis)
        destination_path = os.path.join(destination_dir, file)
        if os.path.exists(source_path):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            cmd = f'move "{source_path}" "{destination_path}"'
            # print(cmd)
            os.system(cmd)
        else:
            print(f"File '{file}' does not exist in the current directory.")