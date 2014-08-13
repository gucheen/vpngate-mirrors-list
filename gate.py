import urllib2
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask.ext import restful


app = Flask(__name__)
api = restful.Api(app)


@app.route('/')
def show_crab():
    url = 'http://www.vpngate.net/cn/sites.aspx'
    raw = urllib2.urlopen(url)
    soup = BeautifulSoup(raw.read())
    site_list = soup.find_all('ul', 'listBigArrow')[1]
    return render_template('index.html', content=site_list)


class GetList(restful.Resource):
    def get(self):
        url = 'http://www.vpngate.net/cn/sites.aspx'
        raw = urllib2.urlopen(url)
        soup = BeautifulSoup(raw.read())
        site_list = soup.find_all(target='_blank')
        sites = []
        for i in range(len(site_list)-1):
            sites.append(site_list[i].get_text())
        return sites


api.add_resource(GetList, '/api')


if __name__ == '__main__':
    app.run(debug=True)