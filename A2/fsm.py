"""
The FSM Class has the following functionality:
- Implements a Finite State Machine (FSM) to process binary inputs.
- Transitions between states based on predefined rules.
- Raises an error if an undefined transition is encountered.
- The process function processes the current and the transition states and returns the Final remainder to compute_states function
"""
class FSM:

    def __init__(self, initial_state: str, transitions: dict[tuple[str, str], str]):
        self.current_state = initial_state
        self.transitions = transitions

    def find_transition(self, input_digit):

        current_key = (self.current_state, input_digit)
        if current_key in self.transitions:
            self.current_state = self.transitions[current_key]
            print(f"The state transition is {current_key} --> {self.current_state} ")
        else:
            raise ValueError(f"No transition defined for state ({self.current_state}, {input_digit} )")

    def process_number(self, binary_input):

        for character in binary_input:
            digit = int(character)
            self.find_transition(digit)
        return self.current_state