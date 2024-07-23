# Web Stack Debugging 2

This project focuses on system engineering and web stack debugging tasks using Bash scripts. The tasks aim to improve the security and efficiency of running services and commands in a Linux environment. All scripts are developed and tested on Ubuntu 20.04 LTS.

## Requirements

- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any errors
- Bash scripts must run without errors
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Tasks

1. **Run software as another user:** Write a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument.
2. **Run Nginx as Nginx:** Configure Nginx to run as the `nginx` user and listen on all active IPs on port 8080.
3. **7 lines or less:** Condense the script from Task 2 into 7 lines or fewer without using `;`, `&&`, or executing the previous script.
