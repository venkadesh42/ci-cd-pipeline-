from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
        </head>
        <body>
            <h1>Welcome to DevOps CI/CD Pipeline</h1>
            <h2>Application version 2.0</h2>
            <p>Git → GitHub → Jenkins → Docker → AWS EC2</p>
            <p>Monitoring: Prometheus → Grafana</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "devops-webapp"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
