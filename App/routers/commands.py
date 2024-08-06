
# SQLs commands string to be executed against the database

future_settlements_cmd = ('DECLARE @StartDate DATE = dateadd(day, 2, CAST(GETDATE() AS DATE));'
                          'DECLARE @EndDate DATE = dateadd(day, -4, CAST(GETDATE() AS DATE)); '
                          'SELECT SUM(Amount),COUNT(Amount) ,CAST( RequestDate AS DATE)'
                          'FROM [HamtaDb].[dbo].[PaymentRequests] '
                          'WHERE [RequestDate] >= @EndDate AND [RequestDate] <= @StartDate '
                          'GROUP BY RequestDate '
                          'ORDER BY RequestDate asc')


customer_remain_cmd = (
                       'SELECT  SUM(f.remain) AS total_remain, customer_data.branch_id, customer_data.branch_name '
                       'FROM financial_status_data f '
                       'INNER JOIN customer_data ON customer_data.account_number = f.account_number '
                       'GROUP BY customer_data.branch_id, customer_data.branch_name ORDER BY total_remain;')



