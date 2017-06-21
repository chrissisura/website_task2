{% extends 'music/base.html' %}
{% block title %}register{% endblock %}

{% block body %}
	<div class="container-fluid">
			<div class="row">
			<div class="col-sm-12 col-md-7">
				<div class="panel-body">
					<h3>Create a new Account</h3>
					<form class="form-horizontal" action="" method="post" enctype="multipart/form-data">
						{%csrf_token %}
						{% include 'music/form-template.html' %}
						<div class="form-group">
							<div class="col-sm-offset-2 col-sm-10">
								<button type="submit" class="btn btn-success">Submit</button>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>


{% endblock %}