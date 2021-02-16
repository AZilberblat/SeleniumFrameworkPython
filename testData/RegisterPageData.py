import pandas as pd
class RegisterPageData:

    test_register_data = [{"firstName": "Abraham", "lastName": "Gilbert", "email": "testing457dhg54@gmail.com", "password": "abcd1234"}]

    outputs = {"success": "כיף שהצטרפתם אלינו! החיים הטובים מתחילים כאן"}
    @staticmethod
    def getTestData():
        dfs = pd.read_excel(r"C:\Users\abraham.zilberblat\PycharmProjects\SeleniumFramework\testData\registerData.xlsx")
        listOfData = []
        for item in data_dict.values():
            print(item)
            listOfData.append(item)
        return  listOfData



# {"firstName": "Levi", "lastName": "Gilbert", "email": "tesfhtin1278@gmail.com", "password": "abcd1234"} test