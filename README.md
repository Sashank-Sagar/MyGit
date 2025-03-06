# MyGit

MyGit is a simplified version control system that mimics basic Git functionalities. It allows users to initialize repositories, add files, commit changes, view commit history, and check differences between commits.

## Features

- Initialize a MyGit repository (`init`)
- Add files to the staging area (`add`)
- Commit changes with a message (`commit`)
- View commit history (`log`)
- Show differences between commits (`diff`)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Sashank-Sagar/MyGit.git
   ```
2. Navigate to the project directory:
   ```sh
   cd MyGit
   ```
3. (Optional) Set up a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
4. Install dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run `mygit` commands using the CLI:

```sh
python cli.py init          # Initialize a MyGit repository
python cli.py add <file>    # Add files to the staging area
python cli.py commit -m "Message" # Commit changes
python cli.py log           # Show commit history
python cli.py diff <hash>   # Show differences between commits
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request


## Author

[Sashank Sagar](https://github.com/Sashank-Sagar)

