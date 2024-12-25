# Created by VA
# Initialize tables to store the financial values of the tickers

import globalParameters

def initializeDB():
    import sqlite3
    
    conn = sqlite3.connect(globalParameters.priceDBLocation)

    # Create company_info table
    with conn:    
        
        # Create price table
        conn.execute("""
        CREATE TABLE IF NOT EXISTS price (
            ticker TEXT,
            date TEXT,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume FLOAT,
            PRIMARY KEY (ticker, date),
            FOREIGN KEY (ticker) REFERENCES company_info (ticker) ON DELETE CASCADE
        )
        """)

    conn.close()

if __name__=="__main__":
    initializeDB()