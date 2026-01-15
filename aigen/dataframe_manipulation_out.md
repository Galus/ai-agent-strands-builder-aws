### Documentation:

#### How to Install Dependencies:
```bash
uv add pandas
```

#### How the Code Works:
1. The script creates a sample DataFrame with employee data including Name, Age, and Salary.
2. It adds a Bonus column calculated as 10% of the Salary.
3. The data is filtered to include only employees over 30 years old.
4. The filtered data is grouped into age brackets (30s, 40s, 50s).
5. For each age bracket, it calculates the average Salary and Bonus.

#### Sample Output:
```
Filtered Employee Data (Age > 30):
============================================================
    Name  Age  Salary   Bonus Age_Bracket
1  Alice   32   65000  6500.0         30s
2    Bob   45   85000  8500.0         40s
4  David   35   70000  7000.0         30s
5    Eve   41   75000  7500.0         40s
6  Frank   52   95000  9500.0         50s
7  Grace   38   72000  7200.0         30s

Average Salary and Bonus by Age Bracket:
============================================================
            Salary    Bonus
Age_Bracket
30s         69000.0  6900.0
40s         80000.0  8000.0
50s         95000.0  9500.0
```

#### How to Run:
Save the script as `employee_analysis.py` and run it using:
```bash
python employee_analysis.py
```

#### Code Structure:
- The main logic is encapsulated in the `process_employee_data()` function
- The `main()` function handles the execution flow and result display
- Clear inline comments explain each step of the process
- Type hints and docstrings provide additional documentation

This script provides a clear example of common pandas operations including:
- DataFrame creation
- Column addition
- Filtering
- Grouping
- Aggregation
