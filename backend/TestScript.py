import pyodbc

# Replace with your connection details
conn_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"  # Change this if your instance name is different
    "Database=DjangoWithReact;"
    "UID=sa;"  # Ensure this is your correct username
    "PWD=sa;"  # Ensure this is your correct password
    "TrustServerCertificate=yes;"  # This helps bypass SSL validation
)


try:
    conn = pyodbc.connect(conn_string)
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
