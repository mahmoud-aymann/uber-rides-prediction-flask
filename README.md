# Uber Rides Prediction (Flask + scikit-learn)

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/flask-2.0+-green)

Modern Flask app to predict weekly Uber rides based on simple inputs. Styled with an Uber-like theme and ready for deployment.

## Demo
- Live: https://web-production-0c45c.up.railway.app/

## Features
- Flask backend serving a scikit-learn model (`model.pkl`)
- Clean, responsive UI with labeled inputs and result card
- Production-ready setup: `wsgi.py`, `Procfile`, `.gitignore`, relative model path
 - Easy deploy on Render/Railway/Heroku

## Tech Stack
- Flask, Jinja2
- scikit-learn, numpy, pandas
- Gunicorn (production server)

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
├── model.pkl                # included for deployment on free tiers
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
Commit code, templates, and static assets. For production-sized artifacts prefer Releases/Storage. `model.pkl` is included here for easy deployment on free hosting.

## Flask Highlights
- Routes: `/` (form) and `/predict` (inference)
- Jinja templates + static assets for a clean UX
- Model loaded once via relative path for portability
- Easy to switch `/predict` to JSON API if needed

## Deploy (Render / Railway)
These platforms support Python + Gunicorn easily.

1) Push to GitHub  
2) Create a new Web Service from your repo  
3) Build: `pip install -r requirements.txt`  
4) Start: `gunicorn wsgi:app --bind 0.0.0.0:$PORT`  
5) Env vars: `FLASK_DEBUG=0`

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
- For private models, consider object storage and downloading at startup.
- For AJAX, return `jsonify` from `/predict` and update `static/js/script.js`.

## Screenshots / Demo
Add screenshots of the UI here (e.g., `static/img/screenshot.png`).

