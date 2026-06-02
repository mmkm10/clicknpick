import pandas as pd
import json

def update_catalog():
    # Replace with your actual Google Sheet ID
    SHEET_ID = 'd9xAM8G2AVhIiQhgR6uggRNlgQfdG6VVk4rHf-rTL3g'
    SHEET_NAME = 'Sheet1' # Change if your tab has a different name
    
    # This URL automatically exports the Google Sheet as a CSV
    csv_url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    json_file = 'products.json'

    try:
        # Read directly from the Google Sheets live URL
        df = pd.read_csv(csv_url)

        # Handle blank/missing values safely
        df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(1).astype(int)
        df['image'] = df['image'].fillna("") 
        df = df.fillna("N/A") 

        products = df.to_dict(orient='records')
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
            
        print(f"✅ Success! {len(products)} products updated.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    update_catalog()
