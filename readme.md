#### Create your project with this repo

```bash
git clone git@github.com:tchedem/ansible-quick-starter.git {project_name}
```


The `inventory` directory contain all the Control Nodes.

Command to start the project

```bash
 ansible-playbook -i inventories/local -u tchedem --ask-pass playbook.yml 
```


---


Reference:

https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html

https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html