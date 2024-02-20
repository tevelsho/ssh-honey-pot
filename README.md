This Python script sets up an SSH honeypot to capture credentials of attackers attempting to log into an SSH server. It uses the Paramiko library to create a fake SSH server that accepts connections and logs login attempts.

Modules Used

    socket: Used for socket programming to create a server socket.
    paramiko: Used for SSH server implementation.

Usage

    Generate SSH Key:
    Generate an SSH key using ssh-keygen command and save the private key in a file (e.g., key).

    Run the Script:
    python ssh_honeypot.py

Connect to the Honeypot:

    Use an SSH client to connect to the honeypot on port 2222.
    Username and password combinations used by the attacker will be printed to the console.

Example Output:

    attackerName:password123
