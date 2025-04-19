import sqlite3
conn = sqlite3.connect('logistics.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS shipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    receiver TEXT NOT NULL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    status TEXT NOT NULL
)
''')
conn.commit()

def add_shipment():
    sender = input("Sender Name: ")
    receiver = input("Receiver Name: ")
    origin = input("Origin: ")
    destination = input("Destination: ")
    status = "In Transit"
    cursor.execute("INSERT INTO shipments (sender, receiver, origin, destination, status) VALUES (?, ?, ?, ?, ?)",
                   (sender, receiver, origin, destination, status))
    conn.commit()
    print("Shipment Added Successfully!\n")

def update_status():
    shipment_id = input("Enter Shipment ID to update: ")
    new_status = input("Enter New Status (e.g., Delivered, Delayed): ")
    cursor.execute("UPDATE shipments SET status = ? WHERE id = ?", (new_status, shipment_id))
    conn.commit()
    print("Status Updated!\n")

def track_shipment():
    shipment_id = input("Enter Shipment ID to track: ")
    cursor.execute("SELECT * FROM shipments WHERE id = ?", (shipment_id,))
    result = cursor.fetchone()
    if result:
        print(f"\nShipment ID: {result[0]}")
        print(f"Sender: {result[1]}")
        print(f"Receiver: {result[2]}")
        print(f"Origin: {result[3]}")
        print(f"Destination: {result[4]}")
        print(f"Status: {result[5]}\n")
    else:
        print("Shipment not found.\n")

def view_all_shipments():
    cursor.execute("SELECT * FROM shipments")
    rows = cursor.fetchall()
    if rows:
        print("\nAll Shipments:")
        for row in rows:
            print(row)
        print()
    else:
        print("No shipments found.\n")

def main():
    while True:
        print("==== Logistics Management System ====")
        print("1. Add Shipment")
        print("2. Update Status")
        print("3. Track Shipment")
        print("4. View All Shipments")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_shipment()
        elif choice == '2':
            update_status()
        elif choice == '3':
            track_shipment()
        elif choice == '4':
            view_all_shipments()
        elif choice == '5':
            print("Exiting Bro😎... Goodbye!")
            break
        else:
            print("Invalid Option. Try Again.\n")

if __name__ == "__main__":
    main()
    conn.close()
