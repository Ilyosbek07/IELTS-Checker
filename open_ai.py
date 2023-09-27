import json

import openai


class OpenAiChat:
    def __init__(self, max_tokens: int = 1000):
        self.system_role = """
        You know everything about scoring IELTS essays. You assess the given essay of the given question and provide
        feedback to help the writer to improve in the future, and specify mistakes and suggest corrections.
        """
        self.api_key = "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"
        self.max_tokens = max_tokens
        self.temperature = 0
        self.model = "gpt-3.5-turbo-0613"
        openai.api_key = self.api_key

    def generate_tone_feedback(self, topic, text, letter_type):
        overall_feedback = f"""
            Identify the Formal and Informal tone of the IELTS Letter General Training Writing Task 1.
            Difference between Formal and Informal tone:
            Formal tone: The choice of words, the tone utilized, academic vocabulary, proper sentences, well-elaborated and clear sentences, avoiding the use of emotional language and jargons, avoiding grammatical, punctuation, and spelling mistakes, use of correct references.
            Informal tone: The writer can use short sentences, the writer can use abbreviated words, they are subjective and personal, they are an effective way of addressing things casually, the writer can either use the first or second pronoun, the writer can use imperative of simple sentences.

            Returning format example, return item as a json object:

             {{
                "formal": [
                    {{
                        "word": 'word_1',
                        "sentence": 'sentence_1'
                    }},
                    {{
                        "count": 'count'
                    }}
                ],

                "informal": [
                    {{
                        "word": 'word_2',
                        "sentence": 'sentence_2'
                    }},
                    {{
                        "count": 'count'
                    }}
                ]
            }}

            Topic: {topic}

            Essay:
            {text}

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
        self.tone_feedback = json.loads(
            response["choices"][0]["message"]["content"].strip()
        )

    def get_statistics(self, topic, text, letter_type):
        overall_feedback = f"""
            Identify the Requested Resired Statistics IELTS Letter General Training Writing Task 1.
            There are:
            Total paragraphs: number of letter paragraphs.
            Total words: letter words total number.
            Average Sentence: Average sentence length (avg number of words).
            Total Sentences: letter sentences total number.
            Cohesion: Determine whether the letter number of the connecting devices used is used to help achieve a high score for compatibility and coherence.
            Sentence Variety: Help you find the level of different sentence types, which is one of the most important requirements for getting a high score in writing.
            Spelling Mistakes:Return the level of spelling and typos and errors.
            Word Repetition: the examiner is looking for memorised language, phrases and clichés. Memorised language is easy to identify, so use your own words and avoid overused phrases.Count repited words

            Returning format example, return item as a json object:

            {{
                "total_paragraphs" : "number",
                "total_words" : "number",
                "average_sentence" : "number",
                "total_sentence" : "number",
                "cohesion" : "degree",
                "sentence_variety" : "degree",
                "spelling_mistakes" : "number",
                "word_repetition" : "number",
            }}

            Topic: {topic}

            Essay:
            {text}

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
        self.letter_statistic = json.loads(
            response["choices"][0]["message"]["content"].strip()
        )
        print(self.letter_statistic)

    def get_letter_report(self, topic, text, letter_type):
        overall_feedback = f"""
            Identify Report IELTS Letter General Training Writing Task 1.
            There are:
            Cohesion: Determine whether the letter number of the connecting devices used is used to help achieve a high score for compatibility and coherence.
            Sentence Variety: Help you find the level of different sentence types, which is one of the most important requirements for getting a high score in writing.
            Subordinate clauses: play a crucial role in sentence structure and overall writing quality.
            
            Returning format example, return item as a json object:

            {{
                "cohesion": [
                      {{
                          "feedback" : "text"  
                      }},
                      {{
                          "word": 'word_1',
                          "sentence": 'sentence_1'
                      }},
                ],    
                "sentence_variety" : [
                      {{
                          "feedback" : "text"  
                      }},
                      {{
                          "word": 'word_1',
                          "sentence": 'sentence_1'
                      }},
                "subordinate_clauses" : [
                      {{
                          "feedback" : "text"  
                      }}, 
                      {{
                          "word": 'word_1',
                          "sentence": 'sentence_1'
                      }},
                ],   
            }}

            Topic: {topic}

            Essay:
            {text}

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
        self.letter_report = json.loads(
            response["choices"][0]["message"]["content"].strip()
        )
        print(self.letter_report)

# text = "Dear Sir / Madam,\n\nI am writing to you as I recently received a letter from you informing me that the insurance premium for my car is going to increase from next month.\n\nAs you will be aware if you check my records, I have held my insurance with your company for nearly seven years now. During this time, I have never had an accident and never had any reason to make a claim on my insurance.\n\nI understand that at times prices need to be increased. However, this increase you are suggesting will result in a 20% increase in the amount I pay each month, a rate I feel is too much.\n\nI would therefore like you to write back to me and explain why such an increase has been proposed. If you are unable to justify it to my satisfaction, then I am afraid that I will have no other option but to move my insurance to another company.\n\nI look forward to hearing from you,Yours faithfully,\n\nJay"
text = """
Dear Sir/Madam,

I am writing to express my concern regarding the recent notification I received from your company regarding an impending increase in the insurance premium for my car, set to take effect next month.

As you may have noticed in your records, I have been a loyal customer of your company for nearly seven years. Throughout this period, I have maintained an impeccable driving record, never having been involved in any accidents or needing to file a claim.

While I understand that periodic adjustments to pricing may be necessary, I was surprised to learn that the proposed increase would result in a substantial 20% rise in my monthly premium. This significant increase has prompted me to seek clarification regarding the rationale behind this decision.

I kindly request that you provide a detailed explanation for the substantial premium hike. Understanding the factors contributing to this increase will help me make an informed decision about whether to continue my insurance coverage with your company. 

Should you be unable to provide a satisfactory justification for the proposed rate hike, I may regrettably have no choice but to explore alternative insurance options with other providers.

I eagerly anticipate your response and hope that you can shed light on the reasons for this substantial premium increase. 

Yours faithfully,

Jay
"""
# text = "Dear Sir / Madam, I am writing to you as I recently received a letter from you informing me that the insurance premium for my car is going to increase from next month. As you will be aware if you check my records, I have held my insurance with your company for nearly seven years now. During this time, I have never had an accident and never had any reason to make a claim on my insurance. I understand that at times prices need to be increased. However, this increase you are suggesting will result in a 20% increase in the amount I pay each month, a rate I feel is too much. I would therefore like you to write back to me and explain why such an increase has been proposed. If you are unable to justify it to my satisfaction, then I am afraid that I will have no other option but to move my insurance to another company. I look forward to hearing from you,Yours faithfully, Jay"
topic = 'Letter for informing that the insurance premium for the car is going to increase from next month.'
cv = OpenAiChat()
cv.get_statistics(topic=topic,
                     text=text,
                     letter_type='formal')
