import csv
import os


class CardNames:

    CARD_NAMES = {}

    @staticmethod
    def __init__():
        CardNames.__init_cards_names()

    @staticmethod
    def __init_cards_names():
        os_path = os.path.abspath(os.path.dirname(__file__))
        card_names_path = os.path.join(os_path, "../resources/CARD_NAMES.csv")
        with open(card_names_path) as fp:
            reader = csv.reader(fp, delimiter=",")
            next(reader)
            for row in reader:
                CardNames.CARD_NAMES[int(row[0])] = row[1]

    @staticmethod
    def get_card_name(card_id):
        return CardNames.CARD_NAMES[card_id]


CardNames.__init__()
