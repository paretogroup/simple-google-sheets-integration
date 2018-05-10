import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
pp = pprint.PrettyPrinter()

def get_spreedsheat_pareto(name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    return client.open(name)

sheet = get_spreedsheat_pareto('Descomplica_5444631325_2018-03-14_searchterms.csv')

sheet1 = sheet.sheet1
result = sheet1.col_values(3)
result = set(result)

pp.pprint(result)
