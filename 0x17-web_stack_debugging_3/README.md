# 0x17. Web Stack Debugging #3

## Project Overview
This project focuses on using `strace` to diagnose and fix a 500 Internal Server Error caused by Apache. After identifying the issue using `strace`, the fix is automated using Puppet, ensuring that the server runs smoothly without manual intervention.

## Requirements
- **Operating System:** Ubuntu 14.04 LTS
- **Puppet Version:** Puppet v3.4
- **Puppet-lint Version:** 2.1.1

## Tasks

### 0. Strace is Your Friend
Using `strace`, identify the root cause of a 500 Internal Server Error returned by Apache. Once the issue is identified, automate the fix using Puppet. The solution must meet the following criteria:
- The fix must be implemented in a Puppet manifest file named `0-strace_is_your_friend.pp`.
- The Puppet manifest must pass `puppet-lint` with no errors.
- The Puppet manifest must execute without any errors.

## Installation and Setup
1. **Install Puppet-lint:**
   ```bash
   apt-get install -y ruby
   gem install puppet-lint -v 2.1.1

