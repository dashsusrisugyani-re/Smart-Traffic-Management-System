import random
import time
import matplotlib.pyplot as plt

class TrafficSignal:
    def __init__(self, name):
        self.name = name
        self.green_time = 30  # default green time in seconds
        self.vehicle_count = 0

    def update_vehicle_count(self, count):
        self.vehicle_count = count

    def adjust_green_time(self):
        # Increase green time if vehicle count is high, decrease if low
        if self.vehicle_count > 20:
            self.green_time = min(90, self.green_time + 10)
        elif self.vehicle_count < 5:
            self.green_time = max(20, self.green_time - 5)
        else:
            self.green_time = 30

    def __str__(self):
        return f"{self.name}: {self.vehicle_count} vehicles, Green Time={self.green_time}s"

class SmartTrafficSystem:
    def __init__(self, signals):
        self.signals = signals  # List of TrafficSignal objects
        self.history = {signal.name: [] for signal in signals}

    def simulate_vehicle_counts(self):
        # Simulate vehicle counts from each direction
        for signal in self.signals:
            count = random.randint(0, 40)
            signal.update_vehicle_count(count)
            self.history[signal.name].append((self.current_time, count))

    def adjust_signals(self):
        for signal in self.signals:
            signal.adjust_green_time()

    def run_simulation(self, cycles=10):
        self.current_time = 0
        for _ in range(cycles):
            print(f"\n--- Cycle {self.current_time + 1} ---")
            self.simulate_vehicle_counts()
            self.adjust_signals()
            for signal in self.signals:
                print(signal)
            self.current_time += 1
            time.sleep(0.5)  # Simulate real-time (can be removed for faster runs)

    def plot_traffic(self):
        plt.figure(figsize=(8,6))
        for signal in self.signals:
            times = [t for t, _ in self.history[signal.name]]
            counts = [c for _, c in self.history[signal.name]]
            plt.plot(times, counts, label=signal.name)
        plt.xlabel('Cycle')
        plt.ylabel('Vehicle Count')
        plt.title('Traffic Flow History')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    signals = [
        TrafficSignal("North"),
        TrafficSignal("South"),
        TrafficSignal("East"),
        TrafficSignal("West")
    ]
    system = SmartTrafficSystem(signals)
    system.run_simulation(cycles=15)
    system.plot_traffic()