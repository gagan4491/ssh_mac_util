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
    parser = argparse.ArgumentParser(description="Open iTerm2 and SSH to a host.")
    parser.add_argument("host", help="The host to SSH into")
    args = parser.parse_args()
    open_iterm2(args.host)
