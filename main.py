from flask import Flask, render_template, request, redirect

class HashTable:
    def __init__(self):
        self.entries = {}

    def __repr__(self):
        return repr(self.entries)

    def empty(self):
        return len(self.entries) == 0

    def __len__(self):
        return len(self.entries)

    def __contains__(self, key):
        return key in self.entries

    def insert(self, date, entry):
        self.entries[date] = entry

    def remove(self, date):
        if date in self.entries:
            del self.entries[date]

    def find(self, date):
        return self.entries.get(date)


app = Flask(__name__)
journal = HashTable()


@app.route('/')
def index():
    dates = journal.entries
    return render_template('index.html', dates=dates)


@app.route('/add_entry', methods=['POST'])
def add_entry():
    date = request.form['date']
    entry = request.form['entry']
    journal.insert(date, entry)
    return redirect('/')


@app.route('/delete_entry/<date>', methods=['POST'])
def delete_entry(date):
    journal.remove(date)
    return redirect('/')


@app.route('/view_entry/<date>')
def view_entry(date):
    entry = journal.find(date)
    return render_template('view_entry.html', date=date, entry=entry)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
