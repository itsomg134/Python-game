# Python-game

A classic Snake game implementation in Python using Pygame. Navigate the snake, eat food, grow longer, and try to beat your high score!

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎮 Features

- **Classic Gameplay**: Smooth, grid-based movement with arrow key controls
- **Score Tracking**: Earn points by eating food
- **Collision Detection**: Game ends when hitting walls or yourself
- **Visual Feedback**: Clean, colorful graphics with a grid overlay
- **Game Over Screen**: Restart easily or quit
- **Responsive Controls**: Prevents instant reversing to avoid accidental deaths

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pygame library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```

2. Install the required dependencies:
```bash
pip install pygame
```

### Running the Game

```bash
python snake_game.py
```

## 🎯 How to Play

- **Arrow Keys**: Control the snake's direction
  - ⬆️ Up Arrow: Move up
  - ⬇️ Down Arrow: Move down
  - ⬅️ Left Arrow: Move left
  - ➡️ Right Arrow: Move right
- **Objective**: Eat the red food to grow longer and increase your score
- **Game Over**: When you hit a wall or your own body
- **Restart**: Press `SPACE` on the game over screen
- **Quit**: Press `ESC` or close the window

## 🎨 Game Elements

- **Green Snake**: Your character (head is brighter green)
- **Red Food**: Eating this grows your snake and adds 10 points
- **Black Background**: The game arena with grid lines
- **Score Display**: Shows in the top-left corner

## ⚙️ Customization

You can easily customize the game by modifying these constants in `snake_game.py`:

```python
WIDTH, HEIGHT = 600, 600  # Window size
GRID_SIZE = 20            # Size of each grid cell
FPS = 10                  # Game speed (higher = faster)
```

You can also change colors by modifying the color constants:

```python
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
```

## 🛠️ Technical Details

- **Language**: Python 3
- **Library**: Pygame
- **Architecture**: Object-oriented design with Snake and Food classes
- **Grid System**: 30x30 grid (configurable)
- **Frame Rate**: 10 FPS (adjustable)

## 📝 Future Enhancements

Potential features for future versions:

- [ ] High score persistence
- [ ] Difficulty levels (speed variations)
- [ ] Power-ups and obstacles
- [ ] Sound effects and background music
- [ ] Pause functionality
- [ ] Multiple game modes

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with Python and Pygame
- Thanks to the Pygame community for excellent documentation

## 📧 Contact

Om Gedam

GitHub: @itsomg134

Email: omgedam123098@gmail.com

Twitter (X): @omgedam

LinkedIn: Om Gedam

Portfolio: https://ogworks.lovable.app
