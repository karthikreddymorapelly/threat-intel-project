import sqlite3

print("=== Threat Intelligence Feed Processor ===")

# Step 1: Create a small database to store bad IPs
conn = sqlite3.connect("threat_intel.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS bad_ips (ip TEXT PRIMARY KEY, reason TEXT)")
conn.commit()

# Step 2: Add some fake bad IPs (like a blacklist)
bad_list = [("185.191.171.12", "Phishing"), ("206.189.123.45", "Malware")]
for ip, reason in bad_list:
    cur.execute("INSERT OR IGNORE INTO bad_ips VALUES (?, ?)", (ip, reason))
conn.commit()

# Step 3: Create a fake log file (like internet connections)
with open("access.log", "w") as f:
    f.write("192.168.1.1\n")
    f.write("185.191.171.12\n")
    f.write("8.8.8.8\n")
    f.write("206.189.123.45\n")

print("Fake log file created: access.log")

# Step 4: Read the log and check for bad IPs
with open("access.log", "r") as f:
    for line in f:
        ip = line.strip()
        cur.execute("SELECT * FROM bad_ips WHERE ip=?", (ip,))
        result = cur.fetchone()
        if result:
            print(f"[ALERT] Bad IP found: {ip} ({result[1]})")
        else:
            print(f"[OK] Safe IP: {ip}")

conn.close()
print("=== Done ===")
