#!/usr/bin/env python3
"""
Test script for 2025 Goals & Task Manager
"""

import os
import sys

# Add current directory to path to import task_manager
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task_manager import TaskManager

def test_task_manager():
    """Test the basic functionality of TaskManager."""
    print("🧪 Testing 2025 Goals & Task Manager...")
    
    # Create a test manager with temporary file
    test_file = "test_tasks.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    manager = TaskManager(test_file)
    
    # Test 1: Add tasks and goals
    print("✅ Test 1: Adding tasks and goals")
    task1 = manager.add_task("Learn Python", "Complete Python course", "task")
    goal1 = manager.add_task("Read 12 books in 2025", "One book per month", "goal")
    task2 = manager.add_task("Exercise daily", "30 minutes of exercise", "task")
    
    assert len(manager.tasks) == 3, "Should have 3 items"
    assert task1.category == "task", "First item should be a task"
    assert goal1.category == "goal", "Second item should be a goal"
    print("   ✓ Successfully added tasks and goals")
    
    # Test 2: Complete tasks
    print("✅ Test 2: Completing tasks")
    success = manager.complete_task(task1.id)
    assert success, "Should successfully complete task"
    assert task1.completed, "Task should be marked as completed"
    print("   ✓ Task completion works correctly")
    
    # Test 3: Get filtered tasks
    print("✅ Test 3: Filtering tasks")
    all_tasks = manager.get_tasks(category="task")
    all_goals = manager.get_tasks(category="goal")
    completed_items = manager.get_tasks(completed=True)
    
    assert len(all_tasks) == 2, "Should have 2 tasks"
    assert len(all_goals) == 1, "Should have 1 goal"
    assert len(completed_items) == 1, "Should have 1 completed item"
    print("   ✓ Filtering works correctly")
    
    # Test 4: Statistics
    print("✅ Test 4: Statistics calculation")
    stats = manager.get_stats()
    assert stats['total_tasks'] == 2, "Should show 2 total tasks"
    assert stats['completed_tasks'] == 1, "Should show 1 completed task"
    assert stats['total_goals'] == 1, "Should show 1 total goal"
    assert stats['task_completion_rate'] == 50.0, "Should show 50% completion rate"
    print("   ✓ Statistics calculation works correctly")
    
    # Test 5: Persistence (save and reload)
    print("✅ Test 5: Data persistence")
    manager.save_tasks()
    
    # Create new manager instance with same file
    manager2 = TaskManager(test_file)
    assert len(manager2.tasks) == 3, "Should load 3 items from file"
    assert manager2.next_id == 4, "Should maintain correct next_id"
    
    # Find the completed task
    completed_task = None
    for task in manager2.tasks:
        if task.completed:
            completed_task = task
            break
    
    assert completed_task is not None, "Should find completed task after reload"
    assert completed_task.title == "Learn Python", "Should maintain task details"
    print("   ✓ Data persistence works correctly")
    
    # Test 6: Delete task
    print("✅ Test 6: Deleting tasks")
    initial_count = len(manager2.tasks)
    success = manager2.delete_task(task2.id)
    assert success, "Should successfully delete task"
    assert len(manager2.tasks) == initial_count - 1, "Should have one less task"
    print("   ✓ Task deletion works correctly")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("\n🎉 All tests passed! Task Manager is working correctly.")
    return True

if __name__ == "__main__":
    try:
        test_task_manager()
        print("✅ Task Manager validation complete!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)