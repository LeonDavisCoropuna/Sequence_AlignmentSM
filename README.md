# Sequence Flow

Sequence Flow is a small web application that allows you to easily visualize Multiple Sequence Alignments with an innovative approach - using Sankey diagrams.  
The production version is available at <https://sequenceflow.mimuw.edu.pl/>.

## How to start locally

__(Should be used with Python 3.11)__  
In order to start the application:

1. Download the repository.
2. It's recommended to create a virtual Python environment and activate it.
3. Install the Python packages from the `requirements.txt` file:

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

4. Install and build the JavaScript dependencies. You need to have Node.js and NPM installed:

```bash
cd static/scripts
npm i
npm run build
cd ../../
```

5. Run the application:

```bash
python3 app.py
```
