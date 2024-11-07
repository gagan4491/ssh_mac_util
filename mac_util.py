#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import argparse

def open_iterm2(host):
    # Define AppleScript in one go with straightforward syntax
    apple_script = f'''
    tell application "iTerm2"
        create window with default profile
        tell current session of current window
            write text "ssh {host}"
        end tell
        activate
    end tell
    '''

    try:
        subprocess.run(["osascript", "-e", apple_script], check=True)
        print(f"iTerm2 opened successfully and SSH to {host} initiated.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open an SSH session.")
    parser.add_argument('selected_text', nargs='?', default=None, help='The selected text to open SSH session for')
    args = parser.parse_args()

    if args.selected_text:
        # Get the IP or hostname before the slash if needed
        final_host = str(args.selected_text.split('/')[0]).strip()
        # print(final_host)
        open_iterm2(final_host)
    else:
        print("Please provide the selected text to open an SSH session.")
