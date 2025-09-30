**Goals of this script:**

- add Managed Node (MN) IPs to the Control Node's (CN’s) `known_hosts` file
- copy the Control Node (CN) SSH public key to each Managed Node (MN)

To run it:

```bash
cd ./scripts

# create the .env file and update it
cp .env.example .env

# The -B flag disables bytecode cache (.pyc files), so no cache files will be generated.
python3 -B copy_ssh_keys_to_srvs.py
```