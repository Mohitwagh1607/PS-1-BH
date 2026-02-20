from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/index', methods=['GET'])
def get_gifts():
    # 1. This grabs the input from the user's screen
    age = request.args.get('age', 'Unknown')
    hobbies = request.args.get('hobbies', 'their interests')
    budget = request.args.get('budget', 'your budget')
    
    # 2. This dynamic logic builds specific, crash-proof suggestions
    gifts = [
        f"A premium tool, starter kit, or accessory specifically for {hobbies}.",
        f"A highly-rated book or masterclass about {hobbies} perfect for a {age}-year-old.",
        f"A customized {hobbies} gift basket that fits exactly within your {budget} limit.",
        f"Tickets to a local event, workshop, or convention related to {hobbies}.",
        f"A personalized, engraved keepsake celebrating their passion for {hobbies}."
    ]
    
    # 3. This sends the 5 gifts back to the webpage
    return jsonify({"gifts": gifts})