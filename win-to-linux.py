import pyperclip

def windows_to_linux_path(windows_path):
    linux_path = windows_path.replace('\\', '/')
    if ':' in linux_path:
        drive_letter, rest_of_path = linux_path.split(':', 1)
        linux_path = '/mnt/' + drive_letter.lower() + rest_of_path
    return linux_path

# Take input from the user
windows_path = input("Enter a Windows path: ")
linux_path = windows_to_linux_path(windows_path)

# Copy the Linux path to clipboard
pyperclip.copy(linux_path)

print("Linux path:", linux_path)
print("Linux path has been copied to the clipboard.")
