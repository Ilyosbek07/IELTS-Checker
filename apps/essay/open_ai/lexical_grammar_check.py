import language_tool_python
import enchant
import spacy
from nltk.corpus import wordnet
from dataclasses import dataclass


@dataclass
class Highlight:
    essay: str = ""

    def __init__(self, essay):
        self.essay = essay
        self.split_essay = self.essay.split()
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = self.nlp(self.essay)

    def tool_adjective_adverb_words(self):
        adjectives = set([word.text for word in self.doc if word.pos_ == "ADJ"])
        adverbs = set([word.text for word in self.doc if word.pos_ == "ADV"])
        return list(adverbs), list(adjectives)

    def tool_repetitive_words(self):
        excluded_word_types = [
            "ADP",
            "AUX",
            "DET",
            "INTJ",
            "PART",
            "PRON",
            "PROPN",
            "PUNCT",
            "SYM",
            "SPACE",
        ]
        repeated_words = dict()
        list_format_of_essay = (
            self.essay.replace(",", "").replace(".", "").replace("!", "").split()
        )
        for word in self.doc:
            if (
                    word.pos_ not in excluded_word_types
                    and not word.is_stop
                    and list_format_of_essay.count(word.text) > 2
                    and word.text not in repeated_words.keys()
            ):
                repeated_words[word.text] = self.tool_get_synonyms(word.text)
        return repeated_words

    def tool_spell_checker(self):
        essay = self.essay.replace(",", " ").replace(".", " ").replace("’", "")
        misspelled_words = dict()
        dictionary = enchant.Dict("en_US")
        words = essay.split()
        for word in words:
            if not dictionary.check(word):
                misspelled_words[word] = dictionary.suggest(word)[:3]
        return misspelled_words

    def tool_get_synonyms(self, word):
        return list(
            set(
                [
                    lemma.name().replace("_", " ")
                    for syn in wordnet.synsets(word)
                    for lemma in syn.lemmas()
                    if lemma.name() != word
                ]
            )
        )[:4]

    def tool_compound_sentences(self):
        compound_sentences = set([str(word) for word in self.doc if word.dep_ == "cc"])
        return list(compound_sentences)

    def tool_subordinating_clause(self):
        subordinate_clauses = []
        for sentence in self.doc.sents:
            for token in sentence:
                if token.dep_ == "mark":
                    subordinate_clauses.append([sentence.text, token.text])
        return subordinate_clauses

    def tool_grammar_check(self):
        tool = language_tool_python.LanguageTool("en-US")
        matches = tool.check(self.essay)
        incorrect_grammar = {match.context: match.replacements for  match in matches}
        return incorrect_grammar

    def response(self):
        data = {
            'adverb': self.tool_adjective_adverb_words()[0],
            'adjective': self.tool_adjective_adverb_words()[0],
            'grammar_check': self.tool_grammar_check(),
            'subordinating_clause': self.tool_subordinating_clause(),
            'compound_sentences': self.tool_compound_sentences(),
            'spell_checker': self.tool_spell_checker(),
            'repetitive_words': self.tool_repetitive_words(),
        }
        return data
