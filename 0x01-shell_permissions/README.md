#0x01-shell_permissions
0-iam_betty changes user ID to betty
1-who_am_i prints effective current user ID
2-groups prints all groups current user is part of
3-new_owner changes owner of *hello* to *betty*
4-empty creates empty file *hello*
5-execute adds permission for owner of *hello* to execute
6-multiple_permissions adds execute permission to owner and group owner and read permission for other users to file *hello*
7-everybody adds execute permission to everyone (owner, group owner, and other users) to file *hello*
8-James_Bond sets no permissions to owner and group owner and all permissions to other users to file *hello*
9-John_Doe sets mode of file *hello* to all permissions for owner, read and execute for group owner, and write and execute for other users
10-mirror_permissions sets the mode of file *hello* to the same as *olleh*
11-directories_permissions adds execute permission to all subdirectories of the current directory for owner, group owner, and other users without changing regular files
12-directory_permissions - creates directory *dir_holberton* with permissions 751
13-change_group - changes group owner of file *hello* to *holberton*
14-change_owner_and_group changes the owner to *betty* and group owner to *holberton* for all files and directories in current directory
15-symbolic_link_permissions changes owner and group owner of *_hello* to betty:holberton
16-if_only changes owner of file *hello* to *betty* only if current owner is *guillaume*
