import matplotlib.pyplot as plt

color_map = {
    'W': 'white',
    'Y': 'yellow',
    'R': 'red',
    'O': 'orange',
    'B': 'blue',
    'G': 'green'
}

def draw_cube(state):
    fig, ax = plt.subplots(3, 4, figsize=(8, 6))
    
    for i in range(3):
        for j in range(3):
            ax[0, 1].add_patch(plt.Rectangle((j, 2-i), 1, 1, facecolor=color_map[state.top()[i][j]], edgecolor='black', linewidth=2))
            ax[1, 0].add_patch(plt.Rectangle((j, 2-i), 1, 1, facecolor=color_map[state.left()[i][j]], edgecolor='black', linewidth=2))
            ax[1, 1].add_patch(plt.Rectangle((j, 2-i), 1, 1, facecolor=color_map[state.front()[i][j]], edgecolor='black', linewidth=2))
            ax[1, 2].add_patch(plt.Rectangle((j, 2-i), 1, 1, facecolor=color_map[state.right()[i][j]], edgecolor='black', linewidth=2))
            ax[1, 3].add_patch(plt.Rectangle((j, 2-i), 1, 1, facecolor=color_map[state.back()[i][j]], edgecolor='black', linewidth=2))
            ax[2, 1].add_patch(plt.Rectangle((j, 2-i), 1, 1, facecolor=color_map[state.bottom()[i][j]], edgecolor='black', linewidth=2))
    
    for i in range(3):
        for j in range(4):
            ax[i, j].set_xlim(0, 3)
            ax[i, j].set_ylim(0, 3)
            ax[i, j].set_xticks([])
            ax[i, j].set_yticks([])
            ax[i, j].set_aspect('equal')
            if (i, j) not in [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)]:
                ax[i, j].axis('off')
    
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()