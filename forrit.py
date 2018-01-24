import os
from bottle import route, run, static_file, error, request

@route('/')
def index():
    return '<a href="/lidura">Liður A</a> <a href="/lidurb">Liður B</a>'

@route('/lidura')
def lidurA():
    return '<h2>Veldu tölu</h2><a href="/lidura/1">1</a> ' \
           '<a href="/lidura/2">2</a> <a href="/lidura/3">3</a> ' \
           '<a href="/lidura/4">4</a> <a href="/lidura/5">5</a> ' \
           '<h3><a href="/..">Til baka</a></h3>'

@route('/lidura/<n>')
def tala(n):
    return 'Þú valdir ' + n + '!' \
            '<h3><a href="/">Til baka</a></h3>'

@route('/lidurb')
def lidurB():
    return '<h2>Hvaða Counter-Strike: Global Offensive?</h2>' \
           '<a href="/lidurb/result?mynd=g2"><img src="/static/g2_logo.svg" width="200"></a> <a href="/lidurb/result?mynd=faze"><img src="/static/faze_logo.svg" width="200"></a> ' \
           '<a href="/lidurb/result?mynd=c9"><img src="/static/c9_logo.svg" width="200"></a> <a href="/lidurb/result?mynd=mouse"><img src="/static/ms_logo.svg" width="200"></a> ' \
           '<a href="/lidurb/result?mynd=nip"><img src="/static/nip_logo.svg" width="200"><br></a> <a href="/lidurb/result?mynd=vp"><img src="/static/vp_logo.svg" width="200"></a> ' \
           '<a href="/lidurb/result?mynd=astralis"><img src="/static/astralis_logo.svg" width="200"></a> <a href="/lidurb/result?mynd=vega"><img src="/static/vega_logo.svg" width="200"></a> ' \
           '<a href="/lidurb/result?mynd=sk"><img src="/static/sk_logo.svg" width="200"></a> <a href="/lidurb/result?mynd=fnatic"><img src="/static/fnatic_logo.svg" width="200"></a> '

@route('/lidurb/result')
def result():
    mynd = request.query.mynd
    return '<h2>Því miður er liðið sem þú valdir vitlaust...<br>' + mynd.title() + '</h2>' \
           '<img src="/static/'+mynd+'_logo.svg" width="200">' \
           '<h1>Án efa er besta liðið Vega Squadron</h1><br>' \
           '<img src="/static/vega_logo.svg" width="200"></img>' \
           '<h3><a href="/..">Til baka</a></h3>'


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./resources')


@error(404)
def error404(error):
    return '<h1>Úps...</h1><h3>Síðan sem þú baðst um finnst ekki.</h3>' \
           '<h3><a href="/">Til baka</a></h3>'



run()
