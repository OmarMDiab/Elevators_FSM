
from tkinter import *
from enum import Enum
import time

master = Tk()
w = Canvas(master, width=1000, height=520)
p_image = PhotoImage(file="stickman.png")
p_image = p_image.subsample(12)
class ElevatorState(Enum):
    """Enumerated states for the elevator."""
    IDLE = "IDLE"
    MOVING_UP_TO_REQUESTED = "MOVING_UP_TO_REQUESTED"
    MOVING_DOWN_TO_REQUESTED = "MOVING_DOWN_TO_REQUESTED"
    MOVING_UP_TO_TARGET = "MOVING_UP_TO_TARGET"
    MOVING_DOWN_TO_TARGET = "MOVING_DOWN_TO_TARGET"
    OPEN_DOORS_AT_REQUESTED = "OPEN_DOORS_AT_REQUESTED"
    CLOSE_DOORS_AT_REQUESTED = "CLOSE_DOORS_AT_REQUESTED"
    ABOVE_REQUESTED_FLOOR = "ABOVE_REQUESTED_FLOOR"
    AT_REQUESTED_FLOOR = "AT_REQUESTED_FLOOR"
    ABOVE_TARGET_FLOOR = "ABOVE_TARGET_FLOOR"
    AT_TARGET_FLOOR = "AT_TARGET_FLOOR"
    OPEN_DOORS_AT_TARGET = "OPEN_DOORS_AT_TARGET"
    CLOSE_DOORS_AT_TARGET = "CLOSE_DOORS_AT_TARGET"




class Elevator:
    """
    Defines an Elevator object that can be used to simulate an elevator as a state based machine.
    """

    def __init__(self, current_floor=1):
        self.current_floor = current_floor
        self.requesting_floor = None
        self.targeted_floor = None
        self.state = ElevatorState.IDLE
        elevator_sqr = w.create_rectangle(72, (10 - self.current_floor) * 50 + 12, 168,
                                          (10 - self.current_floor) * 50 + 58, fill="grey")
        master.update()

    def request(self, req_floor):
        """Floor request is fed to the elevator."""
        self.requesting_floor = req_floor
        global p
        p = w.create_image(
            182 + 100,
            (10 - self.requesting_floor) * 50 + 22 + 25,
            image=p_image,
            anchor=CENTER  # Adjust the anchor point as needed
        )
        """p = w.create_rectangle(172 + 100,
                           (10 - self.requesting_floor) * 50 + 12 + 25,
                           192 + 100,
                           (10 - self.requesting_floor) * 50 + 32 + 25,
                           fill="red")"""
        master.update()
        time.sleep(0.5)
        if self.state == ElevatorState.IDLE:
            self.above_requested_floor()
    def at_requested_floor(self):
        """Returns True if the elevator is at the requested floor."""
        self.state = ElevatorState.AT_REQUESTED_FLOOR
        time.sleep(0.5)
        """global elevator_sqr
        w.delete(elevator_sqr)
        master.update()"""
        time.sleep(0.5)
        """elevator_sqr = w.create_rectangle(72, (10 - elevator.current_floor) * 50 + 12, 168,
                                          (10 - elevator.current_floor) * 50 + 58, fill="grey")
        master.update()"""
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
        global elevator_sqr
        w.delete(elevator_sqr)
        master.update()
        time.sleep(0.5)
        self.current_floor += 1
        elevator_sqr = w.create_rectangle(72, (10 - elevator.current_floor) * 50 + 12, 168,
                                          (10 - elevator.current_floor) * 50 + 58, fill="grey")
        master.update()

        print(f"Elevator at floor {self.current_floor}")
        self.above_requested_floor()

    def move_down_to_requested(self):
        """Moves the elevator down one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_DOWN_TO_REQUESTED
        time.sleep(0.5)
        global elevator_sqr
        w.delete(elevator_sqr)
        master.update()

        time.sleep(0.5)
        self.current_floor -= 1
        elevator_sqr = w.create_rectangle(72, (10 - elevator.current_floor) * 50 + 12, 168,
                                          (10 - elevator.current_floor) * 50 + 58, fill="grey")
        master.update()

        print(f"Elevator at floor {self.current_floor}")
        self.above_requested_floor()

    def open_doors_at_requested(self):
        """Opens the elevator doors."""
        self.state = ElevatorState.OPEN_DOORS_AT_REQUESTED
        global p
        w.delete(p)
        print("Doors are opening...")
        time.sleep(2)
        p = w.create_image(
            80 + 10,  # X coordinate
            (10 - self.current_floor) * 50 + 20 + 10,  # Y coordinate
            image=p_image,
            anchor=CENTER  # Adjust the anchor point as needed
        )
        master.update()
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
        global elevator_sqr
        global p
        w.delete(elevator_sqr)

        w.delete(p)
        master.update()

        time.sleep(0.5)
        self.current_floor += 1
        elevator_sqr = w.create_rectangle(72, (10 - elevator.current_floor) * 50 + 12, 168,
                                          (10 - elevator.current_floor) * 50 + 58, fill="grey")
        p = w.create_image(
            80 + 10,  # X coordinate
            (10 - self.current_floor) * 50 + 20 + 10,  # Y coordinate
            image=p_image,
            anchor=CENTER  # Adjust the anchor point as needed
        )
        master.update()
        print(f"Elevator at floor {self.current_floor}")
        self.at_target_floor()

    def move_down_to_targeted(self):
        """Moves the elevator down one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_DOWN_TO_TARGET
        time.sleep(0.5)
        global elevator_sqr
        global p
        w.delete(elevator_sqr)

        w.delete(p)
        master.update()

        time.sleep(0.5)
        self.current_floor -= 1
        elevator_sqr = w.create_rectangle(72, (10 - elevator.current_floor) * 50 + 12, 168,
                                          (10 - elevator.current_floor) * 50 + 58, fill="grey")
        p = w.create_image(
            80 + 10,  # X coordinate
            (10 - self.current_floor) * 50 + 20 + 10,  # Y coordinate
            image=p_image,
            anchor=CENTER  # Adjust the anchor point as needed
        )
        master.update()
        print(f"Elevator at floor {self.current_floor}")
        self.above_target_floor()

    def open_doors_at_target(self):
        """Opens the elevator doors."""
        self.state = ElevatorState.OPEN_DOORS_AT_TARGET
        print("Doors are opening...")
        global p
        w.delete(p)
        master.update()
        p = w.create_image(
            182 + 100,
            (10 - self.targeted_floor) * 50 + 22 + 25,
            image=p_image,
            anchor=CENTER  # Adjust the anchor point as needed
        )
        master.update()
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
# MAIN
if __name__ == "__main__":
    elevator = Elevator()
    #floors_to_request = [3, 1, 4, 2, 5, 7, 2, 8, 1]
    print(f"Requesting floor {6}")
    # Set up canvas constants

    w.pack()
    w.create_rectangle(70, 10, 170, 510, fill="white")
    for i in range(1, 10):
        w.create_line(70, 50 * i + 10, 170, 50 * i + 10)

    for i in range(10):
        w.create_text(20, 50 * i + 18, anchor=NW, text=str(10 - i) + 'F', font=('TimesNewRoman', 15))

    """w.create_text(480, 30, anchor=NW, text='Passengers request at: ')
    w.create_text(480, 150, anchor=NW, text='Passengers target at: ')
    w.create_text(480, 270, anchor=NW, text='Elevator at: ')"""

    master.update()
    global elevator_Sqr
    elevator_sqr = w.create_rectangle(72, (10 - elevator.current_floor) * 50 + 12, 168, (10 - elevator.current_floor) * 50 + 58, fill="grey")
    master.update()
    elevator.request(9)
    #elevator.request(1)
    elevator.target(4)
