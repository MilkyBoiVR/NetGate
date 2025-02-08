import subprocess
import os

def block_internet(process_path):
    """Blocks a specific process from accessing the internet."""
    if not os.path.exists(process_path):
        print(f"Error: The file '{process_path}' does not exist.")
        return

    rule_name = f"Block_{os.path.basename(process_path)}"
    cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=out program="{process_path}" action=block'

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Blocked internet access for {process_path}.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to block {process_path}: {e}")

def unblock_internet(process_path):
    """Unblocks a specific process from the internet."""
    rule_name = f"Block_{os.path.basename(process_path)}"
    cmd = f'netsh advfirewall firewall delete rule name="{rule_name}"'

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Restored internet access for {process_path}.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to unblock {process_path}: {e}")

if __name__ == "__main__":
    process = input("Enter the full path of the game/process executable: ").strip()

    if process.startswith('"') and process.endswith('"'):
        process = process[1:-1]

    action = input("Do you want to (b)lock or (u)nblock the internet for this process? ").strip().lower()

    if action == 'b':
        block_internet(process)
    elif action == 'u':
        unblock_internet(process)
    else:
        print("Invalid choice.")
