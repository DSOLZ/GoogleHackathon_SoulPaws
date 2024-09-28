from flask import Flask, request, jsonify

app = Flask(__name__)

# Dog breeds data
dogs = [
    {"breed": "Pit Bull", "size": "Medium", "personality": ["Loyal", "Playful", "Affectionate"], "activity_level": 4, "experience_level": 4, "living_space": 2},
    {"breed": "Labrador", "size": "Large", "personality": ["Friendly", "Outgoing"], "activity_level": 5, "experience_level": 2, "living_space": 3},
    {"breed": "German Shepherd", "size": "Large", "personality": [], "activity_level": 5, "experience_level": 5, "living_space": 3},
    {"breed": "Chihuahua", "size": "Small", "personality": ["Alert", "Confident", "Lively"], "activity_level": 2, "experience_level": 3, "living_space": 1},
    {"breed": "Boxer", "size": "Large", "personality": ["Playful"], "activity_level": 5, "experience_level": 3, "living_space": 2},
    {"breed": "Dachshund", "size": "Medium", "personality": [], "activity_level": 3, "experience_level": 2, "living_space": 1},
    {"breed": "American Staffordshire", "size": "Medium", "personality": ["Courageous"], "activity_level": 4, "experience_level": 4, "living_space": 1}
]

# Function to get dog size category based on weight range
def get_size(weight):
    if weight <= 20:
        return "Small"
    elif 21 <= weight <= 60:
        return "Medium"
    else:
        return "Large"

# Function to match user with top 3 dog breeds based on preferences
def match_dog(preferred_size, preferred_personality, activity_level, experience_level, living_environment):
    results = []
    
    for dog in dogs:
        score = 0
        
        # Matching size
        if dog["size"] == preferred_size:
            score += 1
        
        # Matching personality (partial matches are also possible)
        if any(trait in dog["personality"] for trait in preferred_personality):
            score += 1
        
        # Matching activity level
        if dog["activity_level"] == activity_level:
            score += 1
        
        # Matching experience level
        if dog["experience_level"] == experience_level:
            score += 1
        
        # Matching living space (simple match)
        if dog["living_space"] == living_environment:
            score += 1
        
        # Store breed and its score in the results list
        results.append((dog["breed"], score))
    
    # Sort the results by score in descending order and return the top 3
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:3]

# API route to get the top 3 dog matches
@app.route('/match_dog', methods=['POST'])
def match_dog_api():
    try:
        data = request.json
        
        # Extract data from JSON request
        weight = data.get('weight')
        preferred_size = get_size(weight)
        
        preferred_personality = data.get('preferred_personality', [])
        activity_level = data.get('activity_level')
        experience_level = data.get('experience_level')
        living_environment = data.get('living_environment')
        
        # Call the dog matching function
        top_dogs = match_dog(preferred_size, preferred_personality, activity_level, experience_level, living_environment)
        
        # Return the top 3 dog matches as JSON response
        return jsonify({
            "status": "success",
            "matches": [{"breed": breed, "score": score} for breed, score in top_dogs]
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)


