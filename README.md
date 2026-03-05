# 🚦 Fuzzy Logic Traffic Light Controller

## 📖 Project Overview
This project implements a **Fuzzy Logic-based Traffic Light Controller** using Python and Streamlit. Unlike traditional fixed-timer signals, this system dynamically calculates **Green, Red, and Yellow light durations** based on real-time inputs:

* **Traffic Density** (Scale: 0–100)
* **Waiting Time** (Scale: 0–100)

Fuzzy logic is used to handle the uncertainty and variability in traffic conditions, making the signal timings adaptive, efficient, and smarter.



---

## ✨ Features
* **Dynamic Signal Calculation:** Computes precise durations based on live traffic data.
* **Interactive Professional Dashboard:** * Modern UI with gradient backgrounds.
    * Interactive sliders for real-time input adjustment.
    * Real-time output cards for signal timings.
* **Data Visualization:** * Visual Traffic Light simulation.
    * Aligned and compact graphs showing **Fuzzy Membership Functions**.
* **Portfolio-ready UI:** Clean, responsive, and easy to demonstrate.

---

## 🛠 Technology Stack
* **Python 3.13.5**
* **Streamlit** (Web Dashboard & UI)
* **scikit-fuzzy** (Fuzzy Logic Inference System)
* **Matplotlib** (Membership Function Plots)
* **NumPy** (Numerical Computation)

---

## 🚀 Installation & Setup (Using VS Code Terminal)

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tripjotsingh2505/fuzzy-logic-traffic-light-controller.git](https://github.com/tripjotsingh2505/fuzzy-logic-traffic-light-controller.git)
    cd fuzzy-logic-traffic-light-controller
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # To activate:
    # Windows: .\venv\Scripts\activate
    # Mac/Linux: source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install streamlit scikit-fuzzy matplotlib numpy
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

---

## 📊 Fuzzy Logic Implementation
The system utilizes the **Mamdani Inference Method** to process overlapping traffic conditions. 



* **Inputs:** Traffic Density (Low, Medium, High) & Waiting Time (Short, Medium, Long).
* **Output:** Light Duration (Short, Medium, Long).

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/tripjotsingh2505/fuzzy-logic-traffic-light-controller/issues).