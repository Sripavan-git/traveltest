from flask import Blueprint, render_template,request

sec= Blueprint("sec",__name__, static_folder="static", template_folder="templates")

@sec.route("/australia")
def aus():
	return render_template("aus.html")

@sec.route("/transaction", methods=["GET","POST"])
def trans():
	try:
		if request.method=="POST":
			print("posttttt")
			return "<h1> Post reqq</h1>"
			# return render_template("aus.html")
		else:
			print("not a posttt: "+request.method )
	except Exception as e:
		print(e)
	return render_template("trans.html")
	