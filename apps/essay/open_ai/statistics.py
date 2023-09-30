import math

import language_tool_python
import nltk
import enchant
import re
import json
import openai
import spacy

from nltk.corpus import wordnet

from nltk.corpus import stopwords
from collections import Counter


# nltk.download('stopwords')


class EssayAnalyzer:
    def __init__(self, essay, topic, max_tokens: int = 1000):
        self.system_role = """
        You know everything about scoring IELTS essays. You assess the given essay of the given question and provide
        feedback to help the writer to improve in the future, and specify mistakes and suggest corrections.
        """
        self.api_key = "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"
        # self.api_key = "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"
        self.max_tokens = max_tokens
        self.temperature = 0
        self.model = "gpt-3.5-turbo-0613"
        openai.api_key = self.api_key
        self.essay = essay
        self.topic = topic
        self.split_essay = self.essay.split()
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = self.nlp(self.essay)

    def count_paragraphs(self):
        paragraphs = self.essay.split("\n\n")
        total_paragraphs = len(paragraphs)
        return total_paragraphs

    def total_words(self):
        res = re.findall(r'\w+[\'’]?\w*', self.essay)
        return len(res)

    def total_sentence(self):
        sentences = nltk.sent_tokenize(self.essay)
        length = len(sentences)
        return length

    def average_sentence(self):
        total_words = self.total_words()
        total_sentences = self.total_sentence()
        count = math.floor(total_words / total_sentences)
        return count

    def generate_feedback(self):
        overall_feedback = f"""
            Please answer these parts as accurately as possible
            Returning format example, return item as a json object:

            responce :[
                {{
                    "cohesion": choose one of this choices: COHESION_CHOICES = (('low', _('Low')),('Not Enough', _('Not Enough')),('good', _('Good')),
                }}
                {{
                    "sentence_variety": choose one of this choices: CHOICES = (('low', _('Low')),('Not Enough', _('Not Enough')),('good', _('Good')),
                }}
            ]
            Topic: {self.topic}

            Essay:
            {self.essay}

            JSON:
            """

        messages = [
            {"role": "system", "content": f"{self.system_role}"},
            {"role": "user", "content": f"{overall_feedback}"},
        ]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return json.loads(response["choices"][0]["message"]["content"].strip())

    def tool_spell_checker(self):
        essay = self.essay.replace(",", " ").replace(".", " ")
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
        # return self.repeated_words

    def analyze_essay(self):
        results = {
            "total_paragraph": self.count_paragraphs(),
            "total_sentence": self.total_sentence(),
            "total_words": self.total_words(),
            "average_sentence": self.average_sentence(),
            "word_repetition": self.tool_repetitive_words(),
            "spelling_mistakes": self.tool_spell_checker(),
            "cohesion_and_sentence_variety": self.generate_feedback()
        }
        return results

    def tool_adjective_adverb_words(self):
        adjectives = set([word.text for word in self.doc if word.pos_ == "ADJ"])
        adverbs = set([word.text for word in self.doc if word.pos_ == "ADV"])
        return list(adverbs), list(adjectives)

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
        incorrect_grammar = {match.context: match.replacements for match in matches}
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


topic = "You have recently started work in a new company.Write a letter to an English-speaking friend. In your letter explain why you changed jobs describe your new job tell him/her your other news."

text = """
Dear Tom

I’m just writing to let you know I quit my old job and found something new.

I was really fed up with being a brain surgeon because it wasn’t really much of a challenge anymore. You know me if I’m not learning new tricks, I get bored too easily and have to find something new.

I’m now teaching English as a foreign language in Vietnam and it suits me down to the ground. I teach two adult classes and a kindergarten class, which is not only challenging but also rewarding too. Can you believe it ?

I also have some other amazing news- I’m getting married. She was one of my first ever students and I guess it was love at first sight for both of us. Make sure you keep the first weekend in July free, so you can come and celebrate with us.

Keep in touch

Chris
"""
# topic = "Nowadays, money is one of the most significant elements in our lives. So, for many people, it may seem appropriate to marry for money rather than love."
#
# text = """Nowadays, money is one of the mst significant elements in our lives. So, for many people, it may seem appropriate to marry for money rather than love. Certainly, money plays an important part in our lives. It is challenging for any persons to accept a partner who does not have money, or at least a job to take care of their future family. Hence, the expression, “marry for money” seems appropriate, in some extent, at least. However, I believe that marriage should involve a combination of both love and money.
#
#             Clearly, love should be the foundation of any marriage. This is because firstly, love is such a strong bond between two persons, who have their own lives, yet become one. They can share each other’s sadness or happiness in order to overcome any difficulties in daily lives. Moreover, love fosters maturity because each member of a couple no longer has responsibility only for themselves, but also for their partner. These are just two, key reasons why marrying for love should always be encouraged.
#
#             In my opinion, love and money are equally necessary. A marriage relying solely on money might rapidly disintegrate in the unfortunate event of the money running out. Similarly, a marriage relying on love alone might sometimes come to an end if the couple could not earn enough money to manage their family’s obligations such as paying bills, or buying food. Therefore, love and money should stand together in marriage, even though their contribution might often be somewhat unequal.
#
#             To summarise, marriage without either money or love could come to an unfortunate end. For that reason, I would claim that they both make their own, vital contribution to the creation of a happy family.
#         """
# results = EssayAnalyzer(topic=topic, essay=text)
# print(results.analyze_essay())

# a = results.analyze_essay()['spelling_mistakes']
# b = len(results.analyze_essay()['spelling_mistakes'])
# print(b)
