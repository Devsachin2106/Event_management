class Event:
    def __init__(self, event, place, amount):
        self.event = event
        self.place = place
        self.amount = amount

    def display_details(self):
        print(f"Event: {self.event}, Place: {self.place}, Amount: {self.amount}")

class SpecialEvent(Event):
    def __init__(self, event, place, amount, special_feature):
        super().__init__(event, place, amount)
        self.special_feature = special_feature

    def display_details(self):
        super().display_details()
        print(f"Special Feature: {self.special_feature}")


class EventManagementSystem:
    def __init__(self):
        self.data = []

    def add_event(self):
        event = input("Enter the type of event: ")
        place = input("Enter the place details: ")
        amount = int(input("Enter the budget: "))
        event_obj = Event(event, place, amount)
        self.data.append(event_obj)
        print("Event added successfully")

    def display_events(self):
        if len(self.data) == 0:
            print("Oops! No events booked currently")
        else:
            print("List of booked events")
            for i, event_obj in enumerate(self.data, start=1):
                print(f"{i}.", end=" ")
                event_obj.display_details()

    def search_events(self):
        event = input("Enter the event details to search: ")
        found_events = []
        for event_obj in self.data:
            if event_obj.event.lower() == event.lower():
                found_events.append(event_obj)

        if len(found_events) == 0:
            print("No matching events found")
        else:
            print("Matching events")
            for event_obj in found_events:
                event_obj.display_details()

    def delete_events(self):
        event = input("Enter the title of event to delete: ")
        found_events = []
        for event_obj in self.data:
            if event_obj.event.lower() == event.lower():
                found_events.append(event_obj)
        if len(found_events) == 0:
            print("No matching event title found")
        else:
            print("Matching Events")
            for i, event_obj in enumerate(found_events, start=1):
                print(f"{i}.", end=" ")
                event_obj.display_details()
        choice = input("Enter the number of the event to delete: ")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= len(found_events):
                event_to_delete = found_events[choice - 1]
                self.data.remove(event_to_delete)
                print("Event successfully deleted")
            else:
                print("Invalid choice")
        except:
            print("Invalid choice")

    def exit(self):
        print("Thank you for using our Event Management System!")



event_system = EventManagementSystem()

while True:
    print("\n***** Event Management System *****")
    print("1. Add Event")
    print("2. Display Events")
    print("3. Search Events")
    print("4. Delete Event")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        event_type = input("Enter the type of event (1. Regular / 2. Special): ")
        if event_type == "1":
            event_system.add_event()
        elif event_type == "2":
            event = input("Enter the type of event: ")
            place = input("Enter the place details: ")
            amount = int(input("Enter the budget: "))
            special_feature = input("Enter the special feature: ")
            event_obj = SpecialEvent(event, place, amount, special_feature)
            event_system.data.append(event_obj)
            print("Special Event added successfully")
        else:
            print("Invalid choice")
    elif choice == "2":
        event_system.display_events()
    elif choice == "3":
        event_system.search_events()
    elif choice == "4":
        event_system.delete_events()
    elif choice == "5":
        event_system.exit()
        break
    else:
        print("Invalid choice. Please choose a correct option.")
