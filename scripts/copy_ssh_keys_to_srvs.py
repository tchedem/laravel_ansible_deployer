import os, shlex, sys
from dotenv import load_dotenv
from functions import displayConnectionCommand

load_dotenv()

home_dir = os.getenv("HOME_DIR", "/home/tchedem")

ips = []
usernames = []

# Read SRV count from env
srv_count = int(os.getenv("SRV_COUNT", 0))

SRVs = {}

# Build SRVs dictionary dynamically
for i in range(srv_count):

    srv_key = f"SRV{i}"

    SRVs[srv_key] = {
        "ip": os.getenv(f"{srv_key}_IP"),
        "ssh_port": os.getenv(f"{srv_key}_SSH_PORT", "22"),
        "username": os.getenv(f"{srv_key}_USERNAME"),
        "password": shlex.quote(os.getenv(f"{srv_key}_PASSWORD")),
        "ssh_key_path": os.path.join(home_dir, os.getenv(f"{srv_key}_SSH_KEY_PATH", ".ssh/personal_ansible_key")),
        "ssh_key_passphrase": os.getenv(f"{srv_key}_SSH_KEY_PASSPHRASE", "")
    }

# Run commands to copy SSH keys to each server
# You need to have sshpass installed for this to work
# sudo apt-get install sshpass
for srvKey, srvData in SRVs.items():

    ip = srvData["ip"]
    ssh_port = srvData["ssh_port"]
    username = srvData["username"]
    password = srvData["password"]
    ssh_key_path = srvData["ssh_key_path"]

    ips.append(ip)
    usernames.append(username)

    print(f"{srvKey}\n")
    print("Remove existing SSH keys...\n\n")

    os.system(f"ssh-keygen -f {home_dir}/.ssh/known_hosts -R {ip} && ssh-keyscan -p {ssh_port} {ip} >> {home_dir}/.ssh/known_hosts")

    command = f"sshpass -p {password} ssh-copy-id -i {ssh_key_path} -p {ssh_port} {username}@{ip}"
    os.system(command)

    print("\n\n")

# Return ssh connection command for each server
displayConnectionCommand(ips, usernames)
