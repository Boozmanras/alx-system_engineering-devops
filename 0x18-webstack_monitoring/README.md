# 0x18. Webstack Monitoring

## Project Overview

This project focuses on setting up monitoring for web servers using Datadog. Monitoring is an essential aspect of maintaining a robust and scalable infrastructure, as it allows you to track key metrics, identify potential issues, and ensure that your services are running smoothly.

## Requirements

- **Editors**: vi, vim, emacs
- **Operating System**: Ubuntu 16.04 LTS
- **File Standards**:
  - All files must end with a new line.
  - A `README.md` file at the root of the project directory is mandatory.
  - All Bash scripts must be executable.
  - Bash scripts must pass Shellcheck (version 0.3.7) without any errors.
  - The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
  - The second line of all Bash scripts should be a comment explaining the script's purpose.

## Servers

| Name           | Username | IP            | State   |
| -------------- | -------- | ------------- | ------- |
| 439444-web-01  | ubuntu   | 54.144.84.8   | running |
| 439444-web-02  | ubuntu   | 34.227.92.37  | running |
| 439444-lb-01   | ubuntu   | 54.89.181.81  | running |

## Tasks

### 0. Sign up for Datadog and install datadog-agent

- Sign up for a free Datadog account at [Datadog US website](https://app.datadoghq.com).
- Use the US1 region during sign-up.
- Install the Datadog agent on `web-01`.
- Create an application key and copy-paste your DataDog API key and application key into your Intranet user profile.
- Ensure that `web-01` is visible in Datadog under the hostname `XX-web-01`.
- Validate your setup using the Datadog API if needed.

**Repo**:
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x18-webstack_monitoring`

### 1. Monitor some metrics

- Set up monitors within the Datadog dashboard to monitor the following:
  - Number of read requests issued to the device per second.
  - Number of write requests issued to the device per second.

**Repo**:
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x18-webstack_monitoring`

### 2. Create a dashboard

- Create a new dashboard in Datadog with at least four widgets that monitor various metrics of your choice.
- Create the file `2-setup_datadog`, containing the `dashboard_id` on the first line.

**Repo**:
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x18-webstack_monitoring`
- File: `2-setup_datadog`

## Conclusion

This project emphasizes the importance of monitoring in maintaining the health of web servers. By setting up Datadog monitoring, you gain insights into your infrastructure's performance and can proactively address potential issues before they impact your users.

