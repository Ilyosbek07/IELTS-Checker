def clean_html_codes(text):
    p_clear = text.replace('<p>', '')
    paragraph = p_clear.replace('</p>', '\n\n')
    return paragraph
# from apps.essay.open_ai.lexical_grammar_check import Feedback
#
# a = Feedback(
#     essay="""
#     The concept of creating vertical cities with towering skyscrapers to accommodate urban expansion has been proposed, and in some cases, materialised in many cities around the world. While there are benefits to this approach, it also presents several disadvantages, and this essay will explore both.
#
# One of the key advantages of vertical cities is their potential to maximize land usage efficiently. With limited available land for urban growth, constructing tall buildings allows for increased population density without further encroaching on natural spaces. For instance, cities like Hong Kong and New York have embraced vertical living to accommodate their growing populations while preserving green spaces and minimizing urban sprawl.
#
# Another benefit lies in the potential reduction of commuting times. Vertical cities can centralize various services and amenities within close proximity, minimizing the need for extensive travel within the city. Residents can easily access workplaces, shopping centres, and recreational facilities without enduring long commutes. This efficiency in commuting can contribute to improved work-life balance and reduced environmental pollution.
#
# However, the drawbacks of living in vertical cities should not be overlooked. Tall buildings can create a sense of isolation and disconnect among residents due to limited outdoor spaces and a lack of community areas. The absence of shared public spaces like parks and open squares may hinder social interactions and impede the development of a cohesive urban community. For instance, studies have shown that high-rise living can lead to feelings of loneliness and social detachment among residents.
#
# Furthermore, the overreliance on vertical expansion could lead to environmental concerns. Tall buildings require extensive energy consumption for heating, cooling, and vertical transportation systems. The sheer height of these structures can exacerbate the urban heat island effect and increase energy consumption, potentially offsetting the environmental benefits of reducing horizontal urban sprawl.
#
# In conclusion, vertical cities with towering buildings revolve around a range of advantages and disadvantages. While efficient land use and reduced commuting times are potential benefits, concerns related to community cohesion, social interaction, and environmental sustainability warrant careful consideration when planning for such urban developments.
#
# """)
#
# print(a.response())
#