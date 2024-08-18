# 0x0C-web_server

## Project Overview
This project involves setting up a web server, transferring files, and configuring a domain name. The tasks include automating these processes using Bash scripts.

## Tasks

### 0. Transfer a File to Your Server
This script transfers a file from the client machine to the server using `scp`. It accepts four parameters: the file path, server IP, username, and the SSH private key path.

### 1. Install Nginx Web Server
This script installs Nginx on the server and configures it to return "Hello World!" when queried at the root (`/`) path.

### 2. Setup a Domain Name
This task involves registering a `.tech` domain, setting up DNS records, and ensuring the domain points to the server's IP address.

## Usage Instructions

### 0. Transfer a File
```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY

