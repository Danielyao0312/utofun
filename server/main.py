from app import app

from views import *
from api import *
from admin import *


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

