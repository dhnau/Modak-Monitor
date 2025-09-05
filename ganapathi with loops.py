import random

# ================== Project Banner ==================
modak_art = """
🐘 ============================== 🐘
       🌸 Modak Monitor 🌸
       Author: Dhanu
       🙏 Ganapati Bappa Blesses You 🙏
       ॐ गण गणपतये नमः
🐘 ============================== 🐘
"""

# ================== Preloaded Recipes ==================
recipes = {
    "Ukadiche Modak": {"calories": 250, "protein": 3, "ingredients": ["rice flour", "jaggery", "coconut", "ghee"]},
    "Puran Poli": {"calories": 350, "protein": 6, "ingredients": ["wheat flour", "jaggery", "chana dal", "ghee"]},
    "Gulab Jamun": {"calories": 150, "protein": 2, "ingredients": ["khoya", "sugar", "ghee"]},
    "Kheer": {"calories": 200, "protein": 5, "ingredients": ["milk", "rice", "sugar", "dry fruits"]},
    "Naralachi Wadi": {"calories": 300, "protein": 4, "ingredients": ["coconut", "sugar", "milk"]}
}

# ================== Bappa Blessings ==================
blessings = [
    "🌸 'Health is the true wealth' – Bappa",
    "🐘 'Eat with devotion, but don’t forget moderation!'",
    "🙏 'Balanced food, balanced thoughts, balanced life.'",
    "✨ 'Too much sugar spoils the prasadam spirit.'",
    "🌼 'Self-control is the best offering to Bappa.'"
]

# ================== Daily Log & Limit ==================
daily_log = []         # Stores all food entries
DAILY_LIMIT = 2000     # Safe daily calorie limit

# ================== Progress Bar Function ==================
def progress_bar(current, total, length=20):
    filled = int(length * current / total)
    bar = "█" * filled + "░" * (length - filled)
    percent = (current / total) * 100
    return f"[{bar}] {percent:.1f}%"

# ================== Eat Food Function ==================
def eat_food():
    print(modak_art)  # Show project banner first

    # Ask user what they ate
    name = input("What did you eat? ").title()

    if name in recipes:
        qty = int(input(f"How many {name}s did you eat? "))
        total_cal = recipes[name]["calories"] * qty
        total_pro = recipes[name]["protein"] * qty

        # Log food
        daily_log.append({"name": name, "calories": total_cal, "protein": total_pro})
        print(f"\n🍴 Logged: {qty} x {name} → {total_cal} kcal, {total_pro}g protein")

        # Current total calories
        current_total = sum(entry["calories"] for entry in daily_log)

        # Show mini progress bar
        print("\nCalorie Progress:")
        print(progress_bar(current_total, DAILY_LIMIT))

        # Blessings / warnings
        if current_total > DAILY_LIMIT:
            print("\n🤯 Sugar overload detected! Even Bappa is worried.")
            over_limit_blessings = [
                "😬 Bappa says: 'Even laddus need moderation!'",
                "🍭 Sweet devotion, but balance is divine!",
                "🐘 Too much sugar today, pray tomorrow with extra focus!"
            ]
            print(random.choice(over_limit_blessings))
        elif current_total > DAILY_LIMIT * 0.8:
            print("\n😅 You're close to your daily limit. Ganapati reminds you: moderation is key!")
            print("🙏 Blessing: 'Control today, enjoy tomorrow!'")
        else:
            print("\n😇 Divine balance today! ✨")
            print(random.choice(blessings))
    else:
        print("Recipe not found! Add it first.")


# ================== Show Recipes Function ==================
def show_recipes():
    print(modak_art)  # Show project banner

    print("\n📖 Recipe Book:")
    for name, details in recipes.items():
        print(f"- {name}: {details['calories']} kcal, {details['protein']} g protein")
        print(f"   Ingredients: {', '.join(details['ingredients'])}")

    # Random blessing after viewing recipes
    print("\n" + random.choice(blessings))
# ================== Show Daily Summary ==================
def show_summary():
    print(modak_art)  # Show project banner

    total_cal = sum(entry["calories"] for entry in daily_log)
    total_pro = sum(entry["protein"] for entry in daily_log)

    print("\n🌸 Daily Nutrition Summary 🌸")
    print(f"Total Calories: {total_cal} kcal")
    print(f"Total Protein: {total_pro} g")

    # Show progress bar
    print("\nCalorie Progress:")
    print(progress_bar(total_cal, DAILY_LIMIT))

    # Mood / Blessings based on calories
    if total_cal > DAILY_LIMIT:
        print("\n🤯 Sugar overload detected! Even Bappa is worried.")
        print("⚠️ Devotion is sweet, but too many laddus drown the balance!")
    elif total_cal > DAILY_LIMIT * 0.8:
        print("\n😅 Careful! You are close to your daily limit.")
        print("🐘 Bappa reminds you: 'Control today, enjoy tomorrow!'")
    else:
        print("\n😇 Divine balance today! ✨")
        print("🙏 Ganapati Bappa Blesses You: 'Balanced food, balanced mind!'")

    # Random blessing
    print("\n" + random.choice(blessings))


# ================== Add Recipe Function ==================
def add_recipe():
    print(modak_art)  # Show project banner first

    name = input("Enter recipe name: ").title()
    calories = int(input("Calories per serving: "))
    protein = int(input("Protein (g) per serving: "))
    ingredients = input("Ingredients (comma separated): ").split(",")

    recipes[name] = {
        "calories": calories,
        "protein": protein,
        "ingredients": [i.strip() for i in ingredients]
    }

    print(f"\n✨ {name} added to recipe book!")
    print(random.choice(blessings))

# ================== Main Menu ==================
while True:
    print(modak_art)
    print("🎉 Welcome to Modak Monitor 🐘")
    print("=======================================")
    print("1. Add Recipe")
    print("2. Log Food Eaten")
    print("3. Show Recipe Book")
    print("4. Show Daily Summary")
    print("5. Exit")
    print("=======================================")

    choice = input("Choose (1-5): ")

    if choice == "1":
        add_recipe()
    elif choice == "2":
        eat_food()
    elif choice == "3":
        show_recipes()
    elif choice == "4":
        show_summary()
    elif choice == "5":
        print("🙏 Ganapati Bappa Morya! Stay healthy 🌸")
        break
    else:
        print("Invalid choice, try again.")



