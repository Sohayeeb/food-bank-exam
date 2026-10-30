class Family:
    def __init__(self, family_id, name, members):
        self.family_id = family_id
        self.name = name
        self.members = members


class FoodBank:
    def __init__(self):
        self.families = {}
        self.registered_ids = set()
        self.stock = 0
        self.history = []

    def register_family(self, family_id, name, members):
        if family_id in self.registered_ids:
            print("That family ID is already registered.")
            return
        if members <= 0:
            print("Member count has to be more than zero.")
            return
        self.families[family_id] = Family(family_id, name, members)
        self.registered_ids.add(family_id)
        print("✓ Family registered!.")

    def add_food(self, packs):
        if packs <= 0:
            print("You need to add at least one pack.")
            return
        self.stock += packs
        print(f"Stock updated. Current stock: {self.stock}")

    def distribute_food(self, family_id, packs):
        if family_id not in self.families:
            print("Family not found.")
            return
        if packs <= 0:
            print("Pack count has to be more than zero.")
            return
        if packs > self.stock:
            print(f"Not enough stock. Available: {self.stock}")
            return
        self.stock -= packs
        self.history.append((family_id, packs))
        print(f"Done. Remaining stock: {self.stock}")

    def show_report(self):
        print("\n===== FOOD BANK REPORT =====")
        print(f"Available packs: {self.stock}")

        print("\nRegistered Families:")
        if self.families:
            for f in self.families.values():
                print(f"  {f.family_id} - {f.name} - {f.members} members")
        else:
            print("  No families registered yet.")

        print("\nDistribution History:")
        if self.history:
            for fid, packs in self.history:
                print(f"  {fid} received {packs} packs")
        else:
            print("  Nothing distributed yet.")

        total = sum(p for _, p in self.history)
        print(f"\nTotal distributed: {total}")
        print("------------------------------\n")


def main():
    bank = FoodBank()

    while True:
        print("\n===== COMMUNITY FOOD BANK =====")
        print("1. Register Family")
        print("2. Add Food Packs")
        print("3. Distribute Food Packs")
        print("4. Show Report")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            fid = input("Family ID: ").strip()
            name = input("Family Name: ").strip()
            try:
                members = int(input("Number of Members: "))
            except ValueError:
                print("That's not a valid number.")
                continue
            bank.register_family(fid, name, members)

        elif choice == "2":
            try:
                packs = int(input("Packs to add: "))
            except ValueError:
                print("That's not a valid number.")
                continue
            bank.add_food(packs)

        elif choice == "3":
            fid = input("Family ID: ").strip()
            try:
                packs = int(input("Packs requested: "))
            except ValueError:
                print("That's not a valid number.")
                continue
            bank.distribute_food(fid, packs)

        elif choice == "4":
            bank.show_report()

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Pick 1 to 5.")


if __name__ == "__main__":
    main()
