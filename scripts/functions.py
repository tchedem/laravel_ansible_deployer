def displayConnectionCommand( ips, usernames ) :

    for i in range(len(ips)) :

        print(" ssh " + usernames[i] + "@" + ips[i])