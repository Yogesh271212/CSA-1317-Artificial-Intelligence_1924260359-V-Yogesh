class HospitalState:
    def __init__(self, current_location, path_cost=0):
        self.current_location = current_location
        self.path_cost = path_cost

    def get_successors(self, graph):
        return graph.get(self.current_location, {})
        
    def is_goal(self, target_ward):
        return self.current_location == target_ward

hospital_map = {
    'Pharmacy': {'Junction A': 2, 'Junction B': 5},
    'Junction A': {'Pharmacy': 2, 'Ward 1': 3, 'Lift Lobby': 1},
    'Junction B': {'Pharmacy': 5, 'Ward 2': 4},
    'Lift Lobby': {'Junction A': 1, 'Ward 3': 2},
    'Ward 1': {'Junction A': 3},
    'Ward 2': {'Junction B': 4},
    'Ward 3': {'Lift Lobby': 2}
}

start_state = HospitalState('Pharmacy')
print(f"Initial State: {start_state.current_location}")
print(f"Goal Check (Ward 3): {start_state.is_goal('Ward 3')}")
print(f"Successors from Pharmacy: {start_state.get_successors(hospital_map)}")

next_loc = 'Junction A'
print(f"\nMoving to {next_loc}...")
current_state = HospitalState(next_loc, 2)
print(f"Current State: {current_state.current_location}")
print(f"Successors from {next_loc}: {current_state.get_successors(hospital_map)}")
