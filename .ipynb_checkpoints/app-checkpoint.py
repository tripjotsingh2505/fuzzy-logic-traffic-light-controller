import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fuzzy Traffic Light Controller", layout="wide")

# ---------- UI STYLE ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#d0e1f9,#f7f9fc);
}

/* Main Title */
.main-title{
font-size:50px;
font-weight:700;
text-align:center;
margin-bottom:30px;
color:#1a1a1a;
}

/* Cards */
.card{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
text-align:center;
border:1px solid #e6e6e6;
}

.card h3{
color:#444;
font-size:28px;
margin-bottom:10px;
}

.card h2{
color:#111;
font-size:40px;
margin-top:5px;
}

/* Traffic Light */
.light-box{
background:#222;
padding:20px;
border-radius:20px;
width:130px;
margin:auto;
}

.light{
width:65px;
height:65px;
border-radius:50%;
margin:12px auto;
}

.red{background:red;}
.yellow{background:yellow;}
.green{background:green;}

/* Section Titles */
.section-title{
font-size:32px;
font-weight:700;
margin-top:30px;
margin-bottom:15px;
color:black;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚦 Fuzzy Logic Traffic Light Controller</div>', unsafe_allow_html=True)

# ---------- SIDEBAR INPUT ----------
st.sidebar.header("Traffic Inputs")
traffic_density_value = st.sidebar.slider("Traffic Density",0,100,60)
waiting_time_value = st.sidebar.slider("Waiting Time",0,100,40)

# ---------- FUZZY SYSTEM ----------
traffic_density = ctrl.Antecedent(np.arange(0,101,1),'traffic_density')
waiting_time = ctrl.Antecedent(np.arange(0,101,1),'waiting_time')
green_light_duration = ctrl.Consequent(np.arange(0,61,1),'green_light_duration')
red_light_duration = ctrl.Consequent(np.arange(0,61,1),'red_light_duration')
yellow_light_duration = ctrl.Consequent(np.arange(3,6,1),'yellow_light_duration')

traffic_density['low']=fuzz.trimf(traffic_density.universe,[0,0,50])
traffic_density['medium']=fuzz.trimf(traffic_density.universe,[30,50,80])
traffic_density['high']=fuzz.trimf(traffic_density.universe,[60,100,100])

waiting_time['short']=fuzz.trimf(waiting_time.universe,[0,0,40])
waiting_time['medium']=fuzz.trimf(waiting_time.universe,[20,50,80])
waiting_time['long']=fuzz.trimf(waiting_time.universe,[60,100,100])

green_light_duration['short']=fuzz.trimf(green_light_duration.universe,[0,0,20])
green_light_duration['medium']=fuzz.trimf(green_light_duration.universe,[10,30,50])
green_light_duration['long']=fuzz.trimf(green_light_duration.universe,[40,60,60])

red_light_duration['short']=fuzz.trimf(red_light_duration.universe,[0,0,20])
red_light_duration['medium']=fuzz.trimf(red_light_duration.universe,[10,30,50])
red_light_duration['long']=fuzz.trimf(red_light_duration.universe,[40,60,60])

yellow_light_duration['fixed']=fuzz.trimf(yellow_light_duration.universe,[3,4,5])

# Rules
rule1=ctrl.Rule(traffic_density['low'] & waiting_time['short'],green_light_duration['short'])
rule2=ctrl.Rule(traffic_density['low'] & waiting_time['medium'],green_light_duration['medium'])
rule3=ctrl.Rule(traffic_density['low'] & waiting_time['long'],green_light_duration['medium'])

rule4=ctrl.Rule(traffic_density['medium'] & waiting_time['short'],green_light_duration['medium'])
rule5=ctrl.Rule(traffic_density['medium'] & waiting_time['medium'],green_light_duration['medium'])
rule6=ctrl.Rule(traffic_density['medium'] & waiting_time['long'],green_light_duration['long'])

rule7=ctrl.Rule(traffic_density['high'] & waiting_time['short'],green_light_duration['medium'])
rule8=ctrl.Rule(traffic_density['high'] & waiting_time['medium'],green_light_duration['long'])
rule9=ctrl.Rule(traffic_density['high'] & waiting_time['long'],green_light_duration['long'])

rule10=ctrl.Rule(traffic_density['low'],red_light_duration['long'])
rule11=ctrl.Rule(traffic_density['medium'],red_light_duration['medium'])
rule12=ctrl.Rule(traffic_density['high'],red_light_duration['short'])

rule13=ctrl.Rule(traffic_density['low'] | traffic_density['medium'] | traffic_density['high'],yellow_light_duration['fixed'])

system = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13])
sim = ctrl.ControlSystemSimulation(system)

sim.input['traffic_density']=traffic_density_value
sim.input['waiting_time']=waiting_time_value
sim.compute()

green = sim.output['green_light_duration']
red = sim.output['red_light_duration']
yellow = sim.output['yellow_light_duration']

# ---------- OUTPUT CARDS ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="card"><h3>🟢 Green Signal</h3><h2>{green:.2f} sec</h2></div>',unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="card"><h3>🔴 Red Signal</h3><h2>{red:.2f} sec</h2></div>',unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="card"><h3>🟡 Yellow Signal</h3><h2>{yellow:.2f} sec</h2></div>',unsafe_allow_html=True)

# ---------- TRAFFIC LIGHT ----------
st.markdown('<div class="section-title">Traffic Signal</div>', unsafe_allow_html=True)

st.markdown("""
<div class="light-box">
<div class="light red"></div>
<div class="light yellow"></div>
<div class="light green"></div>
</div>
""",unsafe_allow_html=True)

# ---------- GRAPH FUNCTION ----------
def plot_membership(var,title,figsize=(4,2.5)):
    fig, ax = plt.subplots(figsize=figsize)
    for label in var.terms:
        ax.plot(var.universe,var[label].mf,label=label)
    ax.set_title(title,fontsize=14)
    ax.tick_params(labelsize=12)
    ax.legend(fontsize=12)
    ax.grid(True)
    st.pyplot(fig)

# ---------- GRAPHS ----------
st.markdown('<div class="section-title">Fuzzy Membership Functions</div>', unsafe_allow_html=True)

# Columns layout for aligned graphs
col1,col2,col3 = st.columns(3)
with col1:
    plot_membership(traffic_density,"Traffic Density")
with col2:
    plot_membership(waiting_time,"Waiting Time")
with col3:
    plot_membership(green_light_duration,"Green Duration")

# Row 2: Red and Yellow aligned
col1,col2 = st.columns(2)
with col1:
    plot_membership(red_light_duration,"Red Duration")
with col2:
    plot_membership(yellow_light_duration,"Yellow Duration",figsize=(3.5,2.5))  # Smaller yellow graph