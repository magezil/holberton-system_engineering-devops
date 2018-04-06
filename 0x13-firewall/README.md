# 0x13-firewall

## Firewall
### 0-firewall_ABC
* File contains answers to questions:
  * What is a firewall? A hardware or software security system - 2
  * What are the 2 types of firewalls? Network and host-based firewall - 3
  * What is the main function of a firewall? To filter incoming and outgoing network traffic - 1

### 1-block_all_incoming_traffic_but
* ufw commands to setup firewall to block all incoming traffic except ports 22 (SSH), 443 (HTTPS SSL), 80 (HTTP)

### 100-port_forwarding
* Copy of `ufw` configuration file modified to allow redirect from port `8080` to `80`

