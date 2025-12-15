import matplotlib.pyplot as plt

# Define sectors and estimated percentage impact on operations due to the 2008 MNS agitation
sectors = [
    "Construction", 
    "Manufacturing (SSI)", 
    "Transport & Taxi", 
    "Hospitality", 
    "Railways & Govt Exams"
]

impact_percentage = [
    50,  # Construction sector experienced up to 50% slowdown
    30,  # Manufacturing slowed by an estimated 30%
    35,  # Public transport dropped 30-40% in active services
    25,  # Restaurants and hospitality were impacted by 20-25%
    80   # Government exams and rail operations severely disrupted (~80%)
]

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(sectors, impact_percentage, color='steelblue')
plt.title("Estimated Sector-wise Impact Due to 2008 MNS Agitation in Maharashtra", fontsize=14)
plt.xlabel("Industry Sector")
plt.ylabel("Estimated Operational Disruption (%)")
plt.ylim(0, 100)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=20)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
