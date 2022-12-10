from flask import Flask, request

app=Flask(__name__)
#!!!!!!!!!!Книги!!!!!!!!!!!!
books=[]

class Book(object):
    def __init__(self, title, author, quanpage, mass, code):
        self.title = title
        self.author = author
        self.quanpage = quanpage
        self.mass = mass
        self.code = code

@app.route('/', methods=['GET'])
def menu():
    return "Главная страница. http://127.0.0.1:3005/api/books, http://127.0.0.1:3005/api/cars"

@app.route('/api/books/', methods=['GET'])
def GetBook():
    List = ''
    for i in books:
        book = f"Название: {i.title}, автор: {i.author}, количество страниц: {i.quanpage}, масса: {i.mass}, код: {i.code}"
        List = List + book
    return List, 200

@app.route('/api/books/', methods=['POST'])
def CreateBook():
    reqvest = request.get_json()
    title = None
    author = None
    quanpage = None
    mass = None
    code = None
    if reqvest:
        if 'title' in reqvest:
            title = reqvest['title']
        else:
            return 'Нет названия книги', 402
        if 'author' in reqvest:
            author = reqvest['author']
        else:
            return 'Нет автора', 402
        if 'quanpage' in reqvest:
            quanpage = reqvest['quanpage']
        else:
            return 'Нет количества страниц', 402
        if 'mass' in reqvest:
            mass = reqvest['mass']
        else:
            return 'Нет массы', 402
        if 'code' in reqvest:
            code = reqvest['code']
        else:
            return 'Нет кода книги', 402
    else:
        return 'Нет запроса', 402
    if title and author and quanpage and mass and code:
        book = Book(title, author, quanpage, mass, code)
    books.append(book)
    return "Создание книги завершено", 201

@app.route('/api/books/<int:Id>', methods=['PUT'])
def EditBook(Id):
    reqvest = request.get_json()
    if reqvest:
        if 'title' in reqvest:
            books[Id].title = reqvest['title']
        if 'author' in reqvest:
            books[Id].author = reqvest['author']
        if 'quanpage' in reqvest:
            books[Id].quanpage = reqvest['quanpage']
        if 'mass' in reqvest:
            books[Id].mass = reqvest['mass']
        if 'code' in reqvest:
            books[Id].code = reqvest['code']
    else:
        return "Нет запроса", 402
    return "Редактирование книги завершено", 200

@app.route('/api/books/<int:Id>', methods=['DELETE'])
def DeleteBook(Id):
    books.pop(Id)
    return "Удаление книги завершено"

#!!!!!!!!Машины!!!!!!!!!!!!
cars=[]

class Car(object):
    def __init__(self, title, model, cost, credit, gift):
        self.title = title
        self.model = model
        self.cost = cost
        self.credit = credit
        self.gift = gift

@app.route('/api/cars/', methods=['GET'])
def GetCar():
    List = ''
    for i in cars:
        car = f"Название: {i.title}, модель: {i.model}, цена: {i.cost}, возможность кредита: {i.credit}, подарок: {i.gift}"
        List = List + car
    return List, 200

@app.route('/api/cars/', methods=['POST'])
def CreateCar():
    reqvest = request.get_json()
    title = None
    model = None
    cost = None
    credit = None
    gift = None
    if reqvest:
        if 'title' in reqvest:
            title = reqvest['title']
        else:
            return 'Нет названия машины', 402
        if 'model' in reqvest:
            model = reqvest['model']
        else:
            return 'Нет модели машины', 402
        if 'cost' in reqvest:
            cost = reqvest['cost']
        else:
            return 'Нет стоимости', 402
        if 'credit' in reqvest:
            credit = reqvest['credit']
        else:
            return 'Нет "возможности кредита"', 402
        if 'gift' in reqvest:
            gift = reqvest['gift']
        else:
            return 'Нет "подарка"', 402
    else:
        return 'Нет запроса', 402
    if title and model and cost and credit and gift:
        car = Car(title, model, cost, credit, gift)
    cars.append(car)
    return "Создание машины завершено", 201

@app.route('/api/cars/<int:Id>', methods=['PUT'])
def EditCar(Id):
    reqvest = request.get_json()
    if reqvest:
        if 'title' in reqvest:
            cars[Id].title = reqvest['title']
        if 'model' in reqvest:
            cars[Id].model = reqvest['model']
        if 'cost' in reqvest:
            cars[Id].cost = reqvest['cost']
        if 'credit' in reqvest:
            cars[Id].credit = reqvest['credit']
        if 'gift' in reqvest:
            cars[Id].gift = reqvest['gift']
    else:
        return "Нет запроса", 402
    return "Редактирование машины завершено", 200

@app.route('/api/cars/<int:Id>', methods=['DELETE'])
def DeleteCar(Id):
    cars.pop(Id)
    return "Удаление машины завершено"

if __name__ == "__main__":
    app.run(host="localhost", port="3005", debug=True)