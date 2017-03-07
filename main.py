import connexion 
import config
from flask_cors import CORS

app = connexion.App(__name__, debug=config.DEBUG, host=config.HOST, port=config.PORT, specification_dir='swagger/')
CORS(app.app)
app.add_api('api.yaml')
if __name__ == "__main__": 
    app.run()
