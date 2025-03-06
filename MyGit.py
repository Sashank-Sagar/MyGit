
import os
import hashlib
import time
import difflib


class MyGit():
    def __init__(self): # Constructor to set the basic path
        self.get_dir = '.mygit'
        self.object_dir = os.path.join(self.get_dir,"Objects")
        self.refs_dir = os.path.join(self.get_dir,"refs","heads")
        self.index_file = os.path.join(self.get_dir,"Index")
        self.head_file = os.path.join(self.get_dir,"HEAD")

    def init(self):# Feature to initialize the repository
        if os.path.exists(self.get_dir):
            print("Repository already exists")
            return
        # Creating the directories
        try:
            os.makedirs(self.object_dir, exist_ok= True)
            os.makedirs(self.refs_dir, exist_ok= True)
        except OSError as e:
            print(f"Error: Could not create directory {e}")
            return
        # Creating files
        try:
            open(self.index_file, 'w').close()
            open(self.head_file, 'w').close()
        except OSError as e:
            print(f"Error: Could not create file {e}")
            return
        
        print("Initialized empty MyGit repository ")

    def file_content_hash(self, filename):  # function to get the hash of the file content
        try:
            if not os.path.isfile(filename):
                raise FileNotFoundError(f"Error: File {filename} does not exist or is not a file")
            with open(filename, 'rb') as f:
                content = f.read()
                return hashlib.sha1(content).hexdigest()
        except OSError as e:
            raise OSError(f"Error: Could not read file {filename} {e}")
            
    def write_file(self,path, content, mode='w'): # function to write content to a file
        try:
            os.makedirs(os.path.dirname(path), exist_ok= True) # Creates the directory if it does not exist
            with open(path, mode) as f:
                f.write(content)
        except OSError as e:
            raise Exception(f"Error: Could not write to file {path} {e}")

    def read_file(self,path, mode= 'r'): # function to read content from a file
        try:
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Error: File {path} does not exist or is not a file")
            with open(path, mode, encoding="utf-8") as f:
                return f.read()
        except UnicodeDecodeError:
            # If UTF-8 fails, try Latin-1 (fallback for unknown encodings)
            with open(path, mode, encoding="latin-1") as f:
                return f.read()
        except OSError as e:
            raise OSError(f"Error: Could not read file {path} {e}")

    def read_index(self): # function to read the index file
        try:
            if not os.path.isfile(self.index_file):
                return {}  # Return an empty dictionary if index file does not exist

            content = self.read_file(self.index_file)
            index_data = {}

            for line in content.splitlines():
                if ":" in line:  # Ensure the line follows the expected format
                    parts = line.split(":",1)
                    if len(parts) == 2:
                        filename, file_hash = parts
                        index_data[filename] = file_hash.strip()

            return index_data
        except OSError as e:
            raise Exception(f"Error: Could not read Index file {self.index_file} {e}")

    def is_file_tracked(self, file_hash): # function to check if file is already stored
        content_path = os.path.join(self.object_dir, file_hash)
        return os.path.exists(content_path) # return True if file already stored else False 

    def update_index(self, filename, file_hash): # function to update the index file
        try:
            # Read current index contents (if exists)
            index_data = self.read_index() or {}
            # Check if file already exists with the same hash
            if index_data.get(filename) == file_hash:
                print(f"File: {filename} already added")
                return
            
            # Update or append entry
            index_data[filename] = file_hash
            updated_content = "\n".join(f"{f}:{h}" for f, h in index_data.items())

            # Write the updated content
            self.write_file(self.index_file, updated_content)
        except OSError as e:
            raise Exception(f"Error: Could not update index file {self.index_file} - {e}")

    def store_file_object(self, file_hash, content): # function to store the file in the object directory
        try:
            object_path = os.path.join(self.object_dir, file_hash)
            if not os.path.exists(object_path):
                self.write_file(object_path, content, 'wb')
        except OSError as e:
            raise Exception(f"Error: could not store the file {file_hash} in objects {e}")    

    def add(self, filename): # Feature for adding file in staging area
        try:
            if not os.path.isfile(filename):
                print(f"Error: File {filename} does not exist")
                return
            file_hash = self.file_content_hash(filename)
            if file_hash is None:
                raise Exception(f"Error: Unable to hash file {filename}")
            
            staged_files = self.read_index()
            # Checking if file is already staged or not
            if staged_files.get(filename) == file_hash:
                print(f"File {filename} is already staged with same content")
                return
            
            with open(filename, 'rb') as f:
                content = f.read()
            self.store_file_object(file_hash, content)

            # Update index
            self.update_index(filename, file_hash)
        
            print(f"File '{filename}' added successfully")
        
        except OSError as e:
            raise Exception(f"Error: File {filename} could not be added - {e}")

    def get_latest_commit_hash(self): # Hepler function to get parent/latest commit
        try:
            if os.path.exists(self.head_file):  
                content = self.read_file(self.head_file).strip()    
                return content if content else None # Return the hash if exists else None
            return None # Return None if HEAD file does not exist
        except OSError as e:
            raise Exception(f"Error: Could not read Head file - {e}")

    def create_commit_content(self, commit_message, staged_files, latest_commit_hash): # Helper function to create commit content
        commit_data = {
            "parent": latest_commit_hash,
            "timestamp": time.strftime("%a %b %d %H:%M:%S %Y"),
            "message": commit_message,
            "files": staged_files
        }
        commit_content = f"parent: {commit_data['parent']}\n"
        commit_content += f"timestamp: {commit_data['timestamp']}\n"
        commit_content += f"message: {commit_data['message']}\n\n"
        commit_content += "files\n" # to do  for after 
        for filename , file_hash in commit_data["files"].items():
            commit_content += f"    {filename}: {file_hash}\n"

        return commit_content

    def commit(self, message): # Feature to commit the staged files
        try:
            staged_files = self.read_index()
            if not staged_files:
                print("No files to commit")
                return

            # Getting Latest Commit Hash from Head file
            latest_commit_hash = self.get_latest_commit_hash()

            # Creating Commit metadata
            commit_message = message
            commit_content = self.create_commit_content(commit_message, staged_files, latest_commit_hash)

            commit_hash = hashlib.sha1(commit_content.encode()).hexdigest()

            self.store_file_object(commit_hash, commit_content.encode())

            # Update Head to point to latest commit
            self.write_file(self.head_file, commit_hash)

            # Clearing Index file
            self.write_file(self.index_file, "")

            print(f"Commit successfully - {commit_hash}")
        
        except OSError as e:
            raise Exception(f"Error: Commit failed - {e}")
        finally:
            # To ensure index file is cleared even if an error occurs
            self.write_file(self.index_file, "")

    def log(self): # Feature to display the commit history
        try:
            # Get the latest commit hash
            commit_hash = self.get_latest_commit_hash()
            if not commit_hash or commit_hash.strip() == "": # If no commit found
                print("No commit found")
                return
            
            while commit_hash:
                commit_content = self.read_file(os.path.join(self.object_dir, commit_hash))

                # Extracting commit metadata
                lines = commit_content.splitlines()
                parent = None
                timestamp = ""
                message = ""

                for line in lines:
                    if line.startswith("parent:"):
                        parent = line.split(":",1)[1].strip()
                        if parent == "None":  # Fix: Stop when reaching the first commit
                            parent = None
                    elif line.startswith("timestamp:"):
                        timestamp = line.split(":",1)[1].strip()
                    elif line.startswith("message:"):
                        message = line.split(":",1)[1].strip()
                    
                # Display Commit_content
                print(f"Commit: {commit_hash}")
                print(f"Date: {timestamp}")
                print(f"Message: {message}")
                print("-" * 48)
                
                # Move from latest commit to parent commit 
                commit_hash = parent if parent else None #  Stop if parent is None

        except OSError as e:
            raise Exception(f"Error: Could not read commit history - {e}")

    def read_commit_data(self,commit_hash): # Helper function to read commit data
        try:
            if not commit_hash:
                raise ValueError("Error: No commit hash provided")
            commit_content = self.read_file(os.path.join(self.object_dir, commit_hash))
            if not commit_content:
                raise ValueError(f"Error: Commit {commit_hash} is empty or corrupted")
            
            # Extracting commit metadata
            lines = commit_content.splitlines()
            files_list = False
            commit_data = {
                "parent": None,"timestamp": "","message": "","files": {}
            }
            for line in lines:
                line = line.strip()

                if line.startswith("parent:"):
                    parent_hash = line.split(":", 1)[1].strip()
                    commit_data["parent"] = parent_hash if parent_hash != "None" else None # Fix: Stop when reaching the first commit
                elif line.startswith("timestamp:"):
                    commit_data["timestamp"] = line.split(":",1)[1].strip()
                elif line.startswith("message"):
                    commit_data["message"] = line.split(":",1)[1].strip()
                elif line.strip() == "files": # Detect when the file list going to start
                    files_list = True
                    continue
                elif files_list and ":" in line:
                        filename, file_hash = line.split(":",1)
                        commit_data["files"][filename.strip()] = file_hash.strip() 
            
            return commit_data
        except FileNotFoundError:
            print(f"Waring: Commit file for hash {commit_hash} not found | (Might be first commit)")
            return None

    def get_file_content(self, file_hash): # Helper function to get the file content
        try:
            if not file_hash:
                raise ValueError("Error: Commit hash or filename is missing")
            file_path = os.path.join(self.object_dir, file_hash)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Error: File {file_hash} not found")
        
            # Read in binary mode and decode
            with open(file_path, "rb") as f:
                content = f.read()

            try:
                return content.decode("utf-8")  # Attempt to decode as UTF-8
            except UnicodeDecodeError:
                return content.decode("utf-16")  # Fallback for UTF-16 files

        except OSError:
            raise Exception("Error: Failed to get file content") 

    def compute_difference(self, content1, content2, filename): # Helper function to compute the difference between two files
        try:
            if content1 is None or content2 is None:
                raise ValueError("Error: One or both file contents are missing")

            content1_lines = content1.splitlines()
            content2_lines = content2.splitlines()

            diff = list(difflib.unified_diff(
                content1_lines, content2_lines,
                fromfile=f"a/{filename}", tofile=f"b/{filename}",
                lineterm=""
            ))

            return "\n".join(diff) if diff else None  # Avoid empty diffs
        except Exception as e:
            raise Exception(f"Error: Failed to compute difference - {e}")

    def diff(self, commit_hash): # Feature to display the difference between two commits
        try:
            if not commit_hash:
                raise ValueError("Error: Commit hash is missing")
            current_commit_content = self.read_commit_data(commit_hash)
            if not current_commit_content:
                raise ValueError("Error: Failed to read commit data")

            parent_commit_hash = current_commit_content["parent"]
            if not parent_commit_hash:
                print("This is the first commit. No parent commit found.")
                return
            parent_commit_content = self.read_commit_data(parent_commit_hash)
            if not parent_commit_content:
                raise ValueError("Error: Failed to read parent commit data")

            current_files = current_commit_content["files"]
            parent_files = parent_commit_content["files"]

            diff_output = []
            diff_output.append(f"These are the files changed in this {commit_hash}:")

            # Compare existing files
            for filename in current_files:
                current_file_hash = current_files[filename]
                parent_file_hash = parent_files.get(filename)

                if parent_file_hash:  # File exists in both commits
                    parent_file_content = self.get_file_content(parent_file_hash)
                    current_file_content = self.get_file_content(current_file_hash)

                    file_diff = self.compute_difference(parent_file_content, current_file_content, filename)
                    if file_diff:
                        diff_output.append(f"\ndiff --mygit {filename}")
                        diff_output.append(file_diff)

                else:  # New file added
                    diff_output.append(f"\ndiff --mygit {filename}")
                    diff_output.append("New file added")
                    diff_output.append(f"+++ b/{filename}")
                    new_file_content = self.get_file_content(current_file_hash)
                    diff_output.extend([f"+{line}" for line in new_file_content.splitlines()])

            # Check for deleted files
            for filename in parent_files:
                if filename not in current_files:
                    diff_output.append(f"\ndiff --git {filename}")
                    diff_output.append("File Has been deleted")
                    diff_output.append(f"--- a/{filename}")
                    deleted_file_content = self.get_file_content(parent_files[filename])
                    diff_output.extend([f"-{line}" for line in deleted_file_content.splitlines()])

            print("\n".join(diff_output) if diff_output else "No changes detected.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    mygit = MyGit()
    # mygit.init()
    # mygit.add("sample.txt")
    # mygit.commit("1st commit")
    # mygit.log()
    # mygit.diff("Commit_hash")
