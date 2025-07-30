#!/usr/bin/env python3
"""
2025 Goals & Task Manager - CLI Interface
A simple task and goal management system for the year 2025.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional


class Task:
    """Represents a single task or goal."""
    
    def __init__(self, id: int, title: str, description: str = "", category: str = "task", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.category = category  # "task" or "goal"
        self.completed = completed
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True
        self.completed_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = cls(data['id'], data['title'], data['description'], data['category'], data['completed'])
        task.created_at = data['created_at']
        task.completed_at = data.get('completed_at')
        return task


class TaskManager:
    """Main task manager class."""
    
    def __init__(self, data_file: str = "tasks_2025.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
                    self.next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, FileNotFoundError):
                self.tasks = []
                self.next_id = 1
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        data = {
            'tasks': [task.to_dict() for task in self.tasks],
            'next_id': self.next_id
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_task(self, title: str, description: str = "", category: str = "task") -> Task:
        """Add a new task or goal."""
        task = Task(self.next_id, title, description, category)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        for task in self.tasks:
            if task.id == task_id and not task.completed:
                task.mark_complete()
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False
    
    def get_tasks(self, category: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        """Get filtered list of tasks."""
        filtered_tasks = self.tasks
        
        if category:
            filtered_tasks = [t for t in filtered_tasks if t.category == category]
        
        if completed is not None:
            filtered_tasks = [t for t in filtered_tasks if t.completed == completed]
        
        return filtered_tasks
    
    def get_stats(self) -> Dict:
        """Get task statistics."""
        total_tasks = len([t for t in self.tasks if t.category == "task"])
        completed_tasks = len([t for t in self.tasks if t.category == "task" and t.completed])
        total_goals = len([t for t in self.tasks if t.category == "goal"])
        completed_goals = len([t for t in self.tasks if t.category == "goal" and t.completed])
        
        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'total_goals': total_goals,
            'completed_goals': completed_goals,
            'task_completion_rate': (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
            'goal_completion_rate': (completed_goals / total_goals * 100) if total_goals > 0 else 0
        }


def print_header():
    """Print application header."""
    print("=" * 50)
    print("   🎯 2025 Goals & Task Manager 🎯")
    print("=" * 50)


def print_menu():
    """Print main menu options."""
    print("\nOptions:")
    print("1. View all tasks")
    print("2. View goals for 2025")
    print("3. Add new task")
    print("4. Add new goal")
    print("5. Complete task/goal")
    print("6. Delete task/goal")
    print("7. View statistics")
    print("8. Exit")


def display_tasks(tasks: List[Task], title: str):
    """Display a list of tasks."""
    print(f"\n{title}")
    print("-" * len(title))
    
    if not tasks:
        print("No items found.")
        return
    
    for task in tasks:
        status = "✅" if task.completed else "⭕"
        category_icon = "🎯" if task.category == "goal" else "📋"
        print(f"{status} {category_icon} [{task.id}] {task.title}")
        if task.description:
            print(f"    📝 {task.description}")
        if task.completed and task.completed_at:
            completed_date = datetime.fromisoformat(task.completed_at).strftime("%Y-%m-%d %H:%M")
            print(f"    ✅ Completed: {completed_date}")
        print()


def main():
    """Main application loop."""
    manager = TaskManager()
    
    print_header()
    print("Welcome to your 2025 Goals & Task Manager!")
    print("Let's make 2025 your most productive year yet! 🚀")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                tasks = manager.get_tasks(category="task")
                display_tasks(tasks, "📋 Your Tasks")
                
            elif choice == "2":
                goals = manager.get_tasks(category="goal")
                display_tasks(goals, "🎯 Your 2025 Goals")
                
            elif choice == "3":
                print("\n📋 Adding a new task")
                title = input("Task title: ").strip()
                if title:
                    description = input("Description (optional): ").strip()
                    task = manager.add_task(title, description, "task")
                    print(f"✅ Task added: {task.title}")
                else:
                    print("❌ Task title cannot be empty!")
                    
            elif choice == "4":
                print("\n🎯 Adding a new 2025 goal")
                title = input("Goal title: ").strip()
                if title:
                    description = input("Description (optional): ").strip()
                    goal = manager.add_task(title, description, "goal")
                    print(f"✅ Goal added: {goal.title}")
                else:
                    print("❌ Goal title cannot be empty!")
                    
            elif choice == "5":
                task_id = input("\nEnter task/goal ID to complete: ").strip()
                try:
                    task_id = int(task_id)
                    if manager.complete_task(task_id):
                        print(f"🎉 Task/Goal {task_id} marked as completed!")
                    else:
                        print(f"❌ Task/Goal {task_id} not found or already completed!")
                except ValueError:
                    print("❌ Please enter a valid ID number!")
                    
            elif choice == "6":
                task_id = input("\nEnter task/goal ID to delete: ").strip()
                try:
                    task_id = int(task_id)
                    if manager.delete_task(task_id):
                        print(f"🗑️ Task/Goal {task_id} deleted!")
                    else:
                        print(f"❌ Task/Goal {task_id} not found!")
                except ValueError:
                    print("❌ Please enter a valid ID number!")
                    
            elif choice == "7":
                stats = manager.get_stats()
                print("\n📊 Your 2025 Progress Statistics")
                print("=" * 35)
                print(f"📋 Tasks: {stats['completed_tasks']}/{stats['total_tasks']} completed ({stats['task_completion_rate']:.1f}%)")
                print(f"🎯 Goals: {stats['completed_goals']}/{stats['total_goals']} completed ({stats['goal_completion_rate']:.1f}%)")
                
                if stats['total_tasks'] > 0 or stats['total_goals'] > 0:
                    overall_completion = ((stats['completed_tasks'] + stats['completed_goals']) / 
                                        (stats['total_tasks'] + stats['total_goals']) * 100)
                    print(f"🚀 Overall Progress: {overall_completion:.1f}%")
                    
            elif choice == "8":
                print("\n👋 Thank you for using 2025 Goals & Task Manager!")
                print("Keep working towards your goals! 🌟")
                break
                
            else:
                print("❌ Invalid choice! Please enter a number from 1-8.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Keep pursuing your 2025 goals! 🌟")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()