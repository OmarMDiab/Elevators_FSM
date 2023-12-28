import time
from ElevatorState import ElevatorState

class Elevator:
    """
    Defines an Elevator object that can be used to simulate an elevator as a state based machine.
    """

    def __init__(self, current_floor=1):
        self.current_floor = current_floor
        self.requesting_floor = None
        self.targeted_floor = None
        self.state = ElevatorState.IDLE

    def request(self, req_floor):
        """Floor request is fed to the elevator."""
        self.requesting_floor = req_floor
        time.sleep(0.5)
        if self.state == ElevatorState.IDLE:
            self.above_requested_floor()
    def at_requested_floor(self):
        """Returns True if the elevator is at the requested floor."""
        self.state = ElevatorState.AT_REQUESTED_FLOOR
        time.sleep(0.5)
        if self.current_floor == self.requesting_floor:
            self.open_doors_at_requested()
        else:
            self.move_up_to_requested()

    def above_requested_floor(self):
        """Returns True if the elevator is above the requested floor."""
        self.state = ElevatorState.ABOVE_REQUESTED_FLOOR
        time.sleep(0.5)
        if self.current_floor > self.requesting_floor:
            self.move_down_to_requested()
        else:
            self.at_requested_floor()

    def move_up_to_requested(self):
        """Moves the elevator up one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_UP_TO_REQUESTED
        time.sleep(0.5)
        self.current_floor += 1
        print(f"Elevator at floor {self.current_floor}")
        self.above_requested_floor()

    def move_down_to_requested(self):
        """Moves the elevator down one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_DOWN_TO_REQUESTED
        time.sleep(0.5)
        self.current_floor -= 1
        print(f"Elevator at floor {self.current_floor}")
        self.above_requested_floor()

    def open_doors_at_requested(self):
        """Opens the elevator doors."""
        self.state = ElevatorState.OPEN_DOORS_AT_REQUESTED
        print("Doors are opening...")
        time.sleep(2)
        self.close_doors_at_requested()

    def close_doors_at_requested(self):
        """Closes the elevator doors."""
        self.state = ElevatorState.CLOSE_DOORS_AT_REQUESTED
        print("Doors are closing...")
        time.sleep(2)

    def target(self, target_floor):
        """Floor target is fed to the elevator."""
        self.targeted_floor = target_floor
        time.sleep(0.5)
        if self.state == ElevatorState.CLOSE_DOORS_AT_REQUESTED:
            self.above_target_floor()

    def above_target_floor(self):
        """Returns True if the elevator is above the target floor."""
        self.state = ElevatorState.ABOVE_TARGET_FLOOR
        time.sleep(0.5)
        if self.current_floor > self.targeted_floor:
            self.move_down_to_targeted()
        else:
            self.at_target_floor()

    def at_target_floor(self):
        """Returns True if the elevator is at the target floor."""
        self.state = ElevatorState.AT_TARGET_FLOOR
        time.sleep(0.5)
        if self.current_floor == self.targeted_floor:
            self.open_doors_at_target()
        else:
            self.move_up_to_targeted()

    def move_up_to_targeted(self):
        """Moves the elevator up one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_UP_TO_TARGET
        time.sleep(0.5)
        self.current_floor += 1
        print(f"Elevator at floor {self.current_floor}")
        self.at_target_floor()

    def move_down_to_targeted(self):
        """Moves the elevator down one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_DOWN_TO_TARGET
        time.sleep(0.5)
        self.current_floor -= 1
        print(f"Elevator at floor {self.current_floor}")
        self.above_target_floor()

    def open_doors_at_target(self):
        """Opens the elevator doors."""
        self.state = ElevatorState.OPEN_DOORS_AT_TARGET
        print("Doors are opening...")
        time.sleep(2)
        self.close_doors_at_target()

    def close_doors_at_target(self):
        """Closes the elevator doors."""
        self.state = ElevatorState.CLOSE_DOORS_AT_TARGET
        print("Doors are closing...")
        time.sleep(2)
        self.idle()

    def idle(self):
        """Returns True if the elevator is idle."""
        self.state = ElevatorState.IDLE
        time.sleep(0.5)
        print("Elevator is idle.")
        self.requesting_floor = None
        self.targeted_floor = None