from flask import Flask, request, render_template_string
import csv
import json
import io

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <title>File Uploader</title>
</head>
<body>
    <h2>Upload JSON or CSV File</h2>
    <form method="POST" enctype="multipart/form-data" action="/uploader">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
'''


@app.route('/upload', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/uploader', methods=['POST'])
def uploader():
    if 'file' not in request.files:
        return "Invalid content type for import"

    file = request.files['file']
    filename = file.filename

    if filename.endswith('.csv'):
        try:
            stream = io.TextIOWrapper(file.stream, encoding="UTF-8")
            reader = csv.reader(stream)
            data = [row for row in reader]
            print(data)
            return "File uploaded successfully"
        except Exception:
            return "Invalid content type for import"

    elif filename.endswith('.json'):
        try:
            data = json.load(file)
            print(data)
            return "File uploaded successfully"
        except Exception:
            return "Invalid content type for import"

    return "Invalid content type for import"


if __name__ == '__main__':
    app.run(debug=True)