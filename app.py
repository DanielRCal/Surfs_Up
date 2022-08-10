

# Import Dependency
from flask import Flask

# Create a new flask app instance
app = Flask("Daniel's Website")

# Create our flask routes

# define our root (starting point)
@app.route("/")

def hello_world():
    x = 2 + 2 

    return f'Hello {x} World'

if __name__ == '__main__':
    app.run(debug=True)