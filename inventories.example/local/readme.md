
Once again, the `inventories` directory should never be pushed on a public or a private repo!

To provision `production` || `staging` || `test` || ... environemnts, you can just copy and paste `local` directory content inside them.


#### Way's to define your hosts file

You can cutomize as you want the `hosts` file 

---

Simple format (I trully recommend  to use SSH keys)

```bash
[webservers]
192.168.56.155
192.168.56.200

[database-srv]
192.168.56.201
192.168.56.202
your.sub.domain.com

[all:children]
webservers
database-srv

[local]
127.0.0.1 ansible_connection=local
```

---

Format with credentials (You can encrypt it with vault, it will still work)
```bash
[webservers]
192.168.56.155 ansible_user=vagrant ansible_ssh_pass=vagrant ansible_port=22 
192.168.56.200 ansible_user=vagrant ansible_ssh_pass=vagrant ansible_port=22 

[database-srv]
192.168.56.201 ansible_user=vagrant ansible_ssh_pass=vagrant ansible_port=22 
192.168.56.202 ansible_user=vagrant ansible_ssh_pass=vagrant ansible_port=22 
your.sub.domain.com ansible_user=srv_username ansible_ssh_pass=password ansible_port=22 

[all:children]
webservers
database-srv

; This is require if you need to run some playbook on the Node Controller(s)
;[local]
;127.0.0.1 ansible_connection=local
```

or (if all your **lab** VM shared have the same credentials || the same SSH Keys)

```bash
192.168.56.155
192.168.56.200

[database-srv]
192.168.56.201
192.168.56.202

[all:children]
webservers
database-srv

[all:vars]
ansible_user=username
ansible_ssh_pass=vagrant
ansible_ssh_common_args='-o StrictHostKeyChecking=no'

;[local]
;127.0.0.1 ansible_connection=local
```

---

format

```bash

```
