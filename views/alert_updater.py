from models.alert import Alert
from dotenv import load_dotenv

load_dotenv()

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.item.save_to_mongo()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts created.")