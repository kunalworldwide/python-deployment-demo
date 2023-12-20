from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the HTML content of the single static webpage
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GDG DF 23 DevOps DEMO</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        @keyframes breather {
            0%, 100% {
                transform: scale(1);
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            50% {
                transform: scale(1.05);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
        }

        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Roboto', sans-serif;
            position: relative;
            background: linear-gradient(white 10%, #4285f4 10%, #4285f4 90%, white 90%); /* Adjusted gradient */
        }

        .logo {
            position: absolute;
            top: 20px;
            left: 20px;
            height: 60px;
        }

        .button-container {
            background-color: #fbbc04;
            padding: 150px 200px;
            border-radius: 10px;
            animation: breather 2s ease-in-out infinite;
        }

        .button-container p {
            color: #000;
            font-size: 48px;
            font-weight: 700;
            margin: 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <img src="https://cdn.statically.io/gh/devfestkolkata2022/assets/c70b81ad6c87672b1da3fe763e929092170b9967/images/gdg-logo.svg" alt="GDG Logo" class="logo">
    <div class="button-container">
        <p>Random String</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Render the static HTML content
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Listen on port 8080
