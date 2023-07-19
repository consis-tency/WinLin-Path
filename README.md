# Windows to Linux Path Converter

This is a simple Python script that allows you to convert Windows file paths to their corresponding Linux format. It replaces backslashes with forward slashes and converts drive letters to the appropriate Linux format.

## Prerequisites

Before using this converter, you need to have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation

1. Clone this repository or download the script directly.

```bash
git clone https://github.com/your_username/windows-to-linux-path-converter.git
```

2. Install the required `pyperclip` library using pip:

```bash
pip install pyperclip
```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where you have downloaded or cloned the repository.

3. Run the script by executing the following command:

```bash
python windows_to_linux_path_converter.py
```

4. You will be prompted to enter a Windows path.

5. After entering the path, press Enter, and the script will convert the path to its corresponding Linux format and copy it to your clipboard.

6. You can now paste the converted Linux path wherever you need it.

## Example

Let's say you have a Windows path:

```
C:\Users\YourUsername\Documents\file.txt
```

After running the script and providing this path as input, it will convert to the following Linux path:

```
/mnt/c/Users/YourUsername/Documents/file.txt
```

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Contributions are welcome!