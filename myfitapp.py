import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from datetime import datetime

food_database = {
    'seabass':{
        'Calories':110,
        'Protein':20,
        'Carbs':0,
        'Fats':2.5,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'sandwich':{
        'Calories':418,
        'Protein':23.5,
        'Carbs':42.4,
        'Fats':15.7,
        'Type':'Other',
        'Unit':'per unit'
    },
    'instanceNoddle':{
        'Calories':445,
        'Protein':8.2,
        'Carbs':68.2,
        'Fats':15.5,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'costcoroll':{
        'Calories':240,
        'Protein':7,
        'Carbs':50,
        'Fats':0.7,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'mixednuts':{
        'Calories':669,
        'Protein':17.9,
        'Carbs':22,
        'Fats':54.8,
        'Type':'Other',
        'Unit':'per 100g'
    },
    'rice':{
        'Calories':360,
        'Protein':5,
        'Carbs':82,
        'Fats':1.7,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'spaghetti':{
        'Calories':356,
        'Protein':12,
        'Carbs':72,
        'Fats':1.5,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'chickenbreast':{
        'Calories':141,
        'Protein':25,
        'Carbs':0,
        'Fats':2,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'dicedbeef':{
        'Calories':169,
        'Protein':25,
        'Carbs':0,
        'Fats':5,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'egg':{
        'Calories':70,
        'Protein':7,
        'Carbs':0,
        'Fats':5,
        'Type':'Protein',
        'Unit':'per unit'
        # per egg
    },
    'oil':{
        'Calories':900,
        'Protein':0,
        'Carbs':0,
        'Fats':100,
        'Type':'Other',
        'Unit':'per 100g'
        # per egg
    },
    'cookedbeef':{
        'Calories':225,
        'Protein':34,
        'Carbs':0,
        'Fats':8,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'wheyprotein':{
        'Calories':113,
        'Protein':24,
        'Carbs':1.1,
        'Fats':1.3,
        'Type':'Protein',
        'Unit':'per unit'
    },
    'oat':{
        'Calories':100,
        'Protein':3,
        'Carbs':16,
        'Fats':2.1,
        'Type':'Carbs',
        'Unit':'per unit'
    },
    'wholemilk':{
        'Calories':64,
        'Protein':3.4,
        'Carbs':4.6,
        'Fats':3.6,
        'Type':'Other',
        'Unit':'per 100g'
    },
    'semimilk':{
        'Calories':47,
        'Protein':3.5,
        'Carbs':4.6,
        'Fats':1.6,
        'Type':'Other',
        'Unit':'per 100g'
    },
    'skimmedmilk':{
        'Calories':33,
        'Protein':3.5,
        'Carbs':4.5,
        'Fats':0.5,
        'Type':'Other',
        'Unit':'per 100g'
    },
    'oatbran':{
        'Calories':368,
        'Protein':14.9,
        'Carbs':47.8,
        'Fats':9.4,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'sweetpotato':{
        'Calories':86,
        'Protein':1.6,
        'Carbs':20,
        'Fats':0,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'salmon':{
        'Calories':208,
        'Protein':20,
        'Carbs':0,
        'Fats':13,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'shrimp':{
        'Calories':70,
        'Protein':15,
        'Carbs':0,
        'Fats':1.1,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'cod':{
        'Calories':75,
        'Protein':17,
        'Carbs':0,
        'Fats':0.5,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'banana':{
        'Calories':93,
        'Protein':1.4,
        'Carbs':22,
        'Fats':0.2,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'turkey':{
        'Calories':114,
        'Protein':25,
        'Carbs':0.2,
        'Fats':1.3,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'salmoncan':{
        'Calories':98,
        'Protein':20,
        'Carbs':0,
        'Fats':1.8,
        'Type':'Protein',
        'Unit':'per 100g'
    },
    'quinoa':{
        'Calories':92,
        'Protein':3.2,
        'Carbs':16.3,
        'Fats':1.1,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'buckwheat':{
        'Calories':118,
        'Protein':4.3,
        'Carbs':21.3,
        'Fats':1.2,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'oatgroats':{
        'Calories':366,
        'Protein':12,
        'Carbs':61,
        'Fats':6.2,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'blackrice':{
        'Calories':360,
        'Protein':8,
        'Carbs':77.3,
        'Fats':2.7,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'avocado':{
        'Calories':171,
        'Protein':2,
        'Carbs':7.4,
        'Fats':15.3,
        'Type':'Other',
        'Unit':'per 100g'
    },
    'pureoats':{
        'Calories':365,
        'Protein':10.1,
        'Carbs':58.4,
        'Fats':7.4,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'chiaseed':{
        'Calories':490,
        'Protein':16,
        'Carbs':6,
        'Fats':31,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'strawberry':{
        'Calories':32,
        'Protein':1,
        'Carbs':7.1,
        'Fats':0.2,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'cacaopowder':{
        'Calories':25.2,
        'Protein':1.6,
        'Carbs':1.16,
        'Fats':0.64,
        'Type':'Other',
        'Unit':'per unit'
    },
    'blueberry':{
        'Calories':57,
        'Protein':0.7,
        'Carbs':14.5,
        'Fats':0.3,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'oatmilk':{
        'Calories':14,
        'Protein':0.2,
        'Carbs':0,
        'Fats':1.2,
        'Type':'Other',
        'Unit':'per 100g'
    },
    'buckwheatflour':{
        'Calories':349,
        'Protein':13,
        'Carbs':68,
        'Fats':2.1,
        'Type':'Carbs',
        'Unit':'per 100g'
    },
    'slices':{
        'Calories':78,
        'Protein':1.7,
        'Carbs':10.4,
        'Fats':2.8,
        'Type':'Carbs',
        'Unit':'per unit'
    },
    'lowgibread':{
        'Calories':287,
        'Protein':13.2,
        'Carbs':36,
        'Fats':8.5,
        'Type':'Carbs',
        'Unit':'per 100g'
    }

}

# Create or load the food database CSV file
data_file = 'my_food_db.csv'
if not os.path.exists(data_file):
    df = pd.DataFrame.from_dict(food_database, orient='index')
    df = df.sort_index()
    df = df[['Type', 'Unit', 'Calories', 'Protein', 'Carbs', 'Fats']]
    df['Food'] = df.index
    df = df[['Food', 'Type', 'Unit', 'Calories', 'Protein', 'Carbs', 'Fats']]
    df.to_csv(data_file, index=False)
else:
    df = pd.read_csv(data_file)

# Create or load the journal CSV file
today = datetime.now().strftime("%Y-%m-%d")
journal_file = 'daily_journal_' + today + '.csv'
if not os.path.exists(journal_file):
    journal_df = pd.DataFrame(columns=['Date', 'Food', 'Quantity', 'Calories', 'Protein', 'Carbs', 'Fats'])
    journal_df.to_csv(journal_file, index=False)
else:
    journal_df = pd.read_csv(journal_file)

class CalorieCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Calorie Calculator")
        self.root.geometry('900x1300')
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.meals = []
        self.total_nutrients = {'Calories': 0, 'Protein': 0, 'Carbs': 0, 'Fats': 0}
        self.df = pd.read_csv(data_file)
        self.setup_widgets()

    def setup_widgets(self):
        # Widget setup for different sections of the app
        self.food_db_frame = ttk.LabelFrame(self.root, text="Food Database", padding=(10, 10))
        self.food_db_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.meal_frame = ttk.LabelFrame(self.root, text="Meal Entries", padding=(10, 10))
        self.meal_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.total_frame = ttk.LabelFrame(self.root, text="Total Nutrition", padding=(10, 10))
        self.total_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        self.journal_frame = ttk.LabelFrame(self.root, text="Nutrition Journal -- Record your food", padding=(10, 10))
        self.journal_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        self.setup_food_db_frame()
        self.setup_meal_frame()
        self.setup_total_frame()
        self.setup_journal_frame()

    def setup_food_db_frame(self):
        description_label = ttk.Label(self.food_db_frame, text="Add your own food into the database")
        description_label.pack(side='top', fill='x', pady=5)
        # Food database entry and management
        ttk.Label(self.food_db_frame, text="Food Name").pack()
        self.food_name_entry = ttk.Entry(self.food_db_frame)
        self.food_name_entry.pack(fill='x')
        ttk.Label(self.food_db_frame, text="Type").pack()
        self.food_type_combobox = ttk.Combobox(self.food_db_frame, values=["Carbs", "Protein", "Other"])
        self.food_type_combobox.pack(fill='x')
        ttk.Label(self.food_db_frame, text="Unit").pack()
        self.unit_combobox = ttk.Combobox(self.food_db_frame, values=["per 100g", "per unit"])
        self.unit_combobox.pack(fill='x')
        ttk.Label(self.food_db_frame, text="Calories").pack()
        self.calories_entry = ttk.Entry(self.food_db_frame)
        self.calories_entry.pack(fill='x')
        ttk.Label(self.food_db_frame, text="Protein (g)").pack()
        self.protein_entry = ttk.Entry(self.food_db_frame)
        self.protein_entry.pack(fill='x')
        ttk.Label(self.food_db_frame, text="Carbs (g)").pack()
        self.carbs_entry = ttk.Entry(self.food_db_frame)
        self.carbs_entry.pack(fill='x')
        ttk.Label(self.food_db_frame, text="Fats (g)").pack()
        self.fats_entry = ttk.Entry(self.food_db_frame)
        self.fats_entry.pack(fill='x')
        self.add_food_button = ttk.Button(self.food_db_frame, text="Add", command=self.add_food_to_db)
        self.add_food_button.pack(pady=10)

        # Refresh button to reload food data and update Meal Entries
        self.refresh_button = ttk.Button(self.food_db_frame, text="Refresh", command=self.refresh_data)
        self.refresh_button.pack(pady=10)

    def add_food_to_db(self):
        # Add or update food in the database
        try:
            food_name = self.food_name_entry.get() or 'noname'
            food_type = self.food_type_combobox.get() or 'Other'
            unit = self.unit_combobox.get() or 'per unit'
            calories = float(self.calories_entry.get() or 0)
            protein = float(self.protein_entry.get() or 0)
            carbs = float(self.carbs_entry.get() or 0)
            fats = float(self.fats_entry.get() or 0)

            if not calories and (protein or carbs or fats):
                calories = (protein * 4) + (carbs * 4) + (fats * 9)

            new_data = {
                'Food': food_name,
                'Type': food_type,
                'Unit': unit,
                'Calories': calories,
                'Protein': protein,
                'Carbs': carbs,
                'Fats': fats
            }

            df = pd.read_csv(data_file)

            # Check if the food already exists in the database
            existing_food = df[(df['Food'] == food_name) & (df['Unit'] == unit)]
            if not existing_food.empty:
                strs = "This food already exists in the database. Do you want to replace it?" + '\n' + existing_food.to_string(index=False)
                answer = messagebox.askquestion("Food Already Exists", strs)
                if answer == 'yes':
                    df = df[~((df['Food'] == food_name) & (df['Unit'] == unit))]  # Remove existing food entry
                else:
                    return

            new_df = pd.DataFrame([new_data])
            df = pd.concat([df, new_df], ignore_index=True)
            df = df.sort_values(by='Food')
            df.to_csv(data_file, index=False)
            messagebox.showinfo("Success", "Food item added successfully!")
            self.refresh_data()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for calories, protein, carbs, and fats.")

    def refresh_data(self):
        # Reload the food database and update meal entries
        self.df = pd.read_csv(data_file)
        for meal in self.meals:
            meal.update_food_options(self.df)

    def setup_meal_frame(self):
        description_label = ttk.Label(self.meal_frame, text="Add meals and their quantities below, for examples: \nCarbs: rice(per 100g) Quantity: 150 \nProtein: egg (per unit) Quantity: 2")
        description_label.pack(side='top', fill='x', pady=5)
        # Meal entry management
        self.add_meal_button = ttk.Button(self.meal_frame, text="Add Meal", command=self.add_meal)
        self.add_meal_button.pack(fill='x', pady=10)

    def add_meal(self):
        # Add a new meal entry section
        new_meal = MealEntry(self.meal_frame, self.df, self.refresh_total_nutrition, len(self.meals) + 1)
        new_meal.frame.pack(fill='both', expand=True, pady=5)
        self.meals.append(new_meal)

    def setup_total_frame(self):
        # Display total nutrition summary
        self.total_text = tk.Text(self.total_frame, height=10, state='disabled')
        self.total_text.pack(fill='both', expand=True)
        self.reset_button = ttk.Button(self.total_frame, text="Reset All", command=self.reset_all)
        self.reset_button.pack(fill='x', pady=10)

    def calculate_total_nutrition(self):
        # Calculate and display total nutrition from all meals
        self.total_nutrients = {'Calories': 0, 'Protein': 0, 'Carbs': 0, 'Fats': 0}
        combined_items = {}
        unit_mapping = {food: unit for food, unit in self.df[['Food', 'Unit']].values}  # Create a mapping of food to unit
        protein_from_carbs = 0  # Initialize protein from carbs to 0

        for meal in self.meals:
            for key, value in meal.nutrients.items():
                self.total_nutrients[key] += value
            for item in meal.food_list:
                food, qty = item.split(': ')
                qty = float(qty.replace('g', '').strip())  # Assume all quantities are initially with 'g' and strip it
                food_data = self.df[self.df['Food'] == food].iloc[0]

                if food_data['Type'] == 'Carbs':
                    protein_from_carbs += (food_data['Protein'] * qty / 100)

                if food in combined_items:
                    combined_items[food] += qty
                else:
                    combined_items[food] = qty

        # Format food items for display, checking if the unit should have 'g'
        self.food_items = [f"{food}: {str(qty) + 'g' if 'per 100g' in unit_mapping[food] else str(qty)}" for food, qty in combined_items.items()]
        self.total_nutrients['Protein_Excluding_Carbs'] = self.total_nutrients['Protein'] - protein_from_carbs  # Add the adjusted protein value
        self.update_total_nutrition_display()

    def update_total_nutrition_display(self):
        # Update the display with the total calculated nutrition values
        self.total_text.config(state='normal')
        self.total_text.delete(1.0, tk.END)
        self.total_text.insert(tk.END, f"Total Calories: {self.total_nutrients['Calories']:.1f}\n")
        self.total_text.insert(tk.END, f"Total Protein: {self.total_nutrients['Protein']:.1f} g ({self.total_nutrients['Protein_Excluding_Carbs']:.1f} g)\n")
        self.total_text.insert(tk.END, f"Total Carbs: {self.total_nutrients['Carbs']:.1f} g\n")
        self.total_text.insert(tk.END, f"Total Fats: {self.total_nutrients['Fats']:.1f} g\n")
        for item in self.food_items:
            self.total_text.insert(tk.END, f"{item}\n")
        self.total_text.config(state='disabled')

    def reset_all(self):
        # Reset all meals and total nutrition calculations
        for meal in self.meals:
            meal.clear_meal()
        self.meals.clear()
        self.calculate_total_nutrition()

    def refresh_total_nutrition(self):
        # Refresh and recalculate the total nutrition display
        self.calculate_total_nutrition()

    def setup_journal_frame(self):

        # Journal section for daily nutrition tracking
        self.display_journal_text = tk.Text(self.journal_frame, height=10, state='disabled')
        self.display_journal_text.pack(fill='both', expand=True)
        self.update_journal_button = ttk.Button(self.journal_frame, text="Update Journal", command=self.update_journal)
        self.update_journal_button.pack(fill='x', pady=10)
        self.reset_journal_button = ttk.Button(self.journal_frame, text="Reset Today's Journal", command=self.reset_journal)
        self.reset_journal_button.pack(fill='x', pady=10)
        self.refresh_journal_display()

    def update_journal(self):
        # Update the daily journal with the entries from meal sections
        today = datetime.now().strftime("%Y-%m-%d")
        journal_df = pd.read_csv(journal_file)

        for meal in self.meals:
            for food_info in meal.food_list:
                food_name, qty_str = food_info.split(': ')
                qty = float(qty_str.replace('g', '').strip())
                food_data = self.df[self.df['Food'] == food_name].iloc[0]
                scale = qty if food_data['Unit'] == 'per unit' else (qty / 100)

                quantity_display = f"{qty}g" if 'per 100g' in food_data['Unit'] else f"{qty}"

                match = journal_df[(journal_df['Date'] == today) & (journal_df['Food'] == food_name)]
                if not match.empty:
                    journal_df.loc[match.index, 'Quantity'] = match['Quantity'].astype(str).str.replace('g', '').astype(float) + qty
                    journal_df.loc[match.index, 'Calories'] += food_data['Calories'] * scale
                    journal_df.loc[match.index, 'Protein'] += food_data['Protein'] * scale
                    journal_df.loc[match.index, 'Carbs'] += food_data['Carbs'] * scale
                    journal_df.loc[match.index, 'Fats'] += food_data['Fats'] * scale
                else:
                    new_entry = pd.DataFrame([{
                        'Date': today,
                        'Food': food_name,
                        'Quantity': quantity_display,
                        'Calories': food_data['Calories'] * scale,
                        'Protein': food_data['Protein'] * scale,
                        'Carbs': food_data['Carbs'] * scale,
                        'Fats': food_data['Fats'] * scale
                    }])
                    journal_df = pd.concat([journal_df, new_entry], ignore_index=True)

        journal_df.to_csv(journal_file, index=False)
        self.refresh_journal_display()

    def refresh_journal_display(self):
        # Refresh and display the journal entries for today
        self.display_journal_text.config(state='normal')
        self.display_journal_text.delete(1.0, tk.END)
        today = datetime.now().strftime("%Y-%m-%d")
        journal_df = pd.read_csv(journal_file)
        today_entries = journal_df[journal_df['Date'] == today]

        if not today_entries.empty:
            headers = ["Food", "Quantity", "Calories", "Protein", "Carbs", "Fats"]

            # Calculate the maximum width for the food name column
            max_food_width = max(today_entries['Food'].apply(lambda x: len(x + " (" + self.df[self.df['Food'] == x].iloc[0]['Unit'] + ")")))
            food_col_width = max(max_food_width, len(headers[0])) + 5  # Add some extra space to keep the format neat

            for header in headers:
                if header == "Food":
                    self.display_journal_text.insert(tk.END, f"{header:<{food_col_width}} ")
                else:
                    self.display_journal_text.insert(tk.END, f"{header:<15} ")
            self.display_journal_text.insert(tk.END, "\n")

            protein_from_carbs = 0

            for index, row in today_entries.iterrows():
                food_display = f"{row['Food']} ({self.df[self.df['Food'] == row['Food']].iloc[0]['Unit']})"
                self.display_journal_text.insert(tk.END, f"{food_display:<{food_col_width}} {row['Quantity']:<15} {row['Calories']:<15.1f} {row['Protein']:<15.1f} {row['Carbs']:<15.1f} {row['Fats']:<15.1f}\n")
                food_data = self.df[self.df['Food'] == row['Food']].iloc[0]
                if food_data['Type'] == 'Carbs':
                    protein_from_carbs += row['Protein']

            # Calculate and display totals
            self.display_journal_text.insert(tk.END, "\nTotal:")
            total_calories = today_entries['Calories'].sum()
            total_protein = today_entries['Protein'].sum()
            total_carbs = today_entries['Carbs'].sum()
            total_fats = today_entries['Fats'].sum()
            total_protein_excluding_carbs = total_protein - protein_from_carbs
            self.display_journal_text.insert(tk.END, f"{'':<{food_col_width-len('Total:')}} {'':<15} {total_calories:<15.1f} {total_protein:.1f}/{total_protein_excluding_carbs:<9.1f} {total_carbs:<15.1f} {total_fats:<15.1f}\n")
            #self.display_journal_text.insert(tk.END, f"{'':<{food_col_width-len('Total:')}} {'':<15} {total_calories:<15.1f} {total_protein:<15.1f} ({total_protein_excluding_carbs:<15.1f}) {total_carbs:<15.1f} {total_fats:<15.1f}\n")
        else:
            self.display_journal_text.insert(tk.END, "No entries for today.")

        self.display_journal_text.config(state='disabled')

    def reset_journal(self):
        # Reset the journal entries for today
        answer = messagebox.askquestion("Reset Journal", "Are you sure you want to reset today's journal entries?")
        if answer == 'yes':
            today = datetime.now().strftime("%Y-%m-%d")
            journal_df = pd.read_csv(journal_file)
            journal_df = journal_df[journal_df['Date'] != today]
            journal_df.to_csv(journal_file, index=False)
            messagebox.showinfo("Journal Reset", "Today's journal has been reset successfully.")
            self.refresh_journal_display()

class MealEntry:
    def __init__(self, parent, df, refresh_total_nutrition, meal_number):
        # Initialize a meal entry
        self.frame = ttk.Frame(parent)
        self.nutrients = {'Calories': 0, 'Protein': 0, 'Carbs': 0, 'Fats': 0}
        self.df = df
        self.refresh_total_nutrition = refresh_total_nutrition
        self.food_list = []
        self.setup_widgets(meal_number)

    def setup_widgets(self, meal_number):
        # Set up widgets for each meal entry
        ttk.Label(self.frame, text=f"Meal {meal_number}:").pack()
        self.comboboxes = {}

        for food_type in ['Carbs', 'Protein', 'Other']:
            frame = ttk.Frame(self.frame)
            frame.pack(fill='x', expand=True)

            label = ttk.Label(frame, text=f"{food_type}:")
            label.pack(side='left')

            food_options = self.df[self.df['Type'] == food_type].apply(lambda row: f"{row['Food']} ({row['Unit']})", axis=1).tolist()
            combo = ttk.Combobox(frame, values=food_options)
            combo.pack(side='left', fill='x', expand=True)
            self.comboboxes[food_type] = combo

            ttk.Label(frame, text="Quantity:").pack(side='left')

            qty_entry = ttk.Entry(frame)
            qty_entry.pack(side='left')

            add_button = ttk.Button(frame, text="Add", command=lambda c=combo, q=qty_entry, ft=food_type: self.add_food(c, q, ft))
            add_button.pack(side='left')

        self.nutrition_text = tk.Text(self.frame, height=4, state='disabled')
        self.nutrition_text.pack(fill='both', expand=True)
        self.clear_button = ttk.Button(self.frame, text="Clear Meal", command=self.clear_meal)
        self.clear_button.pack(fill='x')

    def update_food_options(self, df):
        # Update the food options for each meal based on the current database
        self.df = df
        for food_type, combo in self.comboboxes.items():
            combo['values'] = self.df[self.df['Type'] == food_type].apply(lambda row: f"{row['Food']} ({row['Unit']})", axis=1).tolist()

    def add_food(self, combo, qty_entry, food_type):
        # Add food to the meal and calculate the nutrients
        try:
            food_label = combo.get()
            quantity = float(qty_entry.get())
            food_name, unit = food_label.split(' (', 1)
            unit = unit[:-1]  # Remove closing parenthesis
            food_data = self.df[(self.df['Food'] == food_name) & (self.df['Unit'] == unit)].iloc[0]
            scale = quantity if unit == 'per unit' else (quantity / 100)
            self.nutrients['Calories'] += food_data['Calories'] * scale
            self.nutrients['Protein'] += food_data['Protein'] * scale
            self.nutrients['Carbs'] += food_data['Carbs'] * scale
            self.nutrients['Fats'] += food_data['Fats'] * scale
            food_key = f"{food_name}: {quantity if unit == 'per unit' else str(quantity) + 'g'}"
            found = False
            for i, item in enumerate(self.food_list):
                if item.startswith(food_name + ':'):
                    old_qty = float(item.split(': ')[1].replace('g', ''))
                    new_qty = old_qty + quantity
                    self.food_list[i] = f"{food_name}: {new_qty if unit == 'per unit' else str(new_qty) + 'g'}"
                    found = True
                    break
            if not found:
                self.food_list.append(food_key)
            self.update_nutrition_display()
            self.refresh_total_nutrition()
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity. Please enter a valid number.")

    def update_nutrition_display(self):
        # Update the display of nutrition for this meal
        protein_from_carbs = 0
        for food in self.food_list:
            food_name, qty_str = food.split(': ')
            qty = float(qty_str.replace('g', '').strip())
            food_data = self.df[self.df['Food'] == food_name].iloc[0]
            if food_data['Type'] == 'Carbs':
                protein_from_carbs += (food_data['Protein'] * qty / 100)

        self.nutrition_text.config(state='normal')
        self.nutrition_text.delete(1.0, tk.END)
        for food in self.food_list:
            self.nutrition_text.insert(tk.END, f"{food}\n")
        self.nutrition_text.insert(tk.END, f"Calories: {self.nutrients['Calories']:.1f}\n")
        self.nutrition_text.insert(tk.END, f"Protein: {self.nutrients['Protein']:.1f} g ({self.nutrients['Protein'] - protein_from_carbs:.1f} g)\n")
        self.nutrition_text.insert(tk.END, f"Carbs: {self.nutrients['Carbs']:.1f} g\n")
        self.nutrition_text.insert(tk.END, f"Fats: {self.nutrients['Fats']:.1f} g\n")
        self.nutrition_text.config(state='disabled')

    def clear_meal(self):
        # Clear all entries for this meal
        self.nutrients = {'Calories': 0, 'Protein': 0, 'Carbs': 0, 'Fats': 0}
        self.food_list = []
        self.update_nutrition_display()
        self.refresh_total_nutrition()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieCalculatorApp(root)
    root.mainloop()

