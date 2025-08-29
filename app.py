from flask import Flask, jsonify, request
FULL_NAME = "bhavyata_kaur"          
DOB_DDMMYYYY = "03092003"       
EMAIL_ID = "bhavyatakaur@gmail.com"       
ROLL_NUMBER = "22BCE1580"         

app = Flask(__name__)
def parse(data):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    numeric_sum = 0
    alphabet_chars = []  

    for item in data:
        item_str = str(item)

        if item_str.isdigit():
            num_value = int(item_str)
            numeric_sum += num_value
            if num_value % 2 == 0:
                even_numbers.append(item_str)
            else:
                odd_numbers.append(item_str)
        elif item_str.isalpha():
            alphabets.append(item_str.upper())
            alphabet_chars.extend(list(item_str))
        else:
            special_characters.append(item_str)
            for ch in item_str:
                if ch.isalpha():
                    alphabet_chars.append(ch)

    reversed_chars = list(reversed(alphabet_chars))
    concat_chars = []
    for idx, ch in enumerate(reversed_chars):
        if idx % 2 == 0:
            concat_chars.append(ch.upper())
        else:
            concat_chars.append(ch.lower())
    concat_string = "".join(concat_chars)

    return {
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(numeric_sum),
        "concat_string": concat_string,
    }


@app.route("/bfhl", methods=["POST"])
def bfhl():
    if not request.is_json:
        return jsonify({
            "is_success": False,
            "user_id": f"{FULL_NAME}_{DOB_DDMMYYYY}",
            "email": EMAIL_ID,
            "roll_number": ROLL_NUMBER,
            "message": "Invalid JSON payload"
        }), 400

    data = request.get_json()
    if "data" not in data or not isinstance(data["data"], list):
        return jsonify({
            "is_success": False,
            "user_id": f"{FULL_NAME}_{DOB_DDMMYYYY}",
            "email": EMAIL_ID,
            "roll_number": ROLL_NUMBER,
            "message": "'data' key is required and must be a list"
        }), 400

    try:
        parsed = parse(data["data"])
    except Exception as exc:
        return jsonify({
            "is_success": False,
            "user_id": f"{FULL_NAME}_{DOB_DDMMYYYY}",
            "email": EMAIL_ID,
            "roll_number": ROLL_NUMBER,
            "message": f"Error processing input: {exc}"
        }), 500

    response = {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB_DDMMYYYY}",
        "email": EMAIL_ID,
        "roll_number": ROLL_NUMBER,
        "even_numbers": parsed["even_numbers"],
        "odd_numbers": parsed["odd_numbers"],
        "alphabets": parsed["alphabets"],
        "special_characters": parsed["special_characters"],
        "sum": parsed["sum"],
        "concat_string": parsed["concat_string"],
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)