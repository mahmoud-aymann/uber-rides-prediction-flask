# Uber Rides Prediction (Flask + scikit-learn)

![CI](https://img.shields.io/github/actions/workflow/status/mahmoud-aymann/uber-rides-prediction-flask/ci.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-green)

Modern Flask app to predict weekly Uber rides based on simple inputs. Styled with an Uber-like theme and ready for deployment.

## Features
- Flask backend serving a scikit-learn model (`model.pkl`)
- Clean, responsive UI with labeled inputs and result card
- Production-ready setup: `wsgi.py`, `Procfile`, `.gitignore`, relative model path
 - Easy deploy on Render/Railway/Heroku

## Local Setup
```bash
python -m venv venv
venv\Scripts\activate           # Windows
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```

## Project Structure
```
├── app.py
├── wsgi.py
├── model.pkl                # not committed, keep locally
├── requirements.txt
├── Procfile                 # for Gunicorn/Platform-as-a-Service
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── Uber.jpg
│   └── js/
│       └── script.js
└── .gitignore
```

## GitHub: What to Commit
Commit code, templates, and static assets. Do NOT commit big data/model files. This repo ignores `*.pkl` by default; share your `model.pkl` via Releases, Drive, or retrain script.

## Flask Highlights
- Simple routes: `/` (form) and `/predict` (inference)
- Jinja templates and static assets for clean UX
- Model loaded once from relative path for portability
- Ready for JSON API switch if needed

## Deploy (Render / Railway)
These platforms support Python + Gunicorn easily.

1) Push to GitHub.
2) Create a new Web Service from your repo.
3) Build command: `pip install -r requirements.txt`
4) Start command: `gunicorn wsgi:app --bind 0.0.0.0:$PORT`
5) Add environment variables as needed:
   - `FLASK_DEBUG=0`

The service will expose a public URL once deployed.

## Heroku (Alternative)
Heroku needs a `Procfile` (already added):
```
web: gunicorn wsgi:app --bind 0.0.0.0:${PORT}
```
Steps:
```bash
heroku login
heroku create your-uber-ml
git push heroku main
heroku open
```

## Notes
- `app.py` loads `model.pkl` from the project root by relative path.
- For private models, consider storing the artifact in object storage and downloading at startup.
- For AJAX responses, adapt `/predict` to return `jsonify` and update `static/js/script.js` accordingly.

## Screenshots / Demo
Add screenshots of the UI and (optionally) a deployment URL demo here.

