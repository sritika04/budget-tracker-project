import pandas as pd

data = {
    'date': [
        # January
        '2024-01-02', '2024-01-05', '2024-01-08', '2024-01-12', '2024-01-15',
        '2024-01-18', '2024-01-22', '2024-01-25', '2024-01-28', '2024-01-30',
        # February
        '2024-02-01', '2024-02-04', '2024-02-07', '2024-02-10', '2024-02-13',
        '2024-02-16', '2024-02-19', '2024-02-22', '2024-02-25', '2024-02-28',
        # March
        '2024-03-02', '2024-03-05', '2024-03-08', '2024-03-12', '2024-03-15',
        '2024-03-18', '2024-03-22', '2024-03-25', '2024-03-28', '2024-03-30',
        # April
        '2024-04-01', '2024-04-04', '2024-04-07', '2024-04-10', '2024-04-13',
        '2024-04-16', '2024-04-19', '2024-04-22', '2024-04-25', '2024-04-28',
        # May
        '2024-05-02', '2024-05-05', '2024-05-08', '2024-05-12', '2024-05-15',
        '2024-05-18', '2024-05-22', '2024-05-25', '2024-05-28', '2024-05-30',
        # June
        '2024-06-01', '2024-06-04', '2024-06-07', '2024-06-10', '2024-06-13',
        '2024-06-16', '2024-06-19', '2024-06-22', '2024-06-25', '2024-06-28',
        # July
        '2024-07-02', '2024-07-05', '2024-07-08', '2024-07-12', '2024-07-15',
        '2024-07-18', '2024-07-22', '2024-07-25', '2024-07-28', '2024-07-30',
        # August
        '2024-08-01', '2024-08-04', '2024-08-07', '2024-08-10', '2024-08-13',
        '2024-08-16', '2024-08-19', '2024-08-22', '2024-08-25', '2024-08-28',
        # September
        '2024-09-02', '2024-09-05', '2024-09-08', '2024-09-12', '2024-09-15',
        '2024-09-18', '2024-09-22', '2024-09-25', '2024-09-28', '2024-09-30',
        # October
        '2024-10-01', '2024-10-04', '2024-10-07', '2024-10-10', '2024-10-13',
        '2024-10-16', '2024-10-19', '2024-10-22', '2024-10-25', '2024-10-28',
        # November
        '2024-11-02', '2024-11-05', '2024-11-08', '2024-11-12', '2024-11-15',
        '2024-11-18', '2024-11-22', '2024-11-25', '2024-11-28', '2024-11-30',
        # December
        '2024-12-01', '2024-12-04', '2024-12-07', '2024-12-10', '2024-12-13',
        '2024-12-16', '2024-12-19', '2024-12-22', '2024-12-25', '2024-12-28',
    ],
    'category': [
        # January
        'Rent','Food','Transport','Entertainment','Food',
        'Health','Shopping','Utilities','Food','Transport',
        # February
        'Rent','Food','Entertainment','Transport','Food',
        'Health','Shopping','Utilities','Food','Entertainment',
        # March
        'Rent','Food','Transport','Shopping','Food',
        'Health','Entertainment','Utilities','Food','Transport',
        # April
        'Rent','Food','Health','Transport','Food',
        'Shopping','Entertainment','Utilities','Food','Health',
        # May
        'Rent','Food','Transport','Entertainment','Food',
        'Health','Shopping','Utilities','Food','Transport',
        # June
        'Rent','Food','Shopping','Transport','Food',
        'Health','Entertainment','Utilities','Food','Shopping',
        # July
        'Rent','Food','Transport','Entertainment','Food',
        'Health','Shopping','Utilities','Food','Transport',
        # August
        'Rent','Food','Health','Shopping','Food',
        'Transport','Entertainment','Utilities','Food','Health',
        # September
        'Rent','Food','Transport','Entertainment','Food',
        'Health','Shopping','Utilities','Food','Transport',
        # October
        'Rent','Food','Shopping','Transport','Food',
        'Health','Entertainment','Utilities','Food','Shopping',
        # November
        'Rent','Food','Transport','Entertainment','Food',
        'Health','Shopping','Utilities','Food','Transport',
        # December
        'Rent','Food','Shopping','Entertainment','Food',
        'Health','Transport','Utilities','Food','Shopping',
    ],
    'amount': [
        # January
        5000,350,120,500,200,800,999,600,180,150,
        # February
        5000,400,300,130,250,750,1200,580,220,450,
        # March
        5000,370,140,850,230,900,1100,620,190,160,
        # April
        5000,420,110,200,280,820,950,590,210,780,
        # May
        5000,390,130,600,260,870,1050,610,200,170,
        # June
        5000,450,1300,180,300,910,700,630,240,1100,
        # July
        5000,410,150,550,270,840,1150,600,220,140,
        # August
        5000,380,860,1250,290,160,650,615,235,790,
        # September
        5000,430,125,480,310,880,1080,625,215,155,
        # October
        5000,460,1400,165,320,920,720,640,250,1050,
        # November
        5000,400,135,520,280,850,1000,610,225,145,
        # December
        5000,500,1500,800,350,950,200,700,300,1300,
    ],
    'month_num': [
        1,1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,2,
        3,3,3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,4,4,
        5,5,5,5,5,5,5,5,5,5,
        6,6,6,6,6,6,6,6,6,6,
        7,7,7,7,7,7,7,7,7,7,
        8,8,8,8,8,8,8,8,8,8,
        9,9,9,9,9,9,9,9,9,9,
        10,10,10,10,10,10,10,10,10,10,
        11,11,11,11,11,11,11,11,11,11,
        12,12,12,12,12,12,12,12,12,12,
    ],
    'month': [
        'January','January','January','January','January','January','January','January','January','January',
        'February','February','February','February','February','February','February','February','February','February',
        'March','March','March','March','March','March','March','March','March','March',
        'April','April','April','April','April','April','April','April','April','April',
        'May','May','May','May','May','May','May','May','May','May',
        'June','June','June','June','June','June','June','June','June','June',
        'July','July','July','July','July','July','July','July','July','July',
        'August','August','August','August','August','August','August','August','August','August',
        'September','September','September','September','September','September','September','September','September','September',
        'October','October','October','October','October','October','October','October','October','October',
        'November','November','November','November','November','November','November','November','November','November',
        'December','December','December','December','December','December','December','December','December','December',
    ]
}

df = pd.DataFrame(data)
df.to_csv('expense.csv', index=False)
print("Done! expense.csv created!")
print(f"Total rows: {len(df)}")
print(f"Months: {df['month'].nunique()}")
print(f"Total spending: ₹{df['amount'].sum():,}")
