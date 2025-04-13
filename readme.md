The `inventory` directory contain all the Managed Nodes and some critical data. **So never, ever push it on a public/private repo!**

Command to run a playbook

```bash
 ansible-playbook -i inventories/local -u vagrant --ask-pass playbook.yml 
```

Run playbook with secret
```bash
 ansible-playbook -i hosts.ini playbooks.yaml -u vagrant --vault-password-file='/path/to/vault/file'
```

---

#### How to deal with secret

*If you need to publish your playbooks on a repo (private||public), never ever push it with your `inventories` directory!*

Talking about secrets, they are dozen of method available to protect secrets and avoid unauthorize access to them. Solution's like, `Ansible Vault`, `Github Action Secrets`, `AWS Secrets Manager`, ... are design to fit your needs and protect sensitive informations needed by your playbook

Here is a little tuto on Ansible Vault 

```bash

# Create your ~/path/to/your/.vaultSecret file and type your password inside it
 vi ~/path/to/your/.vaultSecret

# Encrypt your sensitive inventories files
 ansible-vault encrypt ./inventories/production/group_vars/all.yml --vault-password-file=~/path/to/your/.vaultSecret

# To embarc your vault password in your playbooks running process, you have to add a parameter in your ansible-playbook command like this
 ansible-playbook -i inventories/local -u vagrant app-deployment-playbook.yaml --vault-password-file=.vaultFile

 # Or if you want to manually type the vault password
 ansible-playbook -i inventories/local -u vagrant app-deployment-playbook.yaml --ask-vault-password 

```




---


Reference:

https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html

https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html