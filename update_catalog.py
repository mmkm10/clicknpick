import pandas as pd
import json
import os

def update_catalog():
    excel_file = 'catalog.xlsx'
    json_file = 'products.json'

    # Check if Excel file exists
    if not os.path.exists(excel_file):
        print(f"Error: Could not find '{excel_file}'. Please create it with columns: id, name, description, price, image, category")
        return

    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)

        # Handle blank/missing values based on your rules
        df['price'] = df['price'].fillna(1).astype(int) # Default price 1
        df['image'] = df['image'].fillna("") # Default empty string for image
        df = df.fillna("N/A") # Fill any other blanks with N/A

        # Convert to dictionary and save as JSON
        products = df.to_dict(orient='records')
        
        with open(json_file, 'w') as f:
            json.dump(products, f, indent=2)
            
        print(f"✅ Success! {len(products)} products have been updated in {json_file}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    update_catalog()