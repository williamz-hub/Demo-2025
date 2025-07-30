# Demo-2025

Welcome to Demo-2025! 🎯 A collection of practical demo applications and utilities to make 2025 your most productive year yet.

## 🎯 2025 Goals & Task Manager

A comprehensive task and goal management system designed specifically for the year 2025. Track your progress, manage your tasks, and achieve your goals with both command-line and beautiful web interfaces.

### Features

**📋 Task Management:**
- Add, complete, and delete tasks
- Track daily activities and to-dos
- Monitor completion progress

**🎯 Goal Setting:**
- Set and track long-term goals for 2025
- Categorize goals separately from daily tasks
- Visual progress tracking

**📊 Progress Analytics:**
- Real-time statistics dashboard
- Completion rates for tasks and goals
- Visual progress indicators

**💾 Data Persistence:**
- Local storage in web interface
- JSON file storage for CLI
- Cross-platform compatibility

### Usage

#### Web Interface (Recommended)

1. **Start the web server:**
   ```bash
   python3 -m http.server 8000
   ```

2. **Open in browser:**
   Navigate to `http://localhost:8000/task_manager.html`

3. **Start managing your 2025 goals:**
   - Add tasks and goals using the form
   - Switch between different views using tabs
   - Complete items by clicking the ✅ Complete button
   - Track your progress with the statistics dashboard

#### Command Line Interface

1. **Run the CLI application:**
   ```bash
   python3 task_manager.py
   ```

2. **Use the interactive menu:**
   - View all tasks and goals
   - Add new items with descriptions
   - Mark items as completed
   - Delete items when no longer needed
   - View detailed statistics

### Screenshots

![2025 Goals & Task Manager](https://github.com/user-attachments/assets/d8e54038-8bca-4118-abcd-17a1f36bd467)

*Beautiful, responsive web interface with gradient design and real-time statistics*

### Technical Details

**Web Interface:**
- Pure HTML, CSS, and JavaScript (no dependencies)
- Responsive design works on desktop and mobile
- Local storage persistence
- Modern gradient UI with smooth animations

**CLI Interface:**
- Python 3.6+ compatible
- JSON file storage (`tasks_2025.json`)
- Interactive menu system
- Full CRUD operations

**Data Structure:**
- Tasks and goals stored with metadata
- Timestamps for creation and completion
- Categories and descriptions
- Unique ID system

### Getting Started

1. Clone the repository
2. Choose your preferred interface (web or CLI)
3. Start adding your 2025 goals and daily tasks
4. Track your progress and stay motivated!

### Development

**Testing:**
```bash
python3 test_task_manager.py
```

**File Structure:**
- `task_manager.py` - CLI interface and core logic
- `task_manager.html` - Web interface (self-contained)
- `test_task_manager.py` - Automated tests
- `tasks_2025.json` - Data storage (created automatically)

---

*Make 2025 your most productive year yet! 🚀*