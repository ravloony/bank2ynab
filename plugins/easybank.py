from bank2ynab import B2YBank
import re


class EasyBank(B2YBank):
    def __init__(self, config_object, is_py2):
        super(EasyBank, self).__init__(config_object, is_py2)
        self.name = "EasyBank"
        pattern = r"^(?P<reference>.*)" \
            "(?P<type>MC|FE|VD|BG|OG|BX|VB|AT|ZE)\/\d+" \
            "(?P<extra>.*)$"
        self.regex = re.match(pattern)

    def _auto_memo(self, row):
        """ auto fill empty memo field with payee info
        :param row: list of values
        """
        payee_index = self.config["output_columns"].index("Payee")
        memo_index = self.config["output_columns"].index("Memo")

        payee = self._parse_payee_from_memo(row[memo_index])

        row[payee_index] = payee

        return row

    def _parse_payee_from_memo(self, memo):
        groups = self.regex.groupdict(memo)


def build_bank(config, is_py2):
    return EasyBank(config, is_py2)
