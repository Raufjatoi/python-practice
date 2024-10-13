file = input("File name: ").strip().lower()

media = {
    '.jpg': 'image/jpg',
    '.png': 'image/png',
    '.jpeg': 'image/jpeg',
    '.gif' : 'image/gif',
    '.pdf' : 'application/pdf',
    '.zip' : 'application/zip',
    '.txt' : 'text/txt'
}

for extensions , media in media.items():
    if file.endswith(extensions):
        print(media)
        break
else:
  print('didnt added yet on the system ')