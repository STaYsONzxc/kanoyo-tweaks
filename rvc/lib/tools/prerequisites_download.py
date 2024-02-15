import os
import wget
import sys

url_base = "https://huggingface.co/kanoyo/0v2Super/resolve/main"
models_download = [
    (
        "pretrained_v2/",
        [
            "f0D40k.pth",
            "f0G40k.pth",
        ],
    ),
]

models_file = [
    "hubert_base.pt",
    "rmvpe.pt",
    "fcpe.pt",
    # "rmvpe.onnx"
]

executables_file = []

folder_mapping = {
    "pretrained_v2/": "rvc/pretraineds/pretrained_v2/",
}

for file_name in models_file:
    destination_path = os.path.join(file_name)
    url = f"{url_base}/{file_name}"
    if not os.path.exists(destination_path):
        os.makedirs(os.path.dirname(destination_path) or ".", exist_ok=True)
        print(f"\nDownloading {url} to {destination_path}...")
        wget.download(url, out=destination_path)

for file_name in executables_file:
    if sys.platform == "win32":
        destination_path = os.path.join(file_name)
        url = f"{url_base}/{file_name}"
        if not os.path.exists(destination_path):
            os.makedirs(os.path.dirname(destination_path) or ".", exist_ok=True)
            print(f"\nDownloading {url} to {destination_path}...")
            wget.download(url, out=destination_path)

for remote_folder, file_list in models_download:
    local_folder = folder_mapping.get(remote_folder, "")
    for file in file_list:
        destination_path = os.path.join(local_folder, file)
        url = f"{url_base}/{remote_folder}{file}"
        if not os.path.exists(destination_path):
            os.makedirs(os.path.dirname(destination_path) or ".", exist_ok=True)
            print(f"\nDownloading {url} to {destination_path}...")
            wget.download(url, out=destination_path)
