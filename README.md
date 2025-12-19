### Laravel Ansible Deployer

A full Laravel deployment solution built with Ansible, bootstraped-from [ansible-quick-starter](https://github.com/tchedem/ansible-quick-starter).

This repository helps you quickly provision and deploy a Laravel application with best practices for automation and repeatability.

It’s designed to make deployment on on-premise or VM-based environments simple and efficient.

NB: The project don't integrate `SSL/TLS`

### Project Structure

`main_playbook.yml` is the entry point of project! 
`playbooks/` contain Ansible playbooks for provisioning and deployment
`roles/` Modular roles for different parts of the stack
`vagrant/` Local test environment (Vagrant + VirtualBox). (NB: You can use any Hypervisor)
`reference/` *have some a manual process ofdeployment of the solution! It's no-more updated! But I left it to share the importance of doing things manually at least once!*

### Roles Overview

Each role is a building block of the deployment process:

- `common` : updates system packages, installs common utilities (git, curl, unzip, etc.)
- `php8.1 or php8.2` : installed any version of php with required extensions on your hosts
- `composer` installed the mytic PHP package manager
- `nginx` installed the NGINX webserver/proxy used to serve content
- `mariadb` installed a relationnal database to store and persist our apps data
- `redis` installed and setup the in memory database use to perform caching and queues jobs
- `deploy-laravel-app` use to deploy the laravel project


### How to use it ?

1. Clone the project
```bash
git clone https://github.com/tchedem/laravel_ansible_deployer.git
cd laravel_ansible_deployer
```

2. Initialize inventory (*optional*)
```bash
mv inventories.example inventories
```


> If you want to use `vagrant` to test the playbook in a controlled environment
```bash
# Make sure you have vagrant installed
cd vagrant
vagrant up

# get SSH keys instructions
cd ../scripts
cat README.md
```

3. Start cooking from your Control Node (CN)
```bash
# ansible-playbook -i inventories/test main_playbook.yml -u <your_username>
ansible-playbook -i inventories/local main_playbook.yml -u vagrant # If you are using vagrant
```