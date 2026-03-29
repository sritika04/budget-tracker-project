import pandas as pd
df= pd.read_csv('expense.csv')
print("data loaded successfully")
print(df)
total= df['amount'].sum()
print(f"\nTotal amount: {total}")
category_summary=df.groupby('category')['amount'].sum()
print(f"\nSpending by category:")
print(category_summary)
monthly_summary=df.groupby('month')['amount'].sum()
print(f"\nSpending by month:")
print(monthly_summary)
with pd.ExcelWriter('budgetsummary.xlsx') as writer:
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    category_summary.to_excel(writer, sheet_name='By Category')
    monthly_summary.to_excel(writer, sheet_name='By Month')

print("\nDone! budgetsummary.xlsx created!")