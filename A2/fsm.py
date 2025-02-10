"""
The FSM Class has the following functionality:
- Implements a Finite State Machine (FSM) to process binary inputs.
- Transitions between states based on predefined rules.
- Raises an error if an undefined transition is encountered.
- The process function processes the current and the transition states and returns the Final remainder to compute_states function
"""
class FSM:

    def __init__(self, initial_state: str, transitions: dict[tuple[str, str], str]):


        if not isinstance(initial_state, str):
            raise TypeError("Initial state must be a string.")
        if not isinstance(transitions, dict):
            raise TypeError("Transitions must be a dictionary.")
    
        self.current_state = initial_state
        self.transitions = transitions

    def find_transition(self, input_digit):

        if input_digit not in (0, 1):
            raise ValueError(f"Invalid input: {input_digit}. Only binary digits (0 and 1) are allowed.")

        current_key = (self.current_state, input_digit)
        if current_key in self.transitions:
            self.current_state = self.transitions[current_key]
            print(f"The state transition is {current_key} --> {self.current_state} ")
        else:
            raise ValueError(f"No transition defined for state ({self.current_state}, {input_digit} )")

    def process_number(self, binary_input):

        try:
            for character in binary_input:
                digit = int(character)
                self.find_transition(digit)
        except:
            raise RuntimeError(f"Error while procieesing Binary Input: {binary_input}")
        
        return self.current_state