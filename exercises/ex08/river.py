"""File to define River class."""


__author__ = "730556372"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Simulating a river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New river with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing old fish and bears."""
        new_bears_list: list[Bear] = []
        for idx in range(0, len(self.bears)):
            if self.bears[idx].age <= 5:
                new_bears_list.append(self.bears[idx])
        self.bears = new_bears_list
        new_fish_list: list[Fish] = []
        for idx in range(0, len(self.fish)):
            if self.fish[idx].age <= 3:
                new_fish_list.append(self.fish[idx])
        self.fish = new_fish_list

    def remove_fish(self, amount: int):
        """Removing the first {amount} fish."""
        for idx in range(0, amount):
            self.fish.pop(0)

    def bears_eating(self):
        """The bears be eating."""
        for baloo in self.bears:
            if len(self.fish) >= 5:  # Checking that there are at least 5 fish before eating them
                self.remove_fish(3)
                baloo.eat(3)
    
    def check_hunger(self):
        """Eliminating bears with a hunger score less than 0."""
        sated_bears_list: list[Bear] = []
        for baloo in self.bears:
            if baloo.hunger_score >= 0:
                sated_bears_list.append(baloo)
        self.bears = sated_bears_list
        return None
        
    def repopulate_fish(self):
        """Adding more fish."""
        new_fish_num: int = 4 * (len(self.fish) // 2)
        for idx in range(0, new_fish_num):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Adding more bears."""
        new_bears_num: int = len(self.bears) // 2
        for idx in range(0, new_bears_num):
            self.bears.append(Bear())
    
    def view_river(self):
        """Displaying relevant river information."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for i in range(0, 7):
            self.one_river_day()
