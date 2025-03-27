# CS50 AI Parser

Parser for natural language sentences using context-free grammar to determine sentence structure. The project focuses on extracting noun phrases and understanding sentence meaning through the application of grammar rules. This approach enables parsing of complex sentences and identification of their components.

## Contributions

`parser.py`:

`preprocess`: This function takes a sentence as input, tokenises it into words using nltk.word_tokenize, and returns a list of lowercase words, excluding non-alphabetic words.

`np_chunk`: Given a syntax tree representing a sentence, this function identifies and returns a list of noun phrase chunks. These are subtrees labeled "NP" that do not contain other "NP" subtrees.

`NONTERMINALS`: This variable is a set of context-free grammar rules for sentence parsing, starting with the rule S ->. These rules define how nonterminal symbols like noun phrases and verbs are expanded to form valid sentences.

### Testing

A test script (`test_parser.py`) has been developed to verify the correct operation of all listed functions.

### Technologies Used

- `Unittest`
- `nltk`

### Usage

- main: `python3 parser.py data_dir`
- test: `python3 test_parser.py`