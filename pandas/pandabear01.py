

import pandas as pd

excel_file = "movies.xls"

movies_sheet1 = pd.read_excel(excel_file,sheet_name=0, index_col=0)
movies_sheet2 = pd.read_excel(excel_file,sheet_name=1, index_col=0)
movies_sheet3 = pd.read_excel(excel_file,sheet_name=2, index_col=0)


movies= pd.concat([movies_sheet1,movies_sheet2,movies_sheet3])

movies= movies.drop_duplicates()
big_bucks = movies.sort_values(["Gross Earnings"], ascending =False)
print(big_bucks.head(10))
