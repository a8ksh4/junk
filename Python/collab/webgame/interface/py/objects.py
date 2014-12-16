from cgi import parse_qs, escape
import MySQLdb

html = """
<canvas id="radar" width="650" height="650" style="border: 1px solid #000000;">Please upgrade your browser to support HTML5</canvas>

<script type="text/javascript">

var c=document.getElementById("radar");
var r=c.getContext("2d");
r.moveTo(0,325);
r.lineTo(650,325);
r.moveTo(325,0);
r.lineTo(325,650);
r.stroke();
"""
posthtml="""</script>"""
def draw_object(x,y,name):
	object= """
r.beginPath();
r.arc(%s,%s,10,0,2*Math.PI);
r.stroke();
r.font="12px Arial";
r.fillText("%s",%s,%s);
""" 
	q=object % (x,y,name,x,y)
	return q


def getlocations():
	db = MySQLdb.connect('localhost', 'root', 'R1ven', 'Web_game')
	cur = db.cursor()
	cur.execute("SELECT x_location, y_location, object_name FROM Locations")
	data = cur.fetchall()
	return data

def application(environ, start_response):
	response_body=html
	locations=getlocations()
	for location in locations:
		response_body+=draw_object(location[0]+325,location[1]+325,location[2])
	response_body+=draw_object(16+325,32+325,"ALPHA125")
	response_body+=posthtml
	start_response('200 OK', [('Content-Type', 'text/html')])

	return [response_body]
