import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_limit = int(input("Enter X-axis limit (e.g., 10): "))
y_limit = int(input("Enter Y-axis limit (e.g., 10): "))
circle_radius = float(input("Enter circle radius (e.g., 0.5): "))
num_frames = int(input("Enter number of frames (e.g., 20): "))

fig, ax = plt.subplots()

ax.set_xlim(0, x_limit)
ax.set_ylim(0, y_limit)

circle = plt.Circle((0, y_limit/2), circle_radius)
ax.add_patch(circle)

def update(frame):
    circle.center = (frame, y_limit/2)
    return circle,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=range(num_frames),
    interval=100
)

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Moving Circle Animation")

plt.show()