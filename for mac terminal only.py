#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import argparse

def open_ssh_session(host):
    apple_script = f'''
    tell application "Terminal"
        do script "ssh {host}"
        activate
    end tell
    '''
    # Use subprocess to execute the AppleScript
    subprocess.run(["osascript", "-e", apple_script])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open an SSH session.")
    parser.add_argument('selected_text', nargs='?', default=None, help='The selected text to open SSH session for')
    args = parser.parse_args()

    if args.selected_text:
        # Get the IP or hostname before the slash if needed
        final_host = str(args.selected_text.split('/')[0]).strip()
        print(final_host)
        open_ssh_session(final_host)
    else:
        print("Please provide the selected text to open an SSH session.")
