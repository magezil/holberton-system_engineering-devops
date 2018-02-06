# 0x05-processes_and_signals

## Processes and signals
### 0-what-is-my-pid
* This script displays its PID

### 1-list_your_processes
* This script displays a list of currently running processes in a user-oriented format

### 2-show_your_bash_pid
* This script displays the line containing the word `bash`

### 3-show_your_bash_pid_made_easy
* This script displays the PID and process name of processes with the word `bash`

### 4-to_infinity_and_beyond
* This script writes `To infinity and beyond` indefinitely

### 5-kill_me_now
* kill the 4-to_infinity_and_beyond process

### 6-kill_me_now_made_easy
* This script kills 4-to_infinity_and_beyond

### 7-highlander
* This script displays `I am invincible!!!` when receiving a SIGTERM signal
### 8-beheaded_process
* This script kills the process 7-highlander

### 100-process_and_pid_file
* This script creates a file with its pid, displays `To infinity and beyond` indefinitely
  * Displays `I hate the kill command` when receive a SIGTERM
  * Displays `Y U no love me?!" when get SIGINT
  * Deletes file with pid when receive a SIGQUIT or SIGTERM signal
* Usage: `sudo ./100-process_and_pid_file`
### 101-manage_my_process
* This script manages daemon `manage_my_process`

