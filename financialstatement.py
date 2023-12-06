## This is the class for calling financial statement data
import requests
import logging
from typing import Optional


class FinancialStatement():

    def __init__(self) -> None:
        """ 
        set endpoint and key. key is hardcoded here because we assume only using this key.
        """

        self.key = "ENTER YOUR KEY"
        self.key_q = "&apikey=" + self.key
        self.endpoint = "https://financialmodelingprep.com/api/v3/"
        
        
    def get_statement(self, statement_type: str, period: str, company_symbol: str, limit: Optional[int] = None) -> list[dict]:
        """ Return statement for the last five years. Free API can only give last five years' data. 

        Parameters
        ----------
        company_symbol: str
            company symbol according to NASDAQ or sth. Ex: apple is not "apple". Apple company's company_symbol here is "AAPL"
        period: str
            statement can be annual statement or quarter statement. we specify "annual" or "quarter" here.
        limit: int
            max number of output statements 
        statement_type: str
            expect string input. "income"/"cash flow"/"balance sheet"

        Return
        ----------
        statement: list[dict]
            the requested statement. Ex: shows only two statements: the apple annual cash flow statement 
            result: list[dict{apple 2023}, dict{apple 2022}]
        """
        
    
        statement_type = self.get_statement_type_str(statement_type)
        period_q = "period="+ period
        query = self.endpoint + statement_type + "/" + company_symbol + "?" + period_q + self.key_q 
        if limit is not None: query = query + "&limit=" + str(limit)
        response = requests.get(query)
        logging.info("Query Response Status (200 is good): "+str(response.status_code))

        statements=response.json()
        return statements
    
    def get_statement_type_str(self, statement_type: str) -> str:
        """ Return statement type(str) in the format that fits query.

        Parameters
        ----------
        statement_type: str
            expect string input. "income"/"cash flow"/"balance sheet"

        Returns
        ----------
        statement type in query format: str
        """
        if statement_type == "income": 
            return "income-statement"
        elif statement_type == "cash flow":
            return "cash-flow-statement"
        elif statement_type == "balance sheet":
            return "balance-sheet-statement"
        else:
            logging.warning("Unidentifiable statement type has been given")


def main():
    ## Set logger
    logging.basicConfig(level=logging.INFO)

    fs = FinancialStatement()
    statement=fs.get_statement(statement_type="cash flow", period="annual", company_symbol="AAPL", limit=2)
    print(statement)

if __name__ == "__main__":
    main()
        
