import glob, shutil

def remove_last_occurence(mystr, removal, replacement):
    reverse_removal = removal[::-1]
    reverse_replacement = replacement[::-1]
    return mystr[::-1].replace(reverse_removal, reverse_replacement, 1)[::-1]

patterns = ['not_can_ann/*/*.png', 'not_can_ann/*/*.jpg', 'not_can_ann/*/*.jpeg']
# patterns = ['cansynth/2019*/*/*/*.png', 'cansynth/2019*/*/*/*.jpg', 'cansynth/2019*/*/*/*.jpeg']

for pattern in patterns:
    for file in glob.glob(pattern):
        print(file)
        new_path = file.replace('.', '_', file.count('.')-1)
        new_path = new_path.replace('_jpg', '')
        new_path = new_path.replace('_jpeg', '')
        new_path = new_path.replace('_png', '')
        new_path = new_path.replace('.jpeg', '.png')
        new_path = new_path.replace('.jpg', '.png')
        shutil.move(file, new_path)
        
      
patterns = ['not_can_ann/*/*.json'] #['*/*canisters*/*/*/*.json']
# patterns = ['cansynth/2019*/*/*/*.json']

for pattern in patterns:
    for file in glob.glob(pattern):
        print(file)
        new_path = remove_last_occurence(file, '.jpeg', '')
        new_path = remove_last_occurence(new_path, '.jpg', '')
        new_path = remove_last_occurence(new_path, '.png', '')
        new_path = file.replace('.', '_', file.count('.')-1)
        new_path = new_path.replace('_jpg', '')
        new_path = new_path.replace('_jpeg', '')
        new_path = new_path.replace('_png', '')
        shutil.move(file, new_path)