import os

DIRECTORY = r"C:\Users\User\skillbox\project_rename_title\Test"


def rename_files(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def get_valid_name(name):
    name = name.replace("Без названия", "Picture")
    name = name.replace(" ", "")
    if not name.startswith("T_"):
        name = 'T_' + name
    return name


if __name__ == '__main__':
    rename_files(DIRECTORY)
