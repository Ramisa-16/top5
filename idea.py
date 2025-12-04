import openai
import ast

openai.api_key = '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'

def ideas(Temperature, Weather_Condition, Day, Time, category):
    """
    Generates 10 location-based ideas based on the weather, temperature, day, time, and category.
    CATEGORY can be one of: 'restaurant', 'cafe', 'bar', 'activity', 'service'.
    The ideas will include terms like 'near me', '1 km', or '500 meters'.
    """
    
    prompt = f"""
    Based on these details -- 
    Temperature: {Temperature}°C, 
    Weather Condition: {Weather_Condition}, 
    Day: {Day}, 
    Time: {Time}, 
    Category: {category},

    Provide 10 relevant(short(maximum 5 words) and smart) and interesting ideas for someone who is looking for {category}.
    The suggestions should be suitable for the given weather and time of day. The ideas should be location-based, with a focus on proximity to the user, using terms like 'near me', '1 km', or '500 meters'.
    
    Output format: ["", "", "", "", "", "", "", "", "", ""]
    Note: Always give exactly 10 ideas. Do not include numbering (e.g., 1., 2.).
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    
    suggestions = response['choices'][0]['message']['content']
    try:
        idea_list = ast.literal_eval(suggestions)
    except (ValueError, SyntaxError):
        idea_list = ["No suggestion available"] * 10

    while len(idea_list) < 10:
        idea_list.append("No suggestion available")  
    idea_list = idea_list[:10]

    return idea_list

Time = "12:12 PM"  
Temperature = "31°C" 
Weather_Condition = "Clear Sky"  
Day = "Monday"  
category = "restaurant"  

ideas_list = ideas(Temperature, Weather_Condition, Day, Time, category)
print(ideas_list)