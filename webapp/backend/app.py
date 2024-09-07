import random
from collections import Counter, defaultdict

from flask import Flask, request, send_from_directory, jsonify
from flask_cors import cross_origin, CORS

# from javfinder.common.setting import DataDir

app = Flask(__name__, static_folder="static")
CORS(app)


# @app.route("/")
# def serve_index():
#     return send_from_directory(app.static_folder, 'index.html')
#
#
# @app.route("/<path:path>")
# def serve_static(path):
#     return send_from_directory(app.static_folder, path)

@app.route('/api/get_violin', methods=['GET'])
@cross_origin(origins="*")
def get_violin():
    with open("../../watched", "r") as f:
        content = f.readlines()
    results = defaultdict(list)
    for item in content:
        results[item.split(",")[0]].append(int(item.split(",")[2]))

    violin_data = []
    for key, value in results.items():
        violin_data.append(
            {'y': value, 'type': 'violin', 'name': key + "_t", 'box': {'visible': True, }, 'meanline': {'visible': True
                                                                                                       }})
    return violin_data


# @app.route('/api/get_actors', methods=['POST'])
# @cross_origin(origins="*")
# def get_actors():
#     year_param = request.get_json()['value']
#     with open(f"{DataDir}/watched", "r") as f:
#         content = f.readlines()
#
#     actors = []
#     for item in content:
#         year = item.split(",")[2].split("-")[0]
#         if year_param.strip() == year.strip():
#             actors += item.split(",")[5].split()
#
#     results = []
#     for key, value in sorted(Counter(actors).items(), key=lambda x: x[1]):
#         results.append({"name": key, "value": value})
#     results = results[-20:]
#     random.shuffle(results)
#
#     return results


# @app.route('/api/get_avids', methods=['POST'])
# @cross_origin(origins="*")
# def get_avids():
#     params = request.get_json()
#     year_param = params['year']
#     actor_param = params['actor']
#
#     with open(f"{DataDir}/watched", "r") as f:
#         content = f.readlines()
#
#     results = []
#     for item in content:
#         year = item.split(",")[2].split("-")[0]
#         if year_param.strip() == year.strip():
#             if actor_param in item.split(",")[5]:
#                 results.append(item)
#
#     return [{"id": item.split(",")[1].strip(), "count": item.split(",")[4].strip(), "date": item.split(",")[0].strip(),
#              "img": item.split(",")[1].replace("-", "").strip().lower(),
#              "tag": item.split(",")[6].split()} for item in results]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
