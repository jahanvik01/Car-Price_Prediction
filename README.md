# Car Price Prediction

## Vision
Car Price Prediction is a lightweight web application that enables users to estimate the resale value of a used car based on its characteristics. Leveraging a pre‑trained machine‑learning model, the app transforms intuitive user inputs into an instant price prediction, helping buyers, sellers, and dealers make informed decisions.

The project is built as a single‑file Streamlit app, keeping the deployment footprint minimal while providing an interactive user experience directly in the browser.

## Architecture
The repository follows a flat structure:

```
/
├─ README.md          # Project documentation
└─ app.py             # Streamlit application – loads data, model and handles inference
```

`app.py` imports:

* **pandas** – for reading the CSV dataset and constructing the input DataFrame.
* **pickle** – for deserialising the pre‑trained model (`pipeline.pkl`).
* **streamlit** – for rendering the web UI and capturing user interaction.

All computation happens in the same process: the model and dataset are loaded into memory at startup, user inputs are collected via Streamlit widgets, and the prediction is performed synchronously when the *Predict* button is pressed.

## Key Components
| Component | Role |
|-----------|------|
| `app.py` | Entry point of the application. Loads the machine‑learning pipeline, reads the reference CSV, defines the UI, and executes the prediction logic. |
| `README.md` | Source of truth documentation for developers and end‑users. |
| `pipeline.pkl` *(external)* | Serialized scikit‑learn pipeline that contains preprocessing steps and the regression model. |
| `new car.csv` *(external)* | CSV file with the original dataset used to populate dropdowns and define slider ranges. |

## Tech Stack

| Category | Tool / Library | Version (recommended) |
|----------|----------------|-----------------------|
| Language | Python 3.9+ | |
| UI Framework | Streamlit | |
| Data Handling | pandas | |
| Model Serialization | pickle (standard library) | |
| Model Type | scikit‑learn (inside `pipeline.pkl`) | |

> **Note:** The repository does not contain a `requirements.txt`. Install the libraries shown above before running the app.

## Flow of Operation
1. **Startup** – Streamlit starts `app.py`.  
   * The pickled model is loaded from `C:/Users/missj/Desktop/CPP/pipeline.pkl`.  
   * The CSV dataset `C:/Users/missj/Desktop/CPP/new car.csv` is read to obtain valid options and range limits for each widget.
2. **User Interaction** – The UI presents dropdowns and sliders for: brand, year, mileage, engine size, etc.
3. **Prediction Trigger** – When the *Predict* button is clicked, the selected values are assembled into a single‑row `pandas.DataFrame`.
4. **Inference** – The DataFrame is passed to the deserialized model’s `predict` method.  
5. **Result Display** – The predicted price is rendered below the button.

## Interaction
To launch the application locally:

```bash
# 1. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate

# 2. Install dependencies
pip install streamlit pandas

# 3. Run the Streamlit app
streamlit run app.py
```

After the server starts, open the URL shown in the terminal (typically `http://localhost:8501`) and fill in the fields to obtain a price prediction.

## Deployment
### Docker (recommended for reproducibility)
Create a `Dockerfile` in the repository root:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy only the necessary files
COPY app.py ./
COPY requirements.txt ./
COPY pipeline.pkl ./
COPY "new car.csv" ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]
```

Create a `requirements.txt`:

```
streamlit
pandas
```

Build and run the container:

```bash
docker build -t car-price-prediction .
docker run -p 8501:8501 car-price-prediction
```

The app will be reachable at `http://localhost:8501`.

### Local Production Setup
1. Ensure the absolute paths in `app.py` point to locations accessible inside your environment, or modify them to relative paths (e.g., `./pipeline.pkl`).
2. Verify that `pipeline.pkl` contains a scikit‑learn pipeline compatible with the feature columns defined in the UI.
3. Optionally, set up a reverse proxy (NGINX) to expose the Streamlit service behind HTTPS for public consumption.

---
*This README is generated automatically to reflect the current source code. Any structural changes to the repository should be reflected here to keep the documentation in sync.*
