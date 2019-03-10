import flask
import loadDataScript
import clearDataScript
import queryDataScript

# Flask object
application = flask.Flask(__name__)

# render index.html (home page)
@application.route('/')
def homePage():
   return flask.render_template('index.html')

# render load.html (load confirmation page)
@application.route('/load', methods=['POST', 'GET'])
def loadPage():
   if flask.request.method == 'POST':
      loadDataScript.copyData()
      loadDataScript.parseData()
      return flask.render_template('load.html')

# render clear.html (clear confirmation page)
@application.route('/clear', methods=['POST', 'GET'])
def clearPage():
   if flask.request.method == 'POST':
      clearDataScript.clearBucket()
      clearDataScript.clearTable()
      return flask.render_template('clear.html')

# render query.html (query page)
@application.route('/query', methods=['POST', 'GET'])
def queryPage():
   if flask.request.method == 'POST':
      LastName = flask.request.form['LastName'].strip()
      FirstName = flask.request.form['FirstName'].strip()
      #print('Last Name: ' + LastName) # for debugging
      #print('First Name: ' + FirstName) # for debugging
      result = ''
      if (not LastName and not FirstName):
         result = ['Fill in either or both First Name and Last Name!']
      else:
         result = queryDataScript.queryData(LastName, FirstName)
         result = queryDataScript.orderKeys(result)
      #print(result) # for debugging
      if (not result):
         result = ['No entry found!']
      return flask.render_template('query.html', result=result)

if __name__ == '__main__':
    application.run()
