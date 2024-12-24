from find_in_file import main_process
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search-all-files", methods=["GET"])
def search():
    keyword = request.args.get("keyword", type=str)

    if keyword is None:
        return jsonify({"error": "Missing or invalid parameter \'keyword\'."}), 400
    not_found = "keyword was not found in the files"
    result = main_process(keyword)
    return jsonify({"keyword": keyword, "files_found": (result if result else not_found)}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)