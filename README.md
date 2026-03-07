# 🚦 Fuzzy Logic Traffic Light Controller

## 📖 Project Overview
This project implements a **Fuzzy Logic-based Traffic Light Controller** using Python and Streamlit. Unlike traditional fixed-timer signals, this system dynamically calculates **Green, Red, and Yellow durations** based on real-time traffic inputs, reducing congestion and wait times.

It handles traffic uncertainty using:

- **Traffic Density** (0–100%): Vehicles present on the road.  
- **Waiting Time** (0–100s): Duration vehicles have been waiting at the signal.  

---

## ✨ Key Features
- **Dynamic Signal Calculation:** Real-time adaptation of traffic light timings.  
- **Interactive Dashboard:** Modern UI with gradient styling and live sliders.  
- **Instant Output Cards:** Shows calculated durations for each light.  
- **Fuzzy Membership Visualization:** Professional graphs for "Low", "Medium", "High" traffic levels.  
- **Visual Feedback:** Real-time traffic light simulation on the dashboard.  

---

## 🛠 Technology Stack
- **Python 3.13.5**  
- **Streamlit** – Web interface  
- **scikit-fuzzy** – Fuzzy logic engine  
- **Matplotlib** – Graph plotting  
- **NumPy** – Numerical computations  

---

## 🚀 Installation & Setup (VS Code Terminal)

1. **Clone the repository:**
```bash
git clone https://github.com/tripjotsingh2505/fuzzy-logic-traffic-light-controller.git
cd fuzzy-logic-traffic-light-controller