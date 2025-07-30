# Sequence Flow

Sequence Flow is a small web application that allows you to easily visualize Multiple Sequence Alignments with an innovative approach - using Sankey diagrams.  
The production version is available at <https://sequenceflow.mimuw.edu.pl/>.

## How to start locally

> ✅ **Requires Python 3.10**
> 🧬 Additionally, make sure you have `clustalo` and `FastTree` installed on your system.

To start the application locally:

1. **Download** the repository.
```bash
git clone https://github.com/LeonDavisCoropuna/Sequence_AlignmentSM.git
```

2. **Create and activate a virtual environment**:

```bash
python3.10 -m venv venv
source venv/bin/activate
```

3. **Install Python dependencies**:

```bash
pip install -r requirements.txt
```

4. **Install system dependencies** for sequence alignment and tree generation:

```bash
sudo apt update
sudo apt install clustalo fasttree
```

5. **Build JavaScript assets** (you need Node.js and npm installed):

```bash
cd static/scripts
npm install
npm run build
cd ../../
```

6. **Run the Flask application**:

```bash
python3 app.py
```
