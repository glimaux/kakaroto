from sanic import Sanic
from controllers import cards, issues

app = Sanic()

app.add_route(cards.Webhook.as_view(), '/cards/hooks', methods=['POST'], version=1)
app.add_route(issues.Webhook.as_view(), '/issues/hooks', methods=['POST'], version=1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3443)
