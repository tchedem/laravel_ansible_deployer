def displayConnectionCommand( ips, usernames ) :

    for i in range(len(ips)) :

        print(" ssh " + usernames[i] + "@" + ips[i])

# ssh -vvv vagrant@192.168.56.155
# Authenticate without using public key:
# ssh -o PubkeyAuthentication=no vagrant@192.168.56.155
# ssh -o IdentitiesOnly=yes -o PubkeyAuthentication=no vagrant@192.168.56.155

# Disable all added keys in the ssh-agent:
# ssh-add -D

