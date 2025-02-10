"""Computes the current and the next states based on the divisor value.
"""
from fsm import FSM

def compute_states(number : int):

    """
    The compute states function computes a dictionary of current states -> next transition state value.
    The next state is obtained using the formula
    S(i+1) = (2*current_remainder + bit (0/1)) % number
    """


    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    if number <= 0:
        raise ValueError("Number must be greater than zero.")
    
    state_transitions={}
    bits=[0, 1]
    for current_remainder in range(number):
        current_state = f'S{current_remainder}'
        for bit in bits:
            next_state = (2 * current_remainder + bit) % number
            next_state = f'S{next_state}'
            state_transitions[(current_state, bit)] = next_state

    print(state_transitions)
    return state_transitions

def compute_remainder(binary_number, number):

    """
    Calculate the state schema to compute the current state and the next states as per modulo number.
    Create an FSM class object to initialize the FSM Algorithm
    Retrueve the final state and its respective remainder after parsing all the bits in the binary number (left to right)
    """    

    if not binary_number:
        raise ValueError("Empty Binary String not acceptable. Please provide correct binary input")
    
    for c in binary_number:
        if c not in {'0', '1'}:
            raise ValueError(f"Invalid Binary String {binary_number}. The input is not a Binary String. A binary string only comprises of 0s ans 1s")
        
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Modulus number must be a positive integer.")

    if number == 1:
        return 0
    
    state_schema = compute_states(number)
    initial_state = 'S0'
    print(f"Starting from initial state : {initial_state}")
    fsm = FSM(initial_state = initial_state, transitions = state_schema)
    final_state = fsm.process_number(binary_input = binary_number)
    final_remainder = int(final_state[1:])
    return final_remainder