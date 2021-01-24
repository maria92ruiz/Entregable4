from silence.decorators import endpoint

@endpoint(
    route="/professors",
    method="GET",
    sql="SELECT * FROM professors",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/professors/$departmentId",
    method="GET",
    sql="SELECT * FROM professors WHERE departmentId = $departmentId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/professors",
    method="POST",
    sql="INSERT INTO professors (name, city) VALUES ($name, $city)",
    auth_required=True,
)
def add(name, city):
    pass

###############################################################################

@endpoint(
    route="/professors/$departmentId",
    method="PUT",
    sql="UPDATE professors SET name = $name, city = $city WHERE departmentId = $departmentId",
    auth_required=True,
)
def update(name, city):
    pass

###############################################################################

@endpoint(
    route="/professors/$departmentId",
    method="DELETE",
    sql="DELETE FROM professors WHERE departmentId = $departmentId",
    auth_required=True,
)
def delete():
    pass