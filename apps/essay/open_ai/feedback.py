import json

import openai

class Feedback:
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

    def generate_cohesion_coherence(self):
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

        Topic: {self.topic}

        Essay:
        {self.essay}
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

        return json.loads(response["choices"][0]["message"]["content"].strip())

    def generate_tone_feedback(self):
        overall_feedback = f"""
        Identify the Formal and Informal tone of the IELTS Letter General Training Writing Task 1.
        Difference between Formal and Informal tone:
        Formal tone: The choice of words, the tone utilized, academic vocabulary, proper sentences, well-elaborated and clear sentences, avoiding the use of emotional language and jargons, avoiding grammatical, punctuation, and spelling mistakes, use of correct references.
        Informal tone: The writer can use short sentences, the writer can use abbreviated words, they are subjective and personal, they are an effective way of addressing things casually, the writer can either use the first or second pronoun, the writer can use imperative of simple sentences.

        Returning format example, return item as a json object:
        
        "note": 'tone_feedback_note' (Note for Formal and Informal tone of the IELTS Letter General Training Writing Task 1)
        {{  
            "formal": [
                {{
                    "word": 'word_1',
                    "sentence": 'sentence_1'
                }},
            ],

            "informal": [
                {{
                    "word": 'word_2',
                    "sentence": 'sentence_2'
                }},
            ]
        }}

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

    def response(self):
        data = [
            self.generate_cohesion_coherence(),
            self.generate_tone_feedback()
        ]
        return data


topic = """
The concept of creating vertical cities with towering skyscrapers to accommodate urban expansion has been proposed, and in some cases, materialised in many cities around the world. While there are benefits to this approach, it also presents several disadvantages, and this essay will explore both.
"""
text = """
The concept of creating vertical cities with towering skyscrapers to accommodate urban expansion has been proposed, and in some cases, materialised in many cities around the world. While there are benefits to this approach, it also presents several disadvantages, and this essay will explore both.

One of the key advantages of vertical cities is their potential to maximize land usage efficiently. With limited available land for urban growth, constructing tall buildings allows for increased population density without further encroaching on natural spaces. For instance, cities like Hong Kong and New York have embraced vertical living to accommodate their growing populations while preserving green spaces and minimizing urban sprawl.

Another benefit lies in the potential reduction of commuting times. Vertical cities can centralize various services and amenities within close proximity, minimizing the need for extensive travel within the city. Residents can easily access workplaces, shopping centres, and recreational facilities without enduring long commutes. This efficiency in commuting can contribute to improved work-life balance and reduced environmental pollution.

However, the drawbacks of living in vertical cities should not be overlooked. Tall buildings can create a sense of isolation and disconnect among residents due to limited outdoor spaces and a lack of community areas. The absence of shared public spaces like parks and open squares may hinder social interactions and impede the development of a cohesive urban community. For instance, studies have shown that high-rise living can lead to feelings of loneliness and social detachment among residents.

Furthermore, the overreliance on vertical expansion could lead to environmental concerns. Tall buildings require extensive energy consumption for heating, cooling, and vertical transportation systems. The sheer height of these structures can exacerbate the urban heat island effect and increase energy consumption, potentially offsetting the environmental benefits of reducing horizontal urban sprawl.

In conclusion, vertical cities with towering buildings revolve around a range of advantages and disadvantages. While efficient land use and reduced commuting times are potential benefits, concerns related to community cohesion, social interaction, and environmental sustainability warrant careful consideration when planning for such urban developments.

"""
