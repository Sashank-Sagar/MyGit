#!/usr/bin/env python3
import argparse
from MyGit import MyGit # MyGit Class is in MyGit.py file


VERSION = "0.0.1"

def main():
    parser = argparse.ArgumentParser(prog = "mygit", description = "My custom git (Simplified Version 0)")
    parser.add_argument("--version",action = "version", version = f"MyGit version {VERSION}" )

    subparsers = parser.add_subparsers(dest = "command", help = "Commands")

    # init command
    subparsers.add_parser("init", help = "Initialize a MyGit Repository")

    # add command
    add_parser = subparsers.add_parser("add", help="Add files in staging area")
    add_parser.add_argument("files", nargs = "+", help ="Files to add")

    # commit command
    commit_parser = subparsers.add_parser("commit", help = "Commit Changes")
    commit_parser.add_argument("-m", "--message", required = True, help = "Commit Message")

    # log command
    log_parser = subparsers.add_parser("log", help = "Show Commit History")

    # diff command
    diff_parser = subparsers.add_parser("diff", help = "Show Difference")
    diff_parser.add_argument("commit_hash",nargs = "?" , help = "Pass commit_hash to get differnce")

    args = parser.parse_args()

    repo = MyGit()

    if args.command == "init":
        repo.init()
    elif args.command == "add":
        for file in args.files:
            repo.add(file)
    elif args.command == "commit":
        repo.commit(args.message)
    elif args.command == "log":
        repo.log()
    elif args.command == "diff":
        repo.diff(args.commit_hash)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
