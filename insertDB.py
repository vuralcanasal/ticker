# Created by VA
# To insert the financial values of the tickers into the DB

import globalParameters
import sqlite3

def insertPrice(name, date_string, open_price, high_price, low_price, close_price, volume):
    # Open connection for DB
    conn = sqlite3.connect(globalParameters.priceDBLocation)
    # Insert all values into the db - price table
    try:
        conn.execute("""
            INSERT INTO price 
            VALUES (?, ?, ?, ?, ?, ?, ?) 
            ON CONFLICT (ticker, date) 
            DO UPDATE SET 
            open = excluded.open,
            high = excluded.high,
            low = excluded.low,
            close = excluded.close,
            volume = excluded.volume;
            """, 
            (
                name, 
                date_string,
                open_price,
                high_price,
                low_price,
                close_price,
                volume
            )
        )
        
    except Exception as e:
        print(f"Error on inserting price for {name} at {date_string}: {e}")
    finally:
        # Commit changes and close the database connection
        if conn:
            conn.commit()
            conn.close()