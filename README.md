# Smart-Traffic-Management-System
This Python-based simulation project models an intelligent traffic management system that dynamically regulates traffic signal timings based on real-time vehicle counts. Designed for urban intersections, it aims to optimize traffic flow and minimize congestion by adjusting green light durations according to the volume of vehicles in each direction.
## Features
- **Simulates four traffic signals** (North, South, East, West) at an intersection.
- **Vehicle counts are randomly generated** each cycle to mimic camera or sensor input.
- **Green light durations are dynamically adjusted** according to vehicle congestion.
- **Command-line output** shows live signal states and adjustments.
- **Traffic flow history is visualized** using `matplotlib` graphs
---
## Project Structure
```
smart-traffic-management-system/
├── smart_traffic_management.py
└── README.md
```---
## How It Works

1. **TrafficSignal Class:** Represents each signal, tracks vehicle count, and manages green light timing.
2. **SmartTrafficSystem Class:** Manages all signals, simulates vehicle counts, adjusts timings, logs and visualizes data.
3. **Simulation:** Runs for several cycles, printing the signal states each time.
4. **Visualization:** After simulation, a traffic flow graph is displayed for analysis.
---
### Prerequisites
- Python 3.x
- `matplotlib` library

Install `matplotlib` with:
```bash
pip install matplotlib
```

## Author

- [SUSRI SUGYANI DASH](https://github.com/dashsusrisugyani-re)
   ```

---
