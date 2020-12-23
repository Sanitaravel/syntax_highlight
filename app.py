import flask

app = flask.Flask(__name__)

colors = ["#7f8fa6", '#353b48', '#40739e', '#487eb0', '#4cd137', '#44bd32', '#44bd32', '#273c75', '#192a56', '#718093', '#e1b12c', '#fbc531', '#9c88ff', '#8c7ae6', '#00a8ff', '#0097e6', '#e84118', '#c23616']

edited_arr = []

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if flask.request.method == "POST":
        set_str(flask.request.form['input'])
        return flask.redirect('/output')
    else:
        edited_arr.clear()
        return flask.render_template('input.html')


@app.route('/output')
def output():
    return flask.render_template('output.html', spans=edited_arr)


def set_str(str):
    str = str.replace('\r', '\t')
    color_idx = 0
    buffer = ''
    style = f'color: {colors[color_idx]};'
    true = True
    for sym in str:
        if color_idx < 0 or not true:
            style = f'color: {colors[color_idx]}; font-weight: bold;'
            true = False
        else:
            style = f'color: {colors[color_idx]};'
        if sym == '{':
            edited_arr.append({'style': style, 'text': buffer})
            color_idx += 1
            buffer = ''
            edited_arr.append({'style': 'color: black;', 'text': sym})
        elif sym == '}':
            edited_arr.append({'style': style, 'text': buffer})
            color_idx -= 1
            buffer = ''
            edited_arr.append({'style': 'color: black', 'text': sym})
        else:
            buffer += sym
    edited_arr.append({'style': 'color: black', 'text': buffer})
    print(edited_arr)


if __name__ == '__main__':
    app.run()
