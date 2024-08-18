# 0x0C. Web Server

## Overview

This project involves setting up and configuring an Nginx web server on an Ubuntu machine. The tasks include file transfer, server installation, DNS setup, implementing redirects, creating custom error pages, and automating server configuration using Puppet.

## Requirements

- **Editors**: `vi`, `vim`, `emacs`
- **Operating System**: Ubuntu 16.04 LTS
- **Bash Scripts**:
  - Must start with `#!/usr/bin/env bash`
  - The second line must describe the script's purpose
  - Must pass Shellcheck (version 0.3.7) without any errors
  - Must be executable

## Tasks

### 0. Transfer a File to Your Server
A Bash script to securely transfer a file to a remote server using SCP.

### 1. Install Nginx Web Server
A script to install and configure Nginx on an Ubuntu machine to serve a "Hello World!" page.

### 2. Setup a Domain Name
Register a `.tech` domain and configure DNS to point to your Nginx server.

### 3. Redirection
Configure Nginx to perform a 301 redirect from `/redirect_me` to a specified URL.

### 4. Custom 404 Error Page
Create a custom 404 error page in Nginx with the message "Ceci n'est pas une page."

### 5. Install Nginx Web Server with Puppet
Use Puppet to install and configure Nginx, including a 301 redirect.

## Repository Structure

- **GitHub repository**: `alx-system_engineering-devops`
- **Directory**: `0x0C-web_server`
- **Files**:
  - `0-transfer_file`
  - `1-install_nginx_web_server`
  - `2-setup_a_domain_name`
  - `3-redirection`
  - `4-not_found_page_404`
  - `7-puppet_install_nginx_web_server.pp`

## Important Notice

You must complete the tasks independently. Plagiarism is strictly prohibited and will lead to removal from the program. Do not publish any content from this project.

