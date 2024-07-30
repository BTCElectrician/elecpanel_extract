# Electrical Panel Information Extractor

This Python script extracts electrical panel information from PDF drawings or text files.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/elecpanel_extract.git
   cd elecpanel_extract
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your PDF file or text file containing electrical panel information in the project directory.

2. Open `elecpanel_extract.py` and update the `file_path` variable with your file's name:
   ```python
   file_path = 'your_file_name.pdf'  # or 'your_file_name.txt' for text files
   ```

3. Run the script:
   ```
   python elecpanel_extract.py
   ```

## Fields Extracted

- PANEL
- VOLTAGE
- FEED
- CIRCUITS
- LOAD NAME
- TRIP
- POLE
- EQUIPMENT REFERENCE

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)