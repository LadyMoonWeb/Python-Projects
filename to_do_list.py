import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Название задачи: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Задача добавлена.")

def mark_done(tasks):
    list_tasks(tasks)
    idx = int(input("Номер задачи для отметки: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Задача отмечена как выполненная.")
    else:
        print("Неверный номер.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Список задач\n2. Добавить\n3. Отметить выполненной\n4. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
