# Web Stack Debugging Project

## Description
This project is focused on enhancing the performance and stability of a web server setup featuring Nginx on Ubuntu 14.04 LTS. The tasks involve debugging, optimizing configurations, and ensuring that the server can handle a high load without failing requests. Additionally, the project includes modifying OS settings to resolve file limit issues encountered by specific users.

## Requirements
- **Operating System**: Ubuntu 14.04 LTS
- **Puppet Version**: v3.4
- **Puppet-lint Version**: 2.1.1
- All Puppet manifests must:
  - Pass `puppet-lint` without errors.
  - Execute without errors.
  - Begin with a comment explaining the purpose.
  - End with a `.pp` file extension.

## Installation
To get started, install the necessary tools:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
# Web Stack Debugging Project

## Description
This project is focused on enhancing the performance and stability of a web server setup featuring Nginx on Ubuntu 14.04 LTS. The tasks involve debugging, optimizing configurations, and ensuring that the server can handle a high load without failing requests. Additionally, the project includes modifying OS settings to resolve file limit issues encountered by specific users.

## Requirements
- **Operating System**: Ubuntu 14.04 LTS
- **Puppet Version**: v3.4
- **Puppet-lint Version**: 2.1.1
- All Puppet manifests must:
  - Pass `puppet-lint` without errors.
  - Execute without errors.
  - Begin with a comment explaining the purpose.
  - End with a `.pp` file extension.

## Installation
To get started, install the necessary tools:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
## Tasks

### 1. Sky is the Limit
- **Objective**: Optimize Nginx to handle 2000 requests with zero failures.
- **Tool**: ApacheBench for benchmarking.
- **File**: `0-the_sky_is_the_limit_not.pp`

### 2. User Limit
- **Objective**: Adjust OS configurations to prevent "Too many open files" errors when logging in as a specific user.
- **File**: `1-user_limit.pp`

## Usage
Apply the Puppet manifests to configure the server:
```bash
$ puppet apply 0-the_sky_is_the_limit_not.pp
$ puppet apply 1-user_limit.pp

