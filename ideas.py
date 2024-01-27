def generate_ideas(client, count):

    prompt = f"""I want to create multiple short videos.

    The videos will be static images of animals with added commentary.

    The images should be energetic, colorful and realistic-looking.
    They should picture animals doing something that they would never do in the real world.

    A good example would be a rhino with a top hat and nice suit playing the saxophone in the jungle. 
    Another good example would be a hummingbird practicing karate on a dummy.

    The commentary should be a real fact about the animal on the picture.    
    The commentary should always start with "Did you know that ".
    The commentary should not be too short, it should be about 8 seconds to read by a human.
    
    The fact should be something less known.
    A bad example of a fact would be "elephant is the largest land animal", since it is very widely know and easily observable fact.
    A good example of a fact would be "octopuses can taste with their arms".
    From time to time, you can throw in a "useless" fact - something, that is obviously true and a bit funny (for example: "rhinos can't drive a truck since they don't have a driver's license" or "raccoons breathe air because they need it to survive").

    Given the examples, please generate {count} (IMPORTANT! the exact count) similar video ideas with different animals. 
    There can be multiple ideas with the same animal, but the fact about the animal and the picture idea should be different every time.
    IMPORTANT! Please don't repeat the same fact!

    One third of the pictures should be about aquatic life, second third should be about smaller life (like rodents, pets or bugs) and the final third should be about birds.

    The generated ideas should be formatted like this:
    n|a|b|c
    where n is the order number of the idea, a is short description of the picture formatted using snake case, b is the idea for the picture and c is the fact
    """

    chat_completion = client.chat.completions.create(
        messages=[
        {
                "role": "user",
                "content": prompt,
        }
        ],
        model="gpt-4", # or gpt-3.5-turbo
    )

    with open('output/list_of_ideas.txt', 'w') as file:
        for c in chat_completion.choices:
            file.write(c.message.content.strip())

    print(f'[info] ideaGenerator has successfully generated {count} ideas')