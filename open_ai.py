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
                          "word": 'words',
                          "sentence": 'sentences'
                      }},
                ],    
                "sentence_variety" : [
                      {{
                          "feedback" : "text"  
                          "word": 'word_1',
                          "sentence": 'sentence_1'
                      }},
                "subordinate_clauses" : [
                      {{
                          "feedback" : "text"  
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

    def generate_cohesion_coherence(self, topic, text):
        # AI
        cohesion_coherence = f"""
        Retrieve sentences containing strong cohesive devices from the essay. Cohesive devices encompass words or phrases that signal connections between paragraphs or sections within a text or speech. These devices include References, Conjunctions, Linking Words and Phrases, Ellipsis, Substitution, and Parallelism. Please exclude any sentences lacking cohesive devices and refrain from returning the entire essay or any descriptive content.
        If the essay do not have any cohesive devices like however, therefore, etc. then return the empty list. You don't need to find the cohesive devices from every essay

        Returning format example, return as a json object:
        {{
                "note": 'cohesion_coherence_note' (Generate concise notes on cohesion and coherence based on the provided essay. Cohesion pertains to the grammatical and lexical elements that connect sentences and paragraphs, ensuring a smooth flow of ideas. Coherence, on the other hand, relates to the logical arrangement and clarity of these ideas. Please provide a summary of these concepts without including the entire essay.),
                "list": [
                    {{
                        "cohesive_device": 'cohesive_device_1',
                        "sentence": 'sentence_1'
                    }},

                    {{
                        "cohesive_device": 'cohesive_device_2',
                        "sentence": 'sentence_2'
                    }},
                ]
        }}

        Topic: {topic}

        Essay:
        {text}
        """

        messages = [
            {"role": "system", "content": f"{self.system_role}"},
            {"role": "user", "content": f"{cohesion_coherence}"},
        ]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        self.cohesion_coherence = json.loads(response["choices"][0]["message"]["content"].strip())
        print(self.cohesion_coherence)
# text = "Dear Sir / Madam,\n\nI am writing to you as I recently received a letter from you informing me that the insurance premium for my car is going to increase from next month.\n\nAs you will be aware if you check my records, I have held my insurance with your company for nearly seven years now. During this time, I have never had an accident and never had any reason to make a claim on my insurance.\n\nI understand that at times prices need to be increased. However, this increase you are suggesting will result in a 20% increase in the amount I pay each month, a rate I feel is too much.\n\nI would therefore like you to write back to me and explain why such an increase has been proposed. If you are unable to justify it to my satisfaction, then I am afraid that I will have no other option but to move my insurance to another company.\n\nI look forward to hearing from you,Yours faithfully,\n\nJay"
text = """Dear Sir / Madam,

I am writing to you as I recently received a letter from you informing me that the insurance premium for my car is going to increase from next month.

As you will be aware if you check my records, I have held my insurance with your company for nearly seven years now. During this time, I have never had an accident and never had any reason to make a claim on my insurance.

I understand that at times prices need to be increased. However, this increase you are suggesting will result in a 20% increase in the amount I pay each month, a rate I feel is too much.

I would therefore like you to write back to me and explain why such an increase has been proposed. If you are unable to justify it to my satisfaction, then I am afraid that I will have no other option but to move my insurance to another company.

I look forward to hearing from you,

Yours faithfully,

Jay"""
# text = "Dear Sir / Madam, I am writing to you as I recently received a letter from you informing me that the insurance premium for my car is going to increase from next month. As you will be aware if you check my records, I have held my insurance with your company for nearly seven years now. During this time, I have never had an accident and never had any reason to make a claim on my insurance. I understand that at times prices need to be increased. However, this increase you are suggesting will result in a 20% increase in the amount I pay each month, a rate I feel is too much. I would therefore like you to write back to me and explain why such an increase has been proposed. If you are unable to justify it to my satisfaction, then I am afraid that I will have no other option but to move my insurance to another company. I look forward to hearing from you,Yours faithfully, Jay"
topic = 'Currently there is a trend towards the use of alternative forms of medicine. However, at best these methods are ineffective, and at worst they may be dangerous.To what extent do you agree with this statement?'
cv = OpenAiChat()
cv.generate_cohesion_coherence(topic=topic,
                  text=text)
