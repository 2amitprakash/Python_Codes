import common.connect_soch as conn
import pandas as pd
import datetime
import pandas.io.formats.excel

def fetch_data():
    sql = 'SELECT s.name AS "State" , \
             d.name AS "District" , \
             div.name as "Division" , \
             ft.facility_type_name AS "Facility_Type" , \
             f.name AS "Facility" , \
             st.transaction_date as "Transaction_Date" , \
             p.product_name AS "Product_name" , \
             uom.uom_name AS "UOM" , \
             sum(fs.current_quantity) AS "Total_Qty" , \
             st1.Qty AS "Consumption_per_month" , \
             round(sum(fs.current_quantity) / nullif(st1.Qty, 0), 2) AS "Months_of_Inventory" , \
             fs.batch_number AS "Batch_No" , \
             fs.expired_date AS "Batch_Expiry" , \
             fs.current_quantity AS "Quantity" \
      FROM facility_stock_tracking AS st \
      JOIN facility AS f ON (st.facility_id = f.id) \
      JOIN product AS p ON (st.product_id = p.id) \
      JOIN facility_stock_tracking_type AS stp ON (st.type_id = stp.id) \
      JOIN facility_type AS ft ON (f.facility_type_id = ft.id) \
      JOIN address AS a ON (f.address_id = a.id) \
      JOIN STATE AS s ON (a.state_id = s.id) \
      JOIN district AS d ON (a.district_id = d.id) \
      JOIN division AS div ON (f.division_id = div.id) \
      JOIN facility_stock AS fs ON (st.batch_number = fs.batch_number) \
      JOIN product_uom_master AS uom ON (p.uom_id = uom.id) \
      JOIN \
        (SELECT cast(sum(st.quantity)/6 as numeric) as Qty , \
                st.product_id , \
                st.facility_id \
         FROM facility_stock_tracking AS st \
         JOIN facility_stock_tracking_type AS stp ON (st.type_id = stp.id) \
         WHERE stp.type LIKE '"'%dispensation%'"' \
           AND CAST((cast(CURRENT_DATE as date) - st.transaction_date) DAY AS NUMERIC) <= 180 \
         GROUP BY st.product_id, \
                  st.facility_id \
         UNION SELECT 0 AS Qty , \
                      st.product_id, \
                      st.facility_id \
         FROM facility_stock_tracking AS st \
         JOIN facility_stock_tracking_type AS stp ON (st.type_id = stp.id) \
         WHERE stp.type NOT LIKE '"'%dispensation%'"' \
         GROUP BY st.product_id, \
                  st.facility_id) AS st1 ON (st1.product_id = st.product_id \
                                             and st1.facility_id = st.facility_id) \
      where st.is_active IN ('"'true'"') \
        and s.is_active IN ('"'true'"') \
        and d.is_active IN ('"'true'"') \
        and ft.is_active IN ('"'true'"') \
        and f.is_active IN ('"'true'"') \
        and p.is_active IN ('"'true'"') \
        and uom.is_active IN ('"'true'"') \
        and fs.is_active IN ('"'true'"') \
        and stp.is_active IN ('"'true'"') \
        and div.is_active in ('"'true'"') \
      GROUP BY s.name , \
               d.name , \
               div.name , \
               ft.facility_type_name , \
               f.name , \
               p.product_name , \
               uom.uom_name , \
               st1.Qty , \
               fs.batch_number , \
               fs.expired_date , \
               fs.current_quantity , \
               st.transaction_date \
      ORDER BY p.product_name, \
                uom.uom_name, \
                st1.Qty, \
                fs.batch_number'
    #Execute query
    dataframe = pd.read_sql(sql, conn.connect())
    if dataframe.empty:
        print('DataFrame is empty!')
        xl_df = dataframe
    else:
        #Select the columns for excel report
        xl_df = dataframe[['Product_name','UOM','Total_Qty','Consumption_per_month',\
                    'Months_of_Inventory','Batch_No','Batch_Expiry','Quantity']]
    return xl_df

def create_file():
    # Current date
    now = datetime.datetime.now()
    pref = now.strftime('%Y-%m-%d')
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    pd.io.formats.excel.ExcelFormatter.header_style = None
    writer = pd.ExcelWriter('reports//daily-inventory-report-'+ pref + '.xlsx', engine='xlsxwriter')    
    return writer 

def get_col_widths(dataframe):
    # First we find the maximum length of the index column   
    idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
    # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
    return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

def add_formatting(df, writer):
    # Get the xlsxwriter workbook and worksheet objects.
    #workbook  = writer.book
    worksheet = writer.sheets['Daily Inventory Report']

    #Set the format to deafult for the index field
    #index_format = workbook.add_format({'bold': False, 'border': 0})
    # Set the column width and format.
    #worksheet.set_column('A:A', 4.55, index_format)
    #worksheet.set_column('B:B', 79.55)
    
    # set the width of the columns as per the max data width
    for i, width in enumerate(get_col_widths(df)):
        worksheet.set_column(i, i, width)
    #Set some custom width
    worksheet.set_column('E:E', 23.55)

def create_header(writer):
    # Get the xlsxwriter workbook and worksheet objects.
    workbook  = writer.book
    worksheet = writer.sheets['Daily Inventory Report']
    create_date = datetime.datetime.now().strftime('%d %b %Y - %H:%M %p') 
    # worksheet.write(0, 0, 'Daily Inventory Report for MCH, Thiruvananthapuram generated on ' \
    #                   + create_date)
    # Create a format to use in the merged range.
    merge_format = workbook.add_format({
        'font_size': 15,
        'bold': 1,
        'align': 'left'})                  
    # Merge 3 cells.
    worksheet.merge_range('A1:K1', 'Daily Inventory Report for MCH, Thiruvananthapuram generated on ' \
                      + create_date, merge_format)
    header_list = ['#', 'Product Name', 'UOM', 'Total Qty', \
                  'Monthly Consumption Rate',	'Months of Inventory', \
                  'Batch No.', 'Expiry', 'Quantity','','']
    header_format = workbook.add_format({
                          'bold': 1,
                          'valign': 'middle',
                          'fg_color': '#E1DFDE'})
    worksheet.write_row(2,0,header_list,header_format)

# To create the report
def create_report():
    #Get dataframe
    df = fetch_data()
    wr = create_file()
    # Write the dataframe without the header
    df.index += 1 # print index starting from 1
    df.to_excel(wr, sheet_name='Daily Inventory Report',
             startrow=3, startcol=0, header=False, index=True)
    #Format the sheet
    add_formatting(df, wr)
    #Write the header
    create_header(wr)

    #Save the file
    wr.save()
    print ('*** Excel report created.')
    #print(df) 

# Test the Function        
if __name__=="__main__":
    create_report()