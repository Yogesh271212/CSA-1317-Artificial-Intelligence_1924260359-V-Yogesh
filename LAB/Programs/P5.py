from collections import deque

def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    return True

def get_successors(state):
    m_left, c_left, b_pos, m_right, c_right = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []
    
    for m, c in moves:
        if b_pos == 'left':
            new_state = (m_left - m, c_left - c, 'right', m_right + m, c_right + c)
        else:
            new_state = (m_left + m, c_left + c, 'left', m_right - m, c_right - c)
            
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def solve_missionaries_cannibals():
    initial_state = (3, 3, 'left', 0, 0)
    goal_state = (0, 0, 'right', 3, 3)
    
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            for step in path + [current_state]:
                print(step)
            return
            
        for next_state in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

solve_missionaries_cannibals()
