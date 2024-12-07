#!/usr/bin/env python3

import os

def audit_directory(directory):
    total_size = 0

    try:
        # List all entries in the directory
        entries = os.listdir(directory)
    except PermissionError:
        print(f"Error: Permission denied while accessing {directory}.")
        return
    except FileNotFoundError:
        print(f"Error: Directory {directory} not found.")
        return

    print(f"Audit Report for Directory: {directory}")
    print("=" * 50)

    for entry in entries:
        entry_path = os.path.join(directory, entry)

        # Check if the entry is a regular file
        if os.path.isfile(entry_path):
            try:
                # Get the file size
                file_size = os.path.getsize(entry_path)
                total_size += file_size
                print(f"File: {entry}, Size: {file_size} bytes")
            except PermissionError:
                print(f"Error: Permission denied for file {entry}.")
            except FileNotFoundError:
                print(f"Error: File {entry} not found.")

    print("=" * 50)
    print(f"Total Size of Regular Files: {total_size} bytes")
    print("Audit Completed.")

def main():
    # Define the directory to audit
    directory_to_audit = "/etc"
    audit_directory(directory_to_audit)

if __name__ == "__main__":
    main()
