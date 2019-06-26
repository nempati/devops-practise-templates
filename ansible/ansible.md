#installing ansible in C M server
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

#insatlling python2.7  in nodes 
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install pyhton

#adding user and passwd  inall machines 
adduser ansible
passwd ansible

#enabling passwd authentications in all machines
sudo vi /etc/ssh/sshd.config
passwordauthentication:yes


#giving root previligaes to ansible in all machines
sudo  #(become root user)
visudo
ansible (ALL)=(ALL) NOPASSWD:ALL

#gen ssh key in C M server
ssh-keygen

#copy this key into nodes

ssh-copy-id ansible@DNS_of_host
#by this above process we enable passwd less authentication
#for ansible to login from C M server to nodes

ssh ansible@hostname 

#by the above coomand CM machine logins into nodes with out
#passwd this is to  verify from us manually

# Inventory
it is located in /etc/ansible/hosts    in CM server 

this hosts file is the inventory for us to add DNS host names for ansible service to communicate with nodes 

