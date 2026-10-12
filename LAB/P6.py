def vacuum_cleaner():
    # 1 = Dirty, 0 = Clean
    rooms = {'A': 1, 'B': 1}
    current_room = 'A'
    
    print(f"Initial State: {rooms}")
    
    for _ in range(2): # Check both rooms
        print(f"Vacuum is in Room {current_room}")
        if rooms[current_room] == 1:
            print(f"Room {current_room} is Dirty. Cleaning...")
            rooms[current_room] = 0
            print(f"Room {current_room} is now Clean.")
        else:
            print(f"Room {current_room} is already Clean.")
            
        # Move to the other room
        current_room = 'B' if current_room == 'A' else 'A'
        print("Moving to Room", current_room)
        
    print(f"Final State: {rooms}")

vacuum_cleaner()
