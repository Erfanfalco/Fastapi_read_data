# SQLs commands string to be executed against the database


future_settlements_cmd = ('''DECLARE @StartDate DATE = dateadd(day, 2, CAST(GETDATE() AS DATE));
                          DECLARE @EndDate DATE = dateadd(day, -4, CAST(GETDATE() AS DATE));
                          SELECT SUM(Amount),COUNT(Amount) ,CAST( RequestDate AS DATE)
                          FROM [HamtaDb].[dbo].[PaymentRequests]
                          WHERE [RequestDate] >= @EndDate AND [RequestDate] <= @StartDate
                          GROUP BY RequestDate
                          ORDER BY RequestDate asc
                          ''')


customer_remain_cmd = ('''SELECT  SUM(f.remain) AS total_remain,customer_data.branch_id,customer_data.branch_name
                        FROM financial_status_data f 
                        INNER JOIN customer_data ON customer_data.account_number = f.account_number 
                        GROUP BY customer_data.branch_id, customer_data.branch_name ORDER BY total_remain;
                        ''')


weekly_wage_cmd = ('''SELECT Week_Number,
                    Total_Interest,
                    tr_ge_date
                    FROM weekly_wage_cube
                    WHERE tr_ge_date <= CURRENT_DATE
                    ORDER BY tr_ge_date DESC
                    LIMIT 20;
                    ''')


daily_usable_credit_cmd = ('''SELECT date, branch_name, sum_credit
                    FROM usable_credit_cube
                    WHERE TO_DATE(date, 'DD/MM/YYYY') = CURRENT_DATE
                    ''')

daily_final_credit_cmd = ('''SELECT branch_name,final_credit,tr_ge_date
                    FROM final_credit_cube
                    WHERE TO_DATE(tr_ge_date, 'YYYY-MM-DD') = CURRENT_DATE
                    ''')


daily_transactions_cmd = (''' SELECT *
                    FROM transaction_cube
                    WHERE TO_DATE(date, 'YYYY-MM-DD') = CURRENT_DATE
                    ''')


daily_portfo_composition = ('''SELECT *
                    FROM portfo_composition_cube
                    where TO_DATE(date_to_ge, 'YYYY-MM') = CURRENT_DATE
                    ''')
