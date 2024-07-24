# Firewall Configuration Projects

This repository contains two projects related to configuring firewalls using UFW (Uncomplicated Firewall) on web servers.

## Project 1: Block All Incoming Traffic Except Specific Ports

### Description
This project involves installing and configuring the UFW firewall on web-01 to block all incoming traffic except for specific TCP ports.

### Requirements
- Configure UFW on web-01
- Block all incoming traffic except:
  - Port 22 (SSH)
  - Port 443 (HTTPS SSL)
  - Port 80 (HTTP)

### Implementation
The UFW commands used to set up the firewall are provided in the answer file.

## Project 2: Port Forwarding

### Description
This advanced project demonstrates how to configure a firewall to forward requests from one port to another.

### Requirements
- Configure web-01 to redirect port 8080/TCP to port 80/TCP
- Modify the UFW configuration file to implement port forwarding

### Implementation
- The modified UFW configuration file is provided in the answer file
- The setup redirects requests from port 8080 to port 80, where the Nginx web server is listening

### Verification
- Use `netstat` to confirm that Nginx is listening on port 80
- Use `curl` to test that requests to both port 80 and port 8080 return a HTTP 200 response

## Files
- `0-block_all_incoming_traffic_but`: Contains UFW commands for Project 1
- `100-port_forwarding`: Contains the modified UFW configuration for Project 2

## Note
These projects were implemented on Ubuntu servers running Nginx. The configurations may need adjustments for different environments or server setups.
