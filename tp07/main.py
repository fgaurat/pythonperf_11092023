from TodoDAO import TodoDAO
from TodoDAOContext import TodoDAOContext


def completed_todos(gen_todos):
    for todo in gen_todos:
        if todo.completed:
            yield todo


def main():
    with TodoDAOContext(r"todos_db.db") as dao:
        todos = list(dao.findAll())
        raise Exception("hoooooo")
        print(len(todos))    

def main01():
    dao = TodoDAO(r"tp07\todos_db.db")
    todos = dao.findAll()
    # t = next(todos):
    # t = next(todos)
    # print(t)
    # for todo in todos:
    #     print(todo)
    # dao.findAll() | completed_todos
    
    for comp_todo in completed_todos(todos):
        print(comp_todo)

if __name__=='__main__':
    main()
