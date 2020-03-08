from flask import Blueprint, render_template, request, url_for, redirect, session
from models.alert import Alert
from models.item import Item
from models.store import Store
from models.user import requires_login

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
@requires_login
def index():
    # TODO remove the following line
    print(f"{session['email']}")
    alerts = Alert.find_many_by('user_email', session['email'])
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
@requires_login
def new_alert():
    if request.method == 'POST':
        alert_name = request.form['name']
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])
        print(f"item url is {item_url}")
        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        item.save_to_mongo()

        Alert(alert_name, item._id, price_limit, session['email']).save_to_mongo()

    return render_template('alerts/new_alert.html')


@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
@requires_login
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if request.method == 'POST':
        alert.price_limit = float(request.form['price_limit'])
        alert.save_to_mongo()
        return redirect(url_for('.index'))

    # why do we load alert ti edut_alert.heml?
    return render_template('alerts/edit_alert.html', alert=alert)


@alert_blueprint.route('/delete/<string:alert_id>')
def delete_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session['email']:
        alert.remove_from_mongo()
    return redirect(url_for('.index'))
