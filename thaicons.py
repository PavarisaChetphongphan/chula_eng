import random
import ipywidgets as widgets
from IPython.display import display, clear_output

# All Thai consonants and their names
thai_consonants = [
    ("ก", "gor gai"), ("ข", "kho khai"), ("ฃ", "kho khuat"),
    ("ค", "kho khwai"), ("ฅ", "kho khon"), ("ฆ", "kho rakhang"),
    ("ง", "ngo ngu"), ("จ", "cho chan"), ("ฉ", "cho ching"),
    ("ช", "cho chang"), ("ซ", "so so"), ("ฌ", "cho choe"),
    ("ญ", "yo ying"), ("ฎ", "do cha-da"), ("ฏ", "to pa-tak"),
    ("ฐ", "tho than"), ("ฑ", "tho montho"), ("ฒ", "tho phu-thao"),
    ("ณ", "no nen"), ("ด", "do dek"), ("ต", "to tao"),
    ("ถ", "tho thung"), ("ท", "tho thahan"), ("ธ", "tho thong"),
    ("น", "no nu"), ("บ", "bo baimai"), ("ป", "po pla"),
    ("ผ", "pho phueng"), ("ฝ", "fo fa"), ("พ", "pho phan"),
    ("ฟ", "fo fan"), ("ภ", "pho sam-phao"), ("ม", "mo ma"),
    ("ย", "yo yak"), ("ร", "ro ruea"), ("ล", "lo ling"),
    ("ว", "wo waen"), ("ศ", "so sala"), ("ษ", "so ruesi"),
    ("ส", "so suea"), ("ห", "ho hip"), ("ฬ", "lo chu-la"),
    ("อ", "o ang"), ("ฮ", "ho nok-huk")
]

class FlashcardApp:
    def __init__(self):
        self.current_card = None
        self.is_flipped = False

        self.label = widgets.Label(value="")
        self.flip_button = widgets.Button(description="Flip")
        self.next_button = widgets.Button(description="Next")

        self.flip_button.on_click(self.flip_card)
        self.next_button.on_click(self.next_card)

        display(self.label, self.flip_button, self.next_button)
        self.next_card()

    def next_card(self, b=None):
        self.current_card = random.choice(thai_consonants)
        self.label.value = self.current_card[0]
        self.is_flipped = False

    def flip_card(self, b=None):
        if self.is_flipped:
            self.label.value = self.current_card[0]
        else:
            self.label.value = self.current_card[1]
        self.is_flipped = not self.is_flipped

# Run the flashcard app
FlashcardApp()

