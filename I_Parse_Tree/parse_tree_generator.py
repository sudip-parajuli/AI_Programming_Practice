import nltk
from nltk import CFG
from nltk.parse.generate import generate
from nltk.parse.chart import ChartParser

# Download required NLTK data (run once)
nltk.download('punkt_tab')

# Define a simple context-free grammar (CFG)
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP
VP -> V NP | VP PP
PP -> P NP
Det -> 'a' | 'the'
N -> 'man' | 'dog' | 'mat' | 'telescope'
V -> 'saw' | 'sat'
P -> 'on' | 'with'
""")

# Create a parser using the grammar
parser = ChartParser(grammar)

# Function to parse and draw the tree
def generate_parse_tree(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    print("\nTokens:", tokens)

    trees = list(parser.parse(tokens))
    if not trees:
        print("No valid parse tree could be generated for this sentence.")
        return

    for tree in trees:
        print("\nParse Tree:")
        print(tree)
        tree.pretty_print()


# Main function
if __name__ == "__main__":
    print("Enter a sentence (e.g., 'the man saw a dog with a telescope'):")
    user_input = input("> ")
    generate_parse_tree(user_input)
