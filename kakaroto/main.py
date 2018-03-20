from sanic import Sanic

from config import APP_NAME
from controllers import cards, issues, projects, columns

app = Sanic(APP_NAME)

app.add_route(cards.Webhook.as_view(), '/projects/<project_id:string>/cards/hooks', methods=['POST'], version=1)
app.add_route(issues.Webhook.as_view(), '/projects/<project_id:string>/issues/hooks', methods=['POST'], version=1)
app.add_route(projects.Collection.as_view(), '/projects', methods=['POST'], version=1)
app.add_route(columns.Collection.as_view(), '/projects/<project_id:string>/columns', methods=['POST'], version=1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3443)
